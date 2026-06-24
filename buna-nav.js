/* buna-nav.js — Shared navigation for the Buna Coffee Leaf Library
   Drop this file in the repository root.
   Add this to every page, just before </body>:
   <script src="buna-nav.js"></script>
   For pages inside /vocab/, use:
   <script src="../buna-nav.js"></script>
*/

(function () {

    /* ── Detect depth ── */
    const inVocab = window.location.pathname.includes('/vocab/');
    const root = inVocab ? '../' : '';

    /* ── Styles ── */
    const style = document.createElement('style');
    style.textContent = `
        #buna-nav {
            background: #1a1a1a;
            position: sticky;
            top: 0;
            z-index: 999;
            width: 100%;
        }
        #buna-nav-inner {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            overflow-x: auto;
            scrollbar-width: none;
            align-items: center;
        }
        #buna-nav-inner::-webkit-scrollbar { display: none; }
        #buna-nav a {
            color: rgba(255,255,255,0.55);
            text-decoration: none;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 0.78em;
            font-weight: 600;
            letter-spacing: 0.04em;
            padding: 13px 16px;
            white-space: nowrap;
            border-bottom: 2px solid transparent;
            transition: color 0.15s, border-color 0.15s;
            display: block;
        }
        #buna-nav a:hover {
            color: #ffffff;
            border-bottom-color: rgba(255,255,255,0.3);
        }
        #buna-nav a.buna-nav-home {
            color: #d4c5c0;
            border-right: 1px solid rgba(255,255,255,0.12);
            padding-right: 18px;
            margin-right: 4px;
        }
        #buna-nav a.buna-nav-active {
            color: #ffffff;
            border-bottom-color: #d4c5c0;
        }
        #buna-nav a.buna-nav-vocab {
            color: rgba(160,200,160,0.8);
            margin-left: auto;
            border-left: 1px solid rgba(255,255,255,0.1);
        }
        #buna-nav a.buna-nav-vocab:hover { color: #a0d0a0; }
        @media (max-width: 600px) {
            #buna-nav a { font-size: 0.72em; padding: 12px 12px; }
        }
    `;
    document.head.appendChild(style);

    /* ── Nav links ── */
    const links = [
        { label: 'Buna Library', href: root + 'index.html', cls: 'buna-nav-home' },
        { label: 'D1 · Begin', href: root + 'begin-with-a-cup.html' },
        { label: 'D2 · Traditions', href: root + 'the-foliage-of-buna.html' },
        { label: 'D3 · Processing', href: root + 'citane-process-compass.html' },
        { label: 'D4 · Chemistry', href: root + 'citane-reactive-landscape.html' },
        { label: 'D5 · Tools', href: root + 'citane-terrain-map.html' },
        { label: 'D6 · Sensory', href: root + 'buna-sensory-school.html' },
        { label: 'D7 · Culinary', href: root + 'buna-culinary.html' },
        { label: 'D8 · Vocabulary', href: root + 'vocab/index.html', cls: 'buna-nav-vocab' },
        { label: 'Catalogue', href: root + 'catalogue.html' },
    ];

    /* ── Build nav ── */
    const nav = document.createElement('nav');
    nav.id = 'buna-nav';
    const inner = document.createElement('div');
    inner.id = 'buna-nav-inner';

    const currentPath = window.location.pathname;

    links.forEach(function (link) {
        const a = document.createElement('a');
        a.href = link.href;
        a.textContent = link.label;
        if (link.cls) a.classList.add(link.cls);

        /* Mark active page */
        const linkFile = link.href.split('/').pop();
        if (currentPath.endsWith(linkFile) || currentPath.endsWith(linkFile.replace('.html', ''))) {
            a.classList.add('buna-nav-active');
        }

        inner.appendChild(a);
    });

    nav.appendChild(inner);

    /* ── Insert after <header> if present, else at top of <body> ── */
    const header = document.querySelector('header');
    if (header && header.nextSibling) {
        header.parentNode.insertBefore(nav, header.nextSibling);
    } else if (header) {
        header.parentNode.appendChild(nav);
    } else {
        document.body.insertBefore(nav, document.body.firstChild);
    }

})();
