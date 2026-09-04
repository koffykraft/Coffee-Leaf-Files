export async function onRequest(context) {
  // Buna v2 pages own their navigation and presentation. The old middleware
  // injected a second global navigation into every HTML response, creating
  // duplicate bars on pages that already had local/site navigation.
  // Keep middleware transparent: Cloudflare serves the requested asset or
  // Pages Function without mutating reader-facing HTML.
  return context.next();
}
