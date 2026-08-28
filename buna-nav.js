/* buna-nav.js - Shared navigation for the Buna Coffee Leaf Library */
(function(){
 if(document.getElementById('buna-nav')) return;
 const inVocab=window.location.pathname.includes('/vocab/');
 const root=inVocab?'../':'';
 const currentPath=window.location.pathname;

 const doors=[
  {door:'Door One',short:'D1 Begin',title:'Begin',href:root+'begin-with-a-cup.html',items:[
   ['Begin With a Cup',root+'begin-with-a-cup.html'],
   ['Sensory Landscape',root+'sensory-landscape-of-coffee-leaf.html']
  ]},
  {door:'Door Two',short:'D2 Traditions',title:'Living Traditions',href:root+'the-foliage-of-buna.html',items:[
   ['The Foliage of Buna',root+'the-foliage-of-buna.html'],
   ['Engere',root+'engere-intro.html'],
   ['Kuti',root+'kuti-intro.html'],
   ['Chemo',root+'chemo-intro.html'],
   ['Kawa Daun',root+'kawa-daun-intro.html']
  ]},
  {door:'Door Three',short:'D3 Processing',title:'Processing and Experiment',href:root+'citane-process-compass.html',items:[
   ['Process Compass',root+'citane-process-compass.html'],
   ['From Leaf to Cup',root+'citane-processing-manual.html'],
   ['Experimental Pathways',root+'citane-processing-protocols.html'],
   ['Field Notes',root+'citane-hack-grill-wilted-leaves.html']
  ]},
  {door:'Door Four',short:'D4 Chemistry',title:'Chemistry and Framework',href:root+'citane-reactive-landscape.html',items:[
   ['Reactive Landscape',root+'citane-reactive-landscape.html'],
   ['Sensory Chemistry',root+'sensory-chemistry.html'],
   ['How We Treat Evidence',root+'the-foliage-of-buna.html#evidence']
  ]},
  {door:'Door Five',short:'D5 Tools',title:'Interactive Tools',href:root+'citane-terrain-map.html',items:[
   ['Terrain Map',root+'citane-terrain-map.html'],
   ['Flavour Landscape',root+'clt-flavour-wheel.html'],
   ['Flavour Logic Board',root+'citane-logic-board.html'],
   ['Epsilon Board',root+'citane-epsilon-board.html']
  ]},
  {door:'Door Six',short:'D6 Sensory',title:'Sensory School',href:root+'buna-sensory-school.html',items:[
   ['Sensory School',root+'buna-sensory-school.html'],
   ['Before You Begin',root+'sensory-already.html'],
   ['The Encounter',root+'sensory-encounter.html'],
   ['The Language',root+'sensory-language.html'],
   ['The Chemistry',root+'sensory-chemistry.html'],
   ['The Companion',root+'sensory-companion.html']
  ]},
  {door:'Door Seven',short:'D7 Culinary',title:'Buna Culinary',href:root+'buna-culinary.html',items:[
   ['The Leaf at the Table',root+'buna-culinary.html'],
   ['Leaf and Elements',root+'buna-culinary-elements.html'],
   ['Preparations',root+'buna-culinary-preparations.html'],
   ['Concepts',root+'buna-culinary-concepts.html'],
   ['Kitchen Companion',root+'buna-culinary-school.html']
  ]},
  {door:'Door Eight',short:'D8 Vocabulary',title:'Buna Vocabulary',href:root+'vocab/index.html',items:[
   ['Vocabulary Index',root+'vocab/index.html'],
   ['Leaf Origin',root+'vocab/leaf-origin.html'],
   ['Process',root+'vocab/process.html'],
   ['Flavour and Sensory',root+'vocab/sensory-flavour.html'],
   ['Ritual Context',root+'vocab/ritual-context.html']
  ]},
  {door:'Door Nine',short:'D9 Biology',title:'Coffee Leaf and Human Biology',href:root+'coffee-leaf-human-biology.html',items:[
   ['Overview',root+'coffee-leaf-human-biology.html'],
   ['From the Cup to the Body',root+'post-cup-landscape.html'],
   ['Gut Barrier and Microbiome',root+'gut-barrier-microbiome.html'],
   ['Metabolic Signals',root+'metabolic-signals.html'],
   ['Rest and Stress',root+'rest-stress-response.html'],
   ['Safety and Variability',root+'safety-dose-variability.html'],
   ['What We Still Do Not Know',root+'research-gaps.html']
  ]}
 ];

 const style=document.createElement('style');
 style.textContent=`
 #buna-nav{background:#1a1a1a;position:sticky;top:0;z-index:999;width:100%;font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif}
 #buna-nav-inner{max-width:1100px;margin:0 auto;display:flex;overflow-x:auto;scrollbar-width:none;align-items:center}
 #buna-nav-inner::-webkit-scrollbar{display:none}
 #buna-nav a{color:rgba(255,255,255,.55);text-decoration:none;font-size:.78em;font-weight:600;letter-spacing:.04em;padding:13px 16px;white-space:nowrap;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;display:block}
 #buna-nav a:hover{color:#fff;border-bottom-color:rgba(255,255,255,.3)}
 #buna-nav a.buna-nav-home{color:#d4c5c0;border-right:1px solid rgba(255,255,255,.12);padding-right:18px;margin-right:4px}
 #buna-nav a.buna-nav-active{color:#fff;border-bottom-color:#d4c5c0}
 #buna-nav a.buna-nav-vocab{color:rgba(160,200,160,.8)}
 #buna-mobile-row,#buna-tree{display:none}
 @media(max-width:700px){
  #buna-nav-inner{display:none}
  #buna-mobile-row{display:flex;align-items:center;justify-content:space-between;min-height:50px}
  #buna-mobile-row a{border:0!important;color:#d4c5c0;padding:14px 18px;font-size:.82rem}
  #buna-map-toggle{appearance:none;border:0;border-left:1px solid rgba(255,255,255,.12);background:#1a1a1a;color:#fff;font:600 .82rem 'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif;letter-spacing:.04em;padding:15px 18px;cursor:pointer}
  #buna-tree{display:none;background:#f8f4ec;color:#2b2b2b;border-bottom:1px solid #d8d0c2;max-height:72vh;overflow-y:auto;-webkit-overflow-scrolling:touch;box-shadow:0 8px 20px rgba(0,0,0,.12)}
  #buna-tree.open{display:block}
  .buna-tree-head{padding:16px 18px 10px;font-size:.7rem;text-transform:uppercase;letter-spacing:.16em;color:#8a7c5e}
  .buna-door{border-top:1px solid #e1d9cc}
  .buna-door summary{list-style:none;cursor:pointer;padding:14px 18px;display:grid;grid-template-columns:78px 1fr 18px;gap:10px;align-items:center}
  .buna-door summary::-webkit-details-marker{display:none}
  .buna-door-no{font-size:.68rem;text-transform:uppercase;letter-spacing:.11em;color:#9a8f80}
  .buna-door-title{font-family:Georgia,'Times New Roman',serif;font-size:1rem;color:#2b2b2b}
  .buna-door-caret{font-size:.8rem;color:#8a7c5e;transition:transform .15s}
  .buna-door[open] .buna-door-caret{transform:rotate(90deg)}
  .buna-branches{padding:0 18px 14px 96px}
  .buna-branches a{padding:8px 0!important;border:0!important;color:#5c564f!important;font-size:.8rem!important;font-weight:500!important;white-space:normal!important}
  .buna-branches a.current{color:#1a1a1a!important;font-weight:700!important}
  .buna-tree-foot{display:flex;gap:8px;padding:14px 18px 18px;border-top:1px solid #e1d9cc}
  .buna-tree-foot a{flex:1;text-align:center;padding:10px!important;border:1px solid #d6cdbc!important;color:#5f4a42!important;background:#fff;font-size:.75rem!important}
 }
 `;
 document.head.appendChild(style);

 const nav=document.createElement('nav');
 nav.id='buna-nav';

 const inner=document.createElement('div');
 inner.id='buna-nav-inner';
 const desktop=[
  {label:'Buna Library',href:root+'index.html',cls:'buna-nav-home'},
  ...doors.map(d=>({label:d.short,href:d.href,cls:d.door==='Door Eight'?'buna-nav-vocab':''})),
  {label:'Catalogue',href:root+'catalogue.html'}
 ];
 desktop.forEach(function(link){
  const a=document.createElement('a');a.href=link.href;a.textContent=link.label;if(link.cls)a.classList.add(link.cls);
  const linkFile=link.href.split('/').pop();if(currentPath.endsWith(linkFile)||currentPath.endsWith(linkFile.replace('.html','')))a.classList.add('buna-nav-active');
  inner.appendChild(a);
 });
 nav.appendChild(inner);

 const mobile=document.createElement('div');mobile.id='buna-mobile-row';
 const home=document.createElement('a');home.href=root+'index.html';home.textContent='Buna Library';
 const toggle=document.createElement('button');toggle.id='buna-map-toggle';toggle.type='button';toggle.setAttribute('aria-expanded','false');toggle.textContent='Library Map ▾';
 mobile.appendChild(home);mobile.appendChild(toggle);nav.appendChild(mobile);

 const tree=document.createElement('div');tree.id='buna-tree';
 const head=document.createElement('div');head.className='buna-tree-head';head.textContent='Library Map';tree.appendChild(head);
 doors.forEach(function(d){
  const det=document.createElement('details');det.className='buna-door';
  const allFiles=[d.href].concat(d.items.map(x=>x[1]));
  if(allFiles.some(h=>currentPath.endsWith(h.split('/').pop())||currentPath.endsWith(h.split('/').pop().replace('.html',''))))det.open=true;
  const sum=document.createElement('summary');
  sum.innerHTML='<span class="buna-door-no">'+d.door+'</span><span class="buna-door-title">'+d.title+'</span><span class="buna-door-caret">›</span>';
  det.appendChild(sum);
  const branches=document.createElement('div');branches.className='buna-branches';
  d.items.forEach(function(item){const a=document.createElement('a');a.href=item[1];a.textContent=item[0];const file=item[1].split('/').pop();if(currentPath.endsWith(file)||currentPath.endsWith(file.replace('.html','')))a.classList.add('current');branches.appendChild(a);});
  det.appendChild(branches);tree.appendChild(det);
 });
 const foot=document.createElement('div');foot.className='buna-tree-foot';
 [['Catalogue',root+'catalogue.html'],['Vocabulary',root+'vocab/index.html']].forEach(function(x){const a=document.createElement('a');a.href=x[1];a.textContent=x[0];foot.appendChild(a);});
 tree.appendChild(foot);nav.appendChild(tree);

 toggle.addEventListener('click',function(){const open=tree.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Close Map ▴':'Library Map ▾';});
 document.addEventListener('click',function(e){if(window.innerWidth<=700&&!nav.contains(e.target)&&tree.classList.contains('open')){tree.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Library Map ▾';}});

 const localNav=Array.from(document.body.children).find(function(el){return el.tagName==='NAV'&&el.id!=='buna-nav';});
 const header=document.querySelector('header');
 if(localNav){localNav.insertAdjacentElement('afterend',nav);}
 else if(header&&header.nextSibling){header.parentNode.insertBefore(nav,header.nextSibling);}
 else if(header){header.parentNode.appendChild(nav);}
 else{document.body.insertBefore(nav,document.body.firstChild);}
})();