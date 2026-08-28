/* Small site-wide compatibility fixes for older Buna pages. */
(function(){
  const path=window.location.pathname.replace(/\/$/,'');

  if(path.endsWith('/buna-culinary-school') || path.endsWith('/buna-culinary-school.html')){
    const style=document.createElement('style');
    style.textContent=`
      body{height:auto!important;min-height:100dvh!important;display:block!important;overflow-y:auto!important}
      .chat-outer{display:block!important;max-width:720px!important;width:100%!important;margin:0 auto!important;padding:0 20px!important;min-height:0!important}
      .chat-window{display:flex!important;flex-direction:column!important;gap:20px!important;overflow:visible!important;height:auto!important;max-height:none!important;min-height:0!important;padding:28px 0 16px!important}
      .input-area{position:static!important;background:#fdfaf4!important;padding:16px 0 28px!important}
      @media(max-width:600px){.chat-outer{padding:0 14px!important}.input-row{align-items:stretch!important}.send-btn{height:auto!important;min-height:52px!important}}
    `;
    document.head.appendChild(style);

    window.scrollToBottom=function(){
      const chat=document.getElementById('chatWindow');
      if(!chat) return;
      const last=chat.lastElementChild;
      if(last && typeof last.scrollIntoView==='function'){
        last.scrollIntoView({behavior:'smooth',block:'end'});
      }
    };
  }

  if(path.endsWith('/catalogue') || path.endsWith('/catalogue.html')){
    const oldHeader=document.querySelector('body > header');
    const hero=document.querySelector('.container .hero');
    const oldNav=oldHeader && oldHeader.querySelector('.nav');

    if(oldHeader) oldHeader.style.display='none';

    if(hero && oldNav && !document.getElementById('catalogue-page-index')){
      const wrap=document.createElement('details');
      wrap.id='catalogue-page-index';
      wrap.className='catalogue-page-index';
      wrap.open=window.innerWidth>=769;

      const summary=document.createElement('summary');
      summary.textContent='On this page';
      wrap.appendChild(summary);

      const links=document.createElement('div');
      links.className='catalogue-page-index-links';

      Array.from(oldNav.querySelectorAll('a')).forEach(function(a){
        if(!a.getAttribute('href') || !a.getAttribute('href').startsWith('#')) return;
        const copy=document.createElement('a');
        copy.href=a.getAttribute('href');
        copy.textContent=a.textContent.trim();
        links.appendChild(copy);
      });

      wrap.appendChild(links);
      hero.insertAdjacentElement('afterend',wrap);

      const style=document.createElement('style');
      style.textContent=`
        .catalogue-page-index{max-width:900px;margin:-54px auto 70px;border-top:1px solid var(--subtle);border-bottom:1px solid var(--subtle);padding:16px 0;background:transparent}
        .catalogue-page-index summary{cursor:pointer;list-style:none;font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);font-weight:600;padding:0 4px}
        .catalogue-page-index summary::-webkit-details-marker{display:none}
        .catalogue-page-index summary:after{content:' +';float:right;font-size:1rem;font-weight:400}
        .catalogue-page-index[open] summary:after{content:' -'}
        .catalogue-page-index-links{display:flex;flex-wrap:wrap;gap:8px 18px;padding:16px 4px 2px}
        .catalogue-page-index-links a{font-size:.9rem;color:var(--gray);text-decoration:none;border-bottom:1px solid transparent}
        .catalogue-page-index-links a:hover{color:var(--accent);border-bottom-color:var(--accent)}
        @media(max-width:768px){
          .catalogue-page-index{margin:-62px 0 48px;padding:14px 0}
          .catalogue-page-index-links{display:grid;grid-template-columns:1fr 1fr;gap:8px 12px}
          .catalogue-page-index-links a{padding:8px 0;border-bottom:1px solid #e6dfda;font-size:.88rem}
        }
      `;
      document.head.appendChild(style);
    }
  }
})();