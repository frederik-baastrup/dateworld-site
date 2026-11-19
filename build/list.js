(function(){
  if(matchMedia('(prefers-reduced-motion:reduce)').matches){return;}
  var groups=[['.sec-head',''],['.cmp-top',''],['.tbl .tr',''],['.lcard','s'],['.ch',''],['.lmeth>div','l'],['.crit li','r'],['.faq-grid>div:first-child','l'],['.qa details',''],['.prose h2',''],['.prose-cols>div',''],['.lom',''],['.foot-top','']];
  var h=window.innerHeight,wait=[];
  document.documentElement.classList.add('js');
  groups.forEach(function(g){document.querySelectorAll(g[0]).forEach(function(el){if(el.getBoundingClientRect().top>h){if(g[1]){el.setAttribute('data-rv',g[1]);}el.classList.add('rv');wait.push(el);}});});
  function rv(){var hh=window.innerHeight,n=0;wait=wait.filter(function(el){if(el.getBoundingClientRect().top<hh*.94){var d=Math.min(n++,6)*80;setTimeout(function(){el.classList.add('in');setTimeout(function(){el.classList.remove('rv','in');el.removeAttribute('data-rv');},1000);},d);return false;}return true;});}
  window.addEventListener('scroll',rv,{passive:true});window.addEventListener('resize',rv);rv();
})();
