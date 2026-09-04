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
function crumbs(){
  if(path==='/')return'';
  const bits=[`<a href="/">Library</a>`];
  if(page.group&&path!==G[page.group].look) bits.push(`<a href="${G[page.group].look}">${h(G[page.group].label)}</a>`);
  bits.push(`<span aria-current="page">${h(page.title)}</span>`);
  return `<div class="breadcrumbs">${bits.join('<span>/</span>')}</div>`;
}
function depth(){if(!page.group)return'';const g=G[page.group];let labels=[['look','LOOK',g.look],['understand','UNDERSTAND',g.understand],['examine','EXAMINE',g.examine]];return `<nav class="depthbar" aria-label="Depth">${labels.map(([k,l,u])=>`<a href="${u}" class="${page.depth===k?'active':''}">${l}</a>`).join('')}</nav>`;}
function claims(){if(!page.claims?.length)return'';return `<section><h2>Evidence position</h2>${page.claims.map(id=>{const c=C[id];if(!c)return'';return `<div class="evidence"><div class="evidence-label">${h(c.type)} · ${h(c.level)}</div><p><strong>${h(c.plain)}</strong></p><p>${h(c.detail)}</p>${c.sources?.length?`<p class="source-note">Sources: ${c.sources.map(x=>S[x]?`<a href="${S[x].url}">${h(S[x].year+' '+S[x].type)}</a>`:'').join(' · ')}</p>`:''}</div>`;}).join('')}</section>`;}
function sources(){if(!page.sources?.length)return'';return `<section><h2>Sources for this page</h2><ul class="source-list">${page.sources.map(id=>{const s=S[id];if(!s)return'';return `<li><a href="${s.url}"><strong>${h(s.title)}</strong></a><div class="source-note">${h(s.year)} · ${h(s.type)} — ${h(s.note)}</div></li>`;}).join('')}</ul></section>`;}
function catalogue(){const el=document.getElementById('catalogue-grid');if(!el)return;const order=Object.entries(P).filter(([r,p])=>r!=='/'&&r!=='/catalogue/'&&r!=='/sources/');el.innerHTML=order.map(([r,p])=>`<a class="card" href="${r}"><div class="kicker">${h(p.eye||'Library')}</div><h3>${h(p.title)}</h3><p>${h(p.lead||'')}</p></a>`).join('');}
function sourceRegistry(){const el=document.getElementById('source-registry');if(!el)return;el.innerHTML=`<ul class="source-list">${Object.values(S).map(s=>`<li><a href="${s.url}"><strong>${h(s.title)}</strong></a><div class="source-note">${h(s.year)} · ${h(s.type)} — ${h(s.note)}</div></li>`).join('')}</ul>`;}
function terms(){const el=document.getElementById('term-list');if(!el)return;el.innerHTML=Object.entries(T).map(([id,t])=>`<div class="card"><div class="kicker">Term</div><h3>${h(id.replace(/-/g,' '))}</h3><p>${h(t.plain)}</p></div>`).join('');}
function toolLaunches(){
  if(path!=='/tools/')return;
  const main=document.getElementById('content');
  const notice=main.querySelector('.notice');
  const block=document.createElement('section');
  block.innerHTML=`<h2>Open the current tools</h2><div class="cards two"><a class="card" href="/citane-terrain-map.html"><div class="kicker">Current interactive tool</div><h3>Terrain Map</h3><p>Explore growing-condition relationships. Treat causal-looking edges according to their evidence status.</p></a><a class="card" href="/citane-flavour-landscape.html"><div class="kicker">Current interactive tool</div><h3>Flavour Landscape</h3><p>Explore sensory territories and process relationships.</p></a><a class="card" href="/citane-logic-board.html"><div class="kicker">Current interactive tool</div><h3>Logic Board</h3><p>Follow structured reasoning across traditions and process questions.</p></a><a class="card" href="/citane-epsilon-board.html"><div class="kicker">Speculative tool</div><h3>Epsilon Board</h3><p>Generate clearly labelled speculative directions, not validated instructions.</p></a></div><p class="notice">These are preserved interactive implementations. Their data relationships are being governed by the same evidence rules as the rebuilt Library; a tool does not become a source merely because it visualises a claim.</p>`;
  main.insertBefore(block,notice);
}
document.title=`${page.title} · Buna`;
document.getElementById('site-header').innerHTML=header();
document.getElementById('site-footer').innerHTML=footer();
document.getElementById('content').innerHTML=`${crumbs()}<header class="hero"><div class="eyebrow">${h(page.eye||'Buna')}</div><h1>${h(page.title)}</h1><p class="lead">${h(page.lead||'')}</p></header>${page.question?`<p class="question">${h(page.question)}</p>`:''}${depth()}${page.body||''}${claims()}${sources()}<div class="notice">Rebuild status: canonical v2 page. Claims are admitted only at the evidence level shown; older unverified pages remain outside the canonical navigation.</div>`;
const btn=document.querySelector('.nav-toggle'),gn=document.getElementById('global-nav');btn?.addEventListener('click',()=>{const open=gn.classList.toggle('open');btn.setAttribute('aria-expanded',String(open));});
catalogue();sourceRegistry();terms();toolLaunches();
})();
