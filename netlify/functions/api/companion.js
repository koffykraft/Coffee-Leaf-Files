export async function onRequestPost(context) {

  try {

    const body = await context.request.json();

    const payload = {
      model: "claude-sonnet-4-6",
      max_tokens: 4000,
      messages: body.messages
    };

    if (body.system) {
      payload.system = body.system;
    }

    const response = await fetch(
      "https://api.anthropic.com/v1/messages",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
          "x-api-key": context.env.ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01"
        },

        body: JSON.stringify(payload)
      }
    );

    const data = await response.json();

    return Response.json(data, {

      headers: {

        "Access-Control-Allow-Origin": "*"

      }

    });

  }

  catch(err) {

    return Response.json(

      {

        error: err.message

      },

      {

        status: 500

      }

    );

  }

}
