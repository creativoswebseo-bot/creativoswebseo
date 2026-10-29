(()=>{const $=s=>[...document.querySelectorAll(s)],R=matchMedia('(prefers-reduced-motion:reduce)').matches,C=matchMedia('(pointer:coarse)').matches;let gi=0;
document.documentElement.classList.add('js');
function art(el){const[,a,b,c,d]=el.dataset.art.split(','),G='g'+gi++;
el.innerHTML='<svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="'+G+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+a+'"/><stop offset="1" stop-color="'+b+'"/></linearGradient></defs><rect width="400" height="500" fill="url(#'+G+')"/><circle cx="200" cy="270" r="170" fill="'+d+'" opacity=".14"/><path d="M135 130l-52 55-28 150 48 12 26-90v220h142V257l26 90 48-12-28-150-52-55q-65 45-130 0z" fill="'+c+'"/><path d="M200 175v300" stroke="'+d+'" stroke-width="3" opacity=".6"/><path d="M135 130q65 50 130 0" fill="none" stroke="'+d+'" stroke-width="4" opacity=".5"/><rect x="150" y="330" width="45" height="8" rx="4" fill="'+d+'" opacity=".5"/><rect x="205" y="330" width="45" height="8" rx="4" fill="'+d+'" opacity=".5"/></svg>'}
window.initArt=()=>$('[data-art]:not([data-d])').forEach(e=>{e.dataset.d=1;art(e)});
function split(el){let i=0;const w=document.createTreeWalker(el,4),ns=[];while(w.nextNode())ns.push(w.currentNode);ns.forEach(n=>{const f=document.createDocumentFragment();n.textContent.split(/(\s+)/).forEach(t=>{if(!t.trim()){f.append(t);return}const s=document.createElement('span');s.className='w';s.innerHTML='<span class="i" style="transition-delay:'+(i++*70)+'ms">'+t+'</span>';f.append(s)});n.replaceWith(f)});el.classList.add('sp')}
document.addEventListener('DOMContentLoaded',()=>{initArt();if(!R)$('h1,.sec h2').forEach(split);const ct=document.getElementById('ct');setTimeout(()=>ct&&ct.classList.remove('on'),60)});
addEventListener('pageshow',()=>{const ct=document.getElementById('ct');ct&&ct.classList.remove('on')});
if(R)return;
document.addEventListener('click',e=>{const a=e.target.closest('a[href]');if(!a||e.defaultPrevented||e.ctrlKey||e.metaKey||a.target||a.origin!==location.origin||a.hash&&a.pathname===location.pathname)return;const ct=document.getElementById('ct');if(!ct)return;e.preventDefault();ct.classList.add('on');setTimeout(()=>location.href=a.href,600)});
let tg=scrollY,cs=scrollY,ani=false,mx=0,my=0,cx=0,cy=0,ly=scrollY,sk=0;const cur=document.getElementById('cur');
if(!C){addEventListener('wheel',e=>{if(e.ctrlKey)return;e.preventDefault();tg=Math.max(0,Math.min(document.documentElement.scrollHeight-innerHeight,tg+e.deltaY*(e.deltaMode?32:1)));ani=true},{passive:false});addEventListener('scroll',()=>{if(!ani)tg=cs=scrollY})}
addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;$('.btn').forEach(b=>{const r=b.getBoundingClientRect(),x=mx-(r.left+r.width/2),y=my-(r.top+r.height/2);b.style.translate=Math.hypot(x,y)<110?x*.3+'px '+y*.3+'px':'0 0'})});
document.addEventListener('mouseover',e=>cur&&cur.classList.toggle('big',!!e.target.closest('[data-c],.pc,.btn')));
(function tick(){if(ani){cs+=(tg-cs)*.085;if(Math.abs(tg-cs)<.5){cs=tg;ani=false}scrollTo(0,cs)}
sk+=((scrollY-ly)-sk)*.08;ly=scrollY;$('.mqo').forEach(e=>e.style.transform='skewY('+Math.max(-4,Math.min(4,sk*.12)).toFixed(2)+'deg)');
$('.sp:not(.in),.rv:not(.in),.art:not(.in)').forEach(e=>{const r=e.getBoundingClientRect();if(r.top<innerHeight*.94&&r.bottom>0)e.classList.add('in')});
if(cur){cx+=(mx-cx)*.18;cy+=(my-cy)*.18;cur.style.transform='translate('+cx+'px,'+cy+'px)'}requestAnimationFrame(tick)})();
})();
