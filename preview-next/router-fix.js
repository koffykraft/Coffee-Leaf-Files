(() => {
  const INTERNAL_PREFIX = '?page=';

  function parseHash() {
    const raw = location.hash.startsWith('#') ? location.hash.slice(1) : '';
    if (!raw) return null;
    const params = new URLSearchParams(raw);
    const nextPage = params.get('page');
    if (!nextPage) return null;
    return {
      page: nextPage,
      depth: params.get('depth') || 'look'
    };
  }

  function toHashHref(id, nextDepth) {
    const params = new URLSearchParams();
    params.set('page', id);
    if (nextDepth) params.set('depth', nextDepth);
    return `#${params.toString()}`;
  }

  function renderCurrent() {
    const route = parseHash();
    if (route) {
      page = route.page;
      depth = route.depth;
    }

    document.getElementById('nav').innerHTML = nav.map(([id, label]) =>
      `<a class="${page === id ? 'active' : ''}" href="${toHashHref(id)}">${label}</a>`
    ).join('');

    let html;
    if (page === 'home') html = home();
    else if (page === 'cup') html = cup();
    else if (page === 'traditions') html = traditionsHome();
    else if (traditionData[page]) html = tradition(page);
    else if (page === 'processing') html = processing();
    else if (generic[page]) html = genericPage(page);
    else {
      page = 'home';
      depth = 'look';
      html = home();
    }

    document.getElementById('app').innerHTML = html;
  }

  function routeTo(nextPage, nextDepth = 'look', push = true) {
    page = nextPage || 'home';
    depth = nextDepth || 'look';
    const href = toHashHref(page, depth === 'look' ? null : depth);
    if (push) history.pushState({ page, depth }, '', href);
    else history.replaceState({ page, depth }, '', href);
    renderCurrent();
    window.scrollTo({ top: 0, behavior: 'auto' });
  }

  document.addEventListener('click', (event) => {
    const link = event.target.closest('a');
    if (!link) return;

    const rawHref = link.getAttribute('href') || '';

    if (rawHref.startsWith(INTERNAL_PREFIX)) {
      event.preventDefault();
      const params = new URLSearchParams(rawHref.slice(1));
      routeTo(params.get('page') || 'home', params.get('depth') || 'look');
      return;
    }

    if (rawHref.startsWith('#page=')) {
      event.preventDefault();
      const params = new URLSearchParams(rawHref.slice(1));
      routeTo(params.get('page') || 'home', params.get('depth') || 'look');
    }
  });

  window.addEventListener('popstate', () => renderCurrent());
  window.addEventListener('hashchange', () => renderCurrent());

  const initial = parseHash();
  if (initial) {
    page = initial.page;
    depth = initial.depth;
    renderCurrent();
  } else if (location.search.includes('page=')) {
    const params = new URLSearchParams(location.search);
    const initialPage = params.get('page') || 'home';
    const initialDepth = params.get('depth') || 'look';
    routeTo(initialPage, initialDepth, false);
  } else {
    routeTo(page || 'home', depth || 'look', false);
  }
})();
