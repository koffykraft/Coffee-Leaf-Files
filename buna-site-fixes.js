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
})();