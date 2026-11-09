/* Nov8rs (Innovators) · motion engine */
(function(){
'use strict';

/* ---- settings you may need to change ---- */
var CFG={
  formEndpoint:'',            /* paste your GHL inbound webhook / form endpoint here */
  email:'hello@nov8rs.com',
  introOncePerSession:true
};

var doc=document.documentElement;
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
function clamp(v,a,b){a=a==null?0:a;b=b==null?1:b;return v<a?a:v>b?b:v}
function ease(t){return 1-Math.pow(1-t,3)}
function lerp(a,b,t){return a+(b-a)*t}
function store(k,v){try{if(v===undefined)return sessionStorage.getItem(k);sessionStorage.setItem(k,v)}catch(e){return null}}

/* ================= smooth scroll ================= */
var lenis=null;
if(window.Lenis&&!reduce){try{lenis=new Lenis({lerp:0.09,smoothWheel:true})}catch(e){lenis=null}}
document.addEventListener('click',function(e){
  var a=e.target.closest('a[href^="#"]');if(!a)return;
  var id=a.getAttribute('href');var el=id.length>1&&document.querySelector(id);if(!el)return;
  e.preventDefault();closeMenu();
  if(lenis)lenis.scrollTo(el,{duration:1.5,offset:-10});else el.scrollIntoView({behavior:reduce?'auto':'smooth'});
});

/* ================= quote CTA tracking ================= */
window.dataLayer=window.dataLayer||[];
document.addEventListener('click',function(e){
  var a=e.target.closest('[data-cta]');if(!a)return;
  window.dataLayer.push({event:'quote_click',cta_location:a.getAttribute('data-cta'),page:location.pathname});
});

/* ================= nav ================= */
var nav=$('.nav'),lastY=0;
var burger=$('.burger');
function closeMenu(){doc.classList.remove('menu-open');if(burger)burger.setAttribute('aria-expanded','false')}
if(burger)burger.addEventListener('click',function(){
  var open=!doc.classList.contains('menu-open');
  doc.classList.toggle('menu-open',open);burger.setAttribute('aria-expanded',String(open));
  if(lenis){open?lenis.stop():lenis.start()}
});
addEventListener('keydown',function(e){if(e.key==='Escape'){closeMenu();if(lenis)lenis.start()}});
$$('.mmenu a').forEach(function(a){a.addEventListener('click',function(){closeMenu();if(lenis)lenis.start()})});
var dropBtn=$('.links .hasdrop > button');
if(dropBtn){var drop=dropBtn.nextElementSibling;
  dropBtn.addEventListener('click',function(){var o=drop.classList.toggle('open');dropBtn.setAttribute('aria-expanded',String(o))});
  document.addEventListener('click',function(e){if(!e.target.closest('.hasdrop')){drop.classList.remove('open');dropBtn.setAttribute('aria-expanded','false')}});
}

/* ================= intro ================= */
var loader=$('#loader');
function ready(){document.body.classList.add('ready')}
function playIntro(){
  if(!loader){ready();return}
  if(reduce||(CFG.introOncePerSession&&store('n8-intro'))){loader.hidden=true;ready();return}
  store('n8-intro','1');
  var scv=$('#sparks'),sctx=scv.getContext('2d'),sparks=[],run=false,last=0;
  function size(){var d=Math.min(devicePixelRatio||1,2);scv.width=innerWidth*d;scv.height=innerHeight*d;sctx.setTransform(d,0,0,d,0,0)}
  function burst(){var r=$('#lb').getBoundingClientRect();
    [[-1,.3],[1,.7]].forEach(function(s){var ox=r.left+r.width*s[1],oy=r.top+r.height*.4;
      for(var i=0;i<14;i++){var sp=3+Math.random()*6,a=-.9+Math.random()*1.1;
        sparks.push({x:ox,y:oy,vx:s[0]*Math.cos(a)*sp,vy:Math.sin(a)*sp-1.5,life:0,max:520+Math.random()*420,w:1+Math.random()*1.4})}});
    if(!run){run=true;requestAnimationFrame(loop)}}
  function loop(t){var dt=last?Math.min(32,t-last):16;last=t;
    sctx.clearRect(0,0,innerWidth,innerHeight);sctx.globalCompositeOperation='lighter';
    for(var i=sparks.length-1;i>=0;i--){var p=sparks[i];p.life+=dt;if(p.life>p.max){sparks.splice(i,1);continue}
      var k=dt/16;p.vy+=.16*k;p.vx*=.985;var px=p.x,py=p.y;p.x+=p.vx*k;p.y+=p.vy*k;var a=1-p.life/p.max;
      sctx.strokeStyle='rgba(255,'+Math.round(190+50*a)+',120,'+a+')';sctx.lineWidth=p.w;sctx.beginPath();sctx.moveTo(px-p.vx*1.6,py-p.vy*1.6);sctx.lineTo(p.x,p.y);sctx.stroke();
      sctx.fillStyle='rgba(255,240,200,'+a+')';sctx.beginPath();sctx.arc(p.x,p.y,p.w*.9,0,6.283);sctx.fill()}
    if(sparks.length)requestAnimationFrame(loop);else run=false}
  doc.classList.add('locked');if(lenis)lenis.stop();
  size();loader.classList.add('play');
  setTimeout(burst,720);setTimeout(burst,1000);
  setTimeout(function(){loader.classList.add('out');ready();doc.classList.remove('locked');if(lenis)lenis.start()},1500);
  setTimeout(function(){loader.hidden=true},2100);
}
playIntro();

/* ================= light rain (falling gold filaments) ================= */
function Rain(cv){
  var ctx=cv.getContext('2d'),W=0,H=0,d=1,drops=[],on=false,raf=0,last=0;
  var dens=+(cv.dataset.density||1)*(innerWidth<700?.55:1);
  function size(){d=Math.min(devicePixelRatio||1,1.5);W=cv.clientWidth;H=cv.clientHeight;cv.width=W*d;cv.height=H*d;ctx.setTransform(d,0,0,d,0,0);
    var n=Math.round(W/38*dens);drops=[];for(var i=0;i<n;i++)drops.push(mk(true))}
  function mk(init){return {x:Math.random()*W,y:init?Math.random()*H:-Math.random()*H*.5,l:30+Math.random()*150,v:.35+Math.random()*1.4,w:Math.random()<.15?1.6:.8,a:.15+Math.random()*.55,c:Math.random()<.12}}
  function step(t){var dt=last?Math.min(40,t-last):16;last=t;ctx.clearRect(0,0,W,H);
    for(var i=0;i<drops.length;i++){var p=drops[i];p.y+=p.v*dt*.06;if(p.y-p.l>H){drops[i]=mk(false);continue}
      var g=ctx.createLinearGradient(0,p.y-p.l,0,p.y);g.addColorStop(0,'rgba(229,180,84,0)');g.addColorStop(1,'rgba(255,214,140,'+p.a+')');
      ctx.strokeStyle=g;ctx.lineWidth=p.w;ctx.beginPath();ctx.moveTo(p.x,p.y-p.l);ctx.lineTo(p.x,p.y);ctx.stroke();
      if(p.c){ctx.fillStyle='rgba(255,236,190,'+p.a+')';ctx.beginPath();ctx.arc(p.x,p.y,1.6,0,6.283);ctx.fill()}}
    if(on)raf=requestAnimationFrame(step)}
  size();addEventListener('resize',size);
  if(reduce){on=false;step(0);return}
  new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!on){on=true;last=0;raf=requestAnimationFrame(step)}else if(!e.isIntersecting){on=false;cancelAnimationFrame(raf)}})}).observe(cv);
}
$$('canvas.rain').forEach(Rain);

/* ================= hover: spotlight cards, spotlight sections, magnetic buttons ================= */
if(fine){
  $$('.hc').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();c.style.setProperty('--x',(e.clientX-r.left)+'px');c.style.setProperty('--y',(e.clientY-r.top)+'px')})});
  $$('.spotsec').forEach(function(s){var bg=$('.spotbg',s);s.addEventListener('pointermove',function(e){var r=s.getBoundingClientRect();bg.style.setProperty('--mx',(e.clientX-r.left)+'px');bg.style.setProperty('--my',(e.clientY-r.top)+'px')})});
  if(!reduce)$$('.btn').forEach(function(b){
    b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.translate=((e.clientX-r.left-r.width/2)*.12).toFixed(1)+'px '+((e.clientY-r.top-r.height/2)*.2).toFixed(1)+'px'});
    b.addEventListener('pointerleave',function(){b.style.translate=''})});
}else{
  /* touch: slowly drift the spotlight so the effect still shows */
  $$('.spotsec').forEach(function(s){var bg=$('.spotbg',s);if(reduce)return;var t0=performance.now();
    (function drift(t){var k=(t-t0)/4000;bg.style.setProperty('--mx',(50+35*Math.sin(k))+'%');bg.style.setProperty('--my',(40+25*Math.cos(k*1.3))+'%');requestAnimationFrame(drift)})(t0)});
}

/* ================= reveals ================= */
$$('.wordrv').forEach(function(h){
  var walk=function(node){Array.prototype.slice.call(node.childNodes).forEach(function(n){
    if(n.nodeType===3){var parts=n.textContent.split(/(\s+)/);var frag=document.createDocumentFragment();
      parts.forEach(function(p){if(!p)return;if(/^\s+$/.test(p)){frag.appendChild(document.createTextNode(p));return}
        var w=document.createElement('span');w.className='w';var i=document.createElement('span');i.textContent=p;w.appendChild(i);frag.appendChild(w)});
      n.parentNode.replaceChild(frag,n)}
    else if(n.nodeType===1&&n.tagName!=='BR')walk(n)})};
  walk(h);$$('.w>span',h).forEach(function(s,i){s.style.transitionDelay=(i*.05)+'s'});
});
if(reduce){$$('[data-rv],.wordrv').forEach(function(el){el.classList.add('in')})}
else{var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
  $$('[data-rv],.wordrv').forEach(function(el){io.observe(el)})}

/* ================= scroll scenes ================= */
function rawProg(sec){var r=sec.getBoundingClientRect(),span=r.height-innerHeight;if(span<=0)return r.top<0?1:0;return clamp(-r.top/span)}
function visible(el){var r=el.getBoundingClientRect();return r.bottom>-80&&r.top<innerHeight+80}
function Sm(){return {p:0}}
function step(s,t){if(reduce){s.p=1;return 1}s.p+=(t-s.p)*.12;if(Math.abs(s.p-t)<.0004)s.p=t;return s.p}
function strikes(sec,p){$$('.sl i',sec).forEach(function(l,i){l.style.transform='scaleX('+ease(clamp((p-.04-i*.11)/.13))+')'});var r=$('.res',sec);if(r)r.classList.toggle('on',p>.38)}
var scenes=[];

/* --- home hero: bulb, rays, orbiting services, chapters --- */
var hero=$('#hero');
if(hero){(function(){
  var hst=$('#hstage'),cv=$('#heroCv'),ctx=cv.getContext('2d'),hb=$('#hbulb'),tiles=$$('.tile',hst),stps=$$('.stp',hero),chaps=$$('.chap',hero),last=-1,pulseT=-1e9,CW=0,CH=0,dpr=1,SW=0,angs=null;
  var dust=[];for(var k=0;k<60;k++)dust.push({x:Math.random(),y:Math.random(),r:Math.random()*1.5+.3,v:Math.random()*.00022+.00005,ph:Math.random()*6.28});
  function size(){dpr=Math.min(devicePixelRatio||1,2);CW=cv.clientWidth;CH=cv.clientHeight;cv.width=Math.round(CW*dpr);cv.height=Math.round(CH*dpr);SW=hst.clientWidth}
  size();addEventListener('resize',size);
  function chapterOf(p){return p<.16?0:1+Math.min(3,Math.floor((p-.16)/.21))}
  function draw(p,t){
    ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,CW,CH);
    var ch=chapterOf(p);
    if(ch!==last){last=ch;pulseT=t;chaps.forEach(function(c,i){c.classList.toggle('on',i===ch)});
      stps.forEach(function(s,i){s.classList.toggle('on',i===ch);s.classList.toggle('done',i<ch)})}
    var blaze=clamp(p/.14),pulse=Math.exp(-(t-pulseT)/450)*(ch>0?1:0),breathe=reduce?1:.93+.07*Math.sin(t*.002),G=breathe*(.7+.3*blaze);
    var sc=lerp(1,.9,ease(clamp((p-.12)/.12)));hb.style.transform='scale('+sc.toFixed(4)+')';
    var cx=CW/2,cy=CH/2,S=SW*.76*sc;
    ctx.save();ctx.translate(cx,cy);ctx.rotate(t*.00006);var n=16,R=S*(.7+.12*blaze+.1*pulse);
    for(var r=0;r<n;r++){ctx.rotate(6.283/n);var gr=ctx.createLinearGradient(0,0,R,0);gr.addColorStop(0,'rgba(229,180,84,'+(.06*G+.06*pulse)+')');gr.addColorStop(1,'rgba(229,180,84,0)');ctx.fillStyle=gr;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(R,-R*.04);ctx.lineTo(R,R*.04);ctx.closePath();ctx.fill()}
    ctx.restore();
    var bl=ctx.createRadialGradient(cx,cy,0,cx,cy,S*(.62+.1*pulse));bl.addColorStop(0,'rgba(229,180,84,'+(.24*G+.1*pulse)+')');bl.addColorStop(1,'rgba(229,180,84,0)');ctx.fillStyle=bl;ctx.fillRect(0,0,CW,CH);
    for(var i=0;i<dust.length;i++){var d=dust[i];var y=(d.y-t*d.v)%1;if(y<0)y+=1;var x=d.x+Math.sin(t*.0004+d.ph)*.01;var px=x*CW,py=y*CH,dist=Math.hypot(px-cx,py-cy)/(CW*.55);
      ctx.fillStyle='rgba(240,205,140,'+clamp(.5*G*(1-dist),0,.8)+')';ctx.beginPath();ctx.arc(px,py,d.r,0,6.283);ctx.fill()}
    /* orbit: tiles travel an ellipse around the bulb; the active service swings to the front */
    var rx=SW*.47,ry=SW*.176,oc=SW/2;
    if(!angs)angs=tiles.map(function(_,j){return j*1.5708})
    for(var j=0;j<tiles.length;j++){
      var act=ch===j+1;
      var target=ch>0?1.5708+(j-(ch-1))*1.5708+(reduce?0:Math.sin(t*.0008)*.06):(reduce?0:t*.00016)+j*1.5708+p*1.6;
      var diff=Math.atan2(Math.sin(target-angs[j]),Math.cos(target-angs[j]));
      angs[j]+=reduce?diff:diff*.07;var base=angs[j];
      var tx=oc+Math.cos(base)*rx,ty=oc+Math.sin(base)*ry,depth=(Math.sin(base)+1)/2;
      var el=tiles[j],hw=el.offsetWidth/2,hh=el.offsetHeight/2;
      tx=clamp(tx,hw,SW-hw);
      var s=lerp(.82,1.06,depth)*(act?1.08:1);
      el.style.transform='translate('+(tx-hw).toFixed(1)+'px,'+(ty-hh).toFixed(1)+'px) scale('+s.toFixed(3)+')';
      el.style.zIndex=depth>.5?4:1;el.style.opacity=(depth>.5?1:.55).toFixed(2);
      el.classList.toggle('act',act);el.classList.toggle('dim',ch>0&&!act);
    }
  }
  scenes.push({el:hero,s:Sm(),draw:draw,hero:true});
})()}

/* --- home problem: leak report --- */
var prob=$('#problem');
if(prob){var leaks=$$('.leak',prob),sumbar=$('.sumbar',prob);
  scenes.push({el:prob,s:Sm(),draw:function(p){strikes(prob,p);leaks.forEach(function(l){l.classList.toggle('on',p>+l.dataset.at)});sumbar.classList.toggle('on',p>.68)}})}

/* --- GAS-EO four-mode results card (scroll on home, auto-loop on service page) --- */
function Gas(root){
  var gws=$$('.gw,.gtab',root),gps=$$('.gp',root),gdefs=$$('.gdef span',root),eng=$('.eng',root),m=-1;
  var ENG=['GOOGLE · SEARCH','GOOGLE · FEATURED SNIPPET','CHATGPT · PERPLEXITY','GOOGLE · AI OVERVIEW'];
  return function(k){if(k===m)return;m=k;
    gws.forEach(function(w,i){w.classList.toggle('act',i===k);w.classList.toggle('done',i<k);if(w.tagName==='BUTTON')w.setAttribute('aria-pressed',String(i===k))});
    gps.forEach(function(g,i){g.classList.toggle('on',i===k)});gdefs.forEach(function(g,i){g.classList.toggle('on',i===k)});if(eng)eng.textContent=ENG[k]}
}
var gshow=$('#gaseo-show');
if(gshow){var gset=Gas(gshow);scenes.push({el:gshow,s:Sm(),draw:function(p){gset(Math.min(3,Math.floor(clamp(p/.94)*4)))}})}

/* --- journey wave --- */
var jour=$('#journey');
if(jour){(function(){
  var wpath=$('#wpath'),wave=$('#wave'),jdot=$('#jdot'),jtb=$('#jtb'),jts=$('#jts'),jns=$$('.jn',jour),jits=$$('.jv .it',jour),jfill=$('#jfill');
  var JT=JSON.parse(jour.dataset.steps||'[]');
  scenes.push({el:jour,s:Sm(),draw:function(p){var q=ease(clamp((p-.04)/.86));
    if(wave.offsetParent!==null){wpath.style.strokeDashoffset=(1-q).toFixed(4);
      var L=wpath.getTotalLength(),pt=wpath.getPointAtLength(q*L),sw=wave.clientWidth/1200,sh=wave.clientHeight/400;
      jdot.style.transform='translate('+(pt.x*sw).toFixed(1)+'px,'+(pt.y*sh).toFixed(1)+'px)'}
    var idx=Math.min(JT.length-1,Math.floor(q*4+.08));if(JT[idx]){jtb.textContent=JT[idx][0];jts.textContent=JT[idx][1]}
    jns.forEach(function(n){n.classList.toggle('on',q>=+n.dataset.t-.04)});jits.forEach(function(n){n.classList.toggle('on',q>=+n.dataset.t-.04)});
    jfill.style.height=(q*100)+'%'}})
})()}

/* ================= auto-loop demos (service page heroes) ================= */
function Loop(el,steps,ms,fn){var i=-1,timer=0,on=false;
  function tick(){i=(i+1)%steps;fn(i)}
  if(reduce){fn(steps-1);return}
  fn(0);i=0;
  new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!on){on=true;timer=setInterval(tick,ms)}else if(!e.isIntersecting&&on){on=false;clearInterval(timer)}})}).observe(el);
  el.addEventListener('pointerenter',function(){if(on){clearInterval(timer);on=false}});
  el.addEventListener('pointerleave',function(){if(!on){on=true;timer=setInterval(tick,ms)}});
  return function(k){i=k;fn(k)};
}
$$('[data-loop]').forEach(function(el){
  var kind=el.dataset.loop;
  if(kind==='gas'){var set=Gas(el);var jump=Loop(el,4,3400,set);$$('button.gw,button.gtab',el).forEach(function(b,i){b.addEventListener('click',function(){if(jump)jump(i);else set(i)})})}
  if(kind==='ads'){var sc=$$('.adscr',el),n=$('.adsN',el),bars=$$('.bars i',el),BH=[.3,.42,.38,.55,.62,.78,.92];
    Loop(el,3,2600,function(k){sc.forEach(function(s,i){s.classList.toggle('on',i===k);s.classList.toggle('out',i<k)});
      bars.forEach(function(b,i){b.style.transform='scaleY('+(k===2?BH[i]:.08)+')'});if(n)n.textContent=k===2?'24':'0'})}
  if(kind==='crm'){var ms=$$('.msg',el);Loop(el,ms.length+3,1100,function(k){ms.forEach(function(m,i){m.classList.toggle('on',i<=k)})})}
  if(kind==='web'){var wb=$$('.wb',el),fg=$('.ring .fg',el),sc2=$('.ring span',el),q=$('.mini.q',el);
    Loop(el,wb.length+4,650,function(k){wb.forEach(function(b,i){b.classList.toggle('on',i<=k)});var r=clamp((k-wb.length+2)/2);
      if(fg)fg.style.strokeDashoffset=(1-.92*r).toFixed(3);if(sc2)sc2.textContent=r>=1?'90+':String(Math.round(90*r));if(q)q.classList.toggle('on',k>=wb.length+2)})}
  if(kind==='flow'){var fl=$$('.fl',el);Loop(el,fl.length,1300,function(k){fl.forEach(function(f,i){f.classList.toggle('on',i<=k)})})}
});

/* ================= contact form ================= */
var form=$('#contactForm');
if(form){var msg=$('.formmsg',form);
  form.addEventListener('submit',function(e){e.preventDefault();
    if(!form.checkValidity()){form.reportValidity();return}
    var data={};new FormData(form).forEach(function(v,k){data[k]=v});data.page=location.href;data.submitted_at=new Date().toISOString();
    var btn=$('button[type=submit]',form);btn.disabled=true;msg.className='formmsg';msg.textContent='Sending…';
    if(!CFG.formEndpoint){msg.className='formmsg err';msg.textContent='The form isn’t connected yet. Please email '+CFG.email+' and we’ll reply within one business day.';btn.disabled=false;return}
    fetch(CFG.formEndpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){if(!r.ok)throw new Error(r.status);msg.className='formmsg ok';msg.textContent='Thanks, we’ve got it. Nov8rs (Innovators) will reply within one business day.';form.reset();window.dataLayer.push({event:'contact_submit'})})
      .catch(function(){msg.className='formmsg err';msg.textContent='That didn’t send. Please try again or email '+CFG.email+'.'})
      .then(function(){btn.disabled=false});
  });
}

/* ================= main loop ================= */
var progEl=$('.prog'),mbar=$('.mbar'),hasHero=!!hero;
function frame(t){
  if(lenis)lenis.raf(t);
  for(var i=0;i<scenes.length;i++){var sc=scenes[i];if(visible(sc.el))sc.draw(sc.hero&&reduce?0:step(sc.s,rawProg(sc.el)),t)}
  var y=scrollY,max=doc.scrollHeight-innerHeight;
  if(progEl)progEl.style.transform='scaleX('+(max>0?clamp(y/max):0)+')';
  if(nav){nav.classList.toggle('solid',y>30);nav.classList.toggle('hide',y>lastY+4&&y>innerHeight*1.2&&!doc.classList.contains('menu-open'));if(y<lastY-4)nav.classList.remove('hide')}
  lastY=y;
  if(mbar)mbar.classList.toggle('on',y>innerHeight*.7);
  if(!reduce)requestAnimationFrame(frame);
}
if(reduce){scenes.forEach(function(sc){sc.draw(sc.hero?0:1,0)});addEventListener('scroll',function(){frame(0)},{passive:true});frame(0)}
else requestAnimationFrame(frame);
})();
