const P=[['ridge','Ridge Jacket',89,'','n1'],['slate','Slate Hoodie',64,'','n2'],['volt','Volt Shell',72,'','n3'],['dusk','Dusk Parka',119,'','n4'],['arc','Arc Windbreaker',58,'','n5'],['moss','Moss Overshirt',76,'','n6']];
let mem=[];const st={get(){try{return JSON.parse(localStorage.getItem('norte_cart')||'[]')}catch(_){return mem}},set(v){mem=v;try{localStorage.setItem('norte_cart',JSON.stringify(v))}catch(_){}}};
const $=s=>document.querySelector(s),money=n=>'$'+n.toFixed(2),find=id=>P.find(p=>p[0]===id);
const art=p=>'<div class="art ph im"><img src="assets/img/'+p[4]+'.jpg" alt="'+p[1]+'"></div>';
const card=(p,i)=>'<a class="pc rv" href="product.html?id='+p[0]+'" data-c>'+art(p)+'<div class="m"><span>0'+(i+1)+'</span><span>'+money(p[2])+'</span></div><h3>'+p[1]+'</h3></a>';
function badge(){const n=st.get().reduce((s,i)=>s+i.q,0);document.querySelectorAll('[data-cart]').forEach(e=>e.textContent=n)}
function totals(){const c=st.get(),sub=c.reduce((s,i)=>s+find(i.id)[2]*i.q,0),ship=sub===0||sub>=60?0:6;return{c,sub,ship,tot:sub+ship}}
function sumHTML(t){return '<div>Subtotal <span style="float:right">'+money(t.sub)+'</span></div><div>Shipping <span style="float:right">'+(t.ship?money(t.ship):'Free')+'</span></div><div><b>Total <span style="float:right">'+money(t.tot)+'</span></b></div>'}
const pg=document.body.dataset.page;
if(pg==='home')$('#feat').innerHTML=P.slice(0,3).map(card).join('');
if(pg==='shop')$('#all').innerHTML=P.map(card).join('');
if(pg==='product'){const p=find(new URLSearchParams(location.search).get('id'))||P[0];let size='M';
$('#pp').innerHTML=art(p)+'<div><span class="note">In stock · ships in 24h</span><h1>'+p[1]+'</h1><div class="pr">'+money(p[2])+'</div><p>Technical shell with sealed seams, a roomy fit and colors you can spot from across the street. Water resistant and light enough to carry all day.</p><div class="sz" id="sz">'+['S','M','L','XL'].map(s=>'<button class="'+(s==='M'?'on':'')+'">'+s+'</button>').join('')+'</div><button class="btn" id="add">+ Add to cart</button></div>';
$('#sz').onclick=e=>{if(e.target.tagName==='BUTTON'){size=e.target.textContent;[...$('#sz').children].forEach(b=>b.classList.toggle('on',b===e.target))}};
$('#add').onclick=()=>{const c=st.get(),k=c.find(i=>i.id===p[0]&&i.s===size);k?k.q++:c.push({id:p[0],s:size,q:1});st.set(c);badge();$('#add').textContent='Added ✓'};
$('#more').innerHTML=P.filter(x=>x!==p).slice(0,3).map(card).join('')}
function renderCart(){const t=totals();if(!t.c.length){$('#cart').innerHTML='<p>Your cart is empty.</p><p style="margin-top:3vh"><a class="btn" href="shop.html">Go to the shop</a></p>';return}
$('#cart').innerHTML=t.c.map((i,n)=>{const p=find(i.id);return '<div class="crow">'+art(p)+'<div><h3>'+p[1]+'</h3><small>Size '+i.s+' · '+money(p[2])+'</small></div><div class="qty"><button data-d="-1" data-n="'+n+'">−</button><span>'+i.q+'</span><button data-d="1" data-n="'+n+'">+</button></div><b>'+money(p[2]*i.q)+'</b></div>'}).join('')+'<div class="sum">'+sumHTML(t)+'<a class="btn" href="checkout.html">Checkout →</a></div>';initArt();document.querySelectorAll('.art').forEach(e=>e.classList.add('in'))}
if(pg==='cart'){renderCart();$('#cart').onclick=e=>{const b=e.target.closest('button[data-n]');if(!b)return;const c=st.get(),i=c[+b.dataset.n];i.q+=+b.dataset.d;if(i.q<1)c.splice(+b.dataset.n,1);st.set(c);badge();renderCart()}}
if(pg==='checkout'){const t=totals();if(!t.c.length){$('#co').innerHTML='<p>Your cart is empty.</p>'}else{$('#sumbox').innerHTML=t.c.map(i=>'<div>'+find(i.id)[1]+' ('+i.s+') × '+i.q+'</div>').join('')+sumHTML(t);
$('#form').onsubmit=e=>{e.preventDefault();const n='NRT-'+Math.floor(1000+Math.random()*9000);st.set([]);badge();$('#co').outerHTML='<div class="ok"><span class="note">Demo store · no payment was taken</span><h1>Thank you.</h1><p style="margin:3vh 0">Order '+n+' is confirmed. A real store would email your receipt now.</p><a class="btn" href="shop.html">Keep shopping</a></div>'}}}
badge();initArt();
