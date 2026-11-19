(function(){
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  // indholdsfortegnelse: marker den sektion, man er i
  var links=Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var secs=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1));});
  function spy(){
    var y=window.innerHeight*.3,cur=0;
    secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<y){cur=i;}});
    links.forEach(function(a,i){a.classList.toggle('on',i===cur);});
  }
  // mobil-bjælke vises, når faktaboksen er scrollet ud af syne
  var bar=document.getElementById('mbar'),fact=document.querySelector('.fact');
  function mb(){if(bar&&fact){bar.classList.toggle('on',fact.getBoundingClientRect().bottom<0);}}
  // indtoning ved scroll
  var vh=function(){return window.innerHeight;};
  var groups=[['.blk>h2',''],['.blk>.lede',''],['.fit>div',''],['.rate',''],['.steps li','s'],['.ftbl',''],['.plan',''],['.note',''],['.urates>div',''],['.fcard',''],['.stats>div',''],['.appgrid>*',''],['.sc',''],['.diary li','l'],['.pull','s'],['.proscons>div',''],['.seo h3',''],['.bgfacts',''],['.alt',''],['.blk .qa details',''],['.concl','s'],['.om','']];
  var wait=[];
  if(!reduce){
    document.documentElement.classList.add('js');
    groups.forEach(function(g){document.querySelectorAll(g[0]).forEach(function(el){if(el.getBoundingClientRect().top>vh()){if(g[1]){el.setAttribute('data-rv',g[1]);}el.classList.add('rv');wait.push(el);}});});
  }
  var rates=document.querySelector('.rates');
  function rv(){
    var h=vh(),n=0;
    wait=wait.filter(function(el){
      if(el.getBoundingClientRect().top<h*.94){
        var d=Math.min(n++,6)*80;
        setTimeout(function(){el.classList.add('in');setTimeout(function(){el.classList.remove('rv','in');el.removeAttribute('data-rv');},1000);},d);
        return false;
      }
      return true;
    });
    if(rates&&!rates.classList.contains('on')&&rates.getBoundingClientRect().top<h*.85){rates.classList.add('on');}
  }
  function all(){spy();mb();rv();}
  window.addEventListener('scroll',all,{passive:true});window.addEventListener('resize',all);all();
  if(reduce&&rates){rates.classList.add('on');}
})();
