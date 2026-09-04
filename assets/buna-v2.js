(()=>{
const P=window.BUNA_PAGES||{},G=window.BUNA_GROUPS||{},S=window.BUNA_SOURCES||{},C=window.BUNA_CLAIMS||{},T=window.BUNA_TERMS||{};
const normalise=p=>{if(!p)return'/';p=p.replace(/index\.html$/,'');if(!p.endsWith('/'))p+='/';return p.replace(/\/+/g,'/');};
const path=normalise(location.pathname);
const page=P[path]||P['/'];
const nav=[['/','Library'],['/cup/','Begin'],['/traditions/','Traditions'],['/processing/','Processing'],['/chemistry/','Chemistry'],['/tools/','Tools'],['/sensory/','Sensory'],['/culinary/','Culinary'],['/vocabulary/','Vocabulary'],['/biology/','Biology']];
function h(s){return String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));}
function isCurrent(url){return path===url||((url!=='/')&&path.startsWith(url));}
function header(){const links=nav.map(([u,l])=>`<a href="${u}"${isCurrent(u)?' aria-current="page"':''}>${h(l)}</a>`).join('');return `<div class="topbar"><a class="brand" href="/"><img src="/buna-leaf.svg" alt=""><span>Buna Coffee Leaf Library</span></a><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="global-nav">Library Map</button></div><nav id="global-nav" class="global-nav" aria-label="Primary">${links}</nav>`;}
function footer(){return `<div class="footer-inner"><div>Buna Coffee Leaf Library · KoffyKraft · Karavaloor, Kerala</div><div><a href="/foundation/">Foundation</a> · <a href="/catalogue/">Catalogue</a> · <a href="/sources/">Sources</a></div></div>`;}
function crumbs(){if(path==='/')return'';let parts=[];if(page.group)parts.push(`<a href="${G[page.group].look}">${h(G[page.group].label)}</a>`);else parts.push(`<a href="/">Library</a>`);return `<div class="breadcrumbs"><a href="/">Library</a><span>/</span>${parts.join('')}</div>`;}
function depth(){if(!page.group)return'';const g=G[page.group];let labels=[['look','LOOK',g.look],['understand','UNDERSTAND',g.understand],['examine','EXAMINE',g.examine]];return `<nav class="depthbar" aria-label="Depth">${labels.map(([k,l,u])=>`<a href="${u}" class="${page.depth===k?'active':''}">${l}</a>`).join('')}</nav>`;}
function claims(){if(!page.claims?.length)return'';return `<section><h2>Evidence position</h2>${page.claims.map(id=>{const c=C[id];if(!c)return'';return `<div class="evidence"><div class="evidence-label">${h(c.type)} · ${h(c.level)}</div><p><strong>${h(c.plain)}</strong></p><p>${h(c.detail)}</p>${c.sources?.length?`<p class="source-note">Sources: ${c.sources.map(x=>S[x]?`<a href="${S[x].url}">${h(S[x].year+' '+S[x].type)}</a>`:'').join(' · ')}</p>`:''}</div>`;}).join('')}</section>`;}
function sources(){if(!page.sources?.length)return'';return `<section><h2>Sources for this page</h2><ul class="source-list">${page.sources.map(id=>{const s=S[id];if(!s)return'';return `<li><a href="${s.url}"><strong>${h(s.title)}</strong></a><div class="source-note">${h(s.year)} · ${h(s.type)} — ${h(s.note)}</div></li>`;}).join('')}</ul></section>`;}
function catalogue(){const el=document.getElementById('catalogue-grid');if(!el)return;const order=Object.entries(P).filter(([r,p])=>r!=='/'&&r!=='/catalogue/'&&r!=='/sources/');el.innerHTML=order.map(([r,p])=>`<a class="card" href="${r}"><div class="kicker">${h(p.eye||'Library')}</div><h3>${h(p.title)}</h3><p>${h(p.lead||'')}</p></a>`).join('');}
function sourceRegistry(){const el=document.getElementById('source-registry');if(!el)return;el.innerHTML=`<ul class="source-list">${Object.values(S).map(s=>`<li><a href="${s.url}"><strong>${h(s.title)}</strong></a><div class="source-note">${h(s.year)} · ${h(s.type)} — ${h(s.note)}</div></li>`).join('')}</ul>`;}
function terms(){const el=document.getElementById('term-list');if(!el)return;el.innerHTML=Object.entries(T).map(([id,t])=>`<div class="card"><div class="kicker">Term</div><h3>${h(id.replace(/-/g,' '))}</h3><p>${h(t.plain)}</p></div>`).join('');}
document.title=`${page.title} · Buna`;
document.getElementById('site-header').innerHTML=header();
document.getElementById('site-footer').innerHTML=footer();
document.getElementById('content').innerHTML=`${crumbs()}<header class="hero"><div class="eyebrow">${h(page.eye||'Buna')}</div><h1>${h(page.title)}</h1><p class="lead">${h(page.lead||'')}</p></header>${page.question?`<p class="question">${h(page.question)}</p>`:''}${depth()}${page.body||''}${claims()}${sources()}<div class="notice">Rebuild status: canonical v2 page. Claims are admitted only at the evidence level shown; older unverified pages remain outside the canonical navigation.</div>`;
const btn=document.querySelector('.nav-toggle'),gn=document.getElementById('global-nav');btn?.addEventListener('click',()=>{const open=gn.classList.toggle('open');btn.setAttribute('aria-expanded',String(open));});
catalogue();sourceRegistry();terms();
})();
