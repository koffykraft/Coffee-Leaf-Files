const ALLOWED_ORIGINS = new Set([
  "https://buna.koffykraft.coffee"
]);

function corsHeaders(origin) {
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
    "Cache-Control": "no-store"
  };
}

function allowedOrigin(origin) {
  if (ALLOWED_ORIGINS.has(origin)) return true;
  try {
    const host = new URL(origin).hostname;
    return host.endsWith(".pages.dev") || host.endsWith(".netlify.app");
  } catch {
    return false;
  }
}

function json(body, status, origin) {
  return Response.json(body, {
    status,
    headers: corsHeaders(origin)
  });
}

export async function onRequestOptions(context) {
  const origin = context.request.headers.get("Origin") || "";
  if (!allowedOrigin(origin)) return new Response(null, { status: 403 });
  return new Response(null, { status: 204, headers: corsHeaders(origin) });
}

export async function onRequestPost(context) {
  const origin = context.request.headers.get("Origin") || "";

  if (!allowedOrigin(origin)) {
    return json({ error: "Request origin is not allowed." }, 403, "https://buna.koffykraft.coffee");
  }

  if (!context.env.ANTHROPIC_API_KEY) {
    return json({ error: "The Companion is not configured." }, 503, origin);
  }

  try {
    const contentLength = Number(context.request.headers.get("Content-Length") || 0);
    if (contentLength > 60000) {
      return json({ error: "The request is too large. Please begin again." }, 413, origin);
    }

    const body = await context.request.json();
    const messages = Array.isArray(body.messages) ? body.messages : [];

    if (!messages.length || messages.length > 30) {
      return json({ error: "Please begin again." }, 400, origin);
    }

    const validMessages = messages.every(message =>
      message &&
      (message.role === "user" || message.role === "assistant") &&
      typeof message.content === "string" &&
      message.content.length <= 10000
    );

    if (!validMessages) {
      return json({ error: "The conversation could not be read." }, 400, origin);
    }

    const payload = {
      model: typeof body.model === "string" ? body.model : "claude-sonnet-4-6",
      max_tokens: Math.min(Number(body.max_tokens) || 4000, 4000),
      messages
    };

    if (typeof body.system === "string" && body.system.length <= 20000) {
      payload.system = body.system;
    }

    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": context.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Anthropic request failed", response.status, data?.error?.type || "unknown");
      const message = response.status === 429
        ? "The Companion is busy. Please try again shortly."
        : "The Companion is temporarily unavailable.";
      return json({ error: message }, response.status, origin);
    }

    return json(data, 200, origin);
  } catch (err) {
    console.error("Buna epsilon API error", err);
    return json({ error: "Something interrupted the request. Please try again." }, 500, origin);
  }
}
