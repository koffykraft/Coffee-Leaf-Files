export async function onRequest(context) {
  const response = await context.next();
  const contentType = response.headers.get('Content-Type') || '';

  if (!contentType.toLowerCase().includes('text/html')) {
    return response;
  }

  return new HTMLRewriter()
    .on('body', {
      element(element) {
        element.append('<script src="/buna-nav.js"></script><script src="/buna-site-fixes.js"></script>', { html: true });
      }
    })
    .transform(response);
}
