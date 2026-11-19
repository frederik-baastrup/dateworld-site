import re
src=open('/home/claude/dw-page/index.html',encoding='utf-8').read()
head=src[:src.index('</head>')]
head=head.replace(re.search(r'<title>.*?</title>',head).group(0),'<title>Bedste datingsider 2026 – sammenlign pris og vilkår – Dateworld</title>')
top=src[src.index('</head>'):src.index('<section class="hero">')]
foot=src[src.index('<footer'):src.index('</footer>')+9]
sc=re.findall(r'<script>(.*?)</script>',src,re.S)
filter_js,menu_js,faq_js=sc[0],sc[1],sc[3]

def ic(d,w=22,sw=1.5): return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%(w,w,sw,d)
ARW='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11h14M12.5 5.5 18 11l-5.5 5.5"/></svg>'
ARS=ARW.replace('width="20" height="20"','width="18" height="18"').replace('1.3','1.4')
CHK=ic('<circle cx="12" cy="12" r="9"/><path d="m8 12.3 2.6 2.6L16 9.4"/>',20)
MIN=ic('<circle cx="12" cy="12" r="9"/><path d="M8.5 12h7"/>',20)
PLUS='<svg aria-hidden="true" width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M11 4v14M4 11h14"/></svg>'
FI={'pris':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.6 2.5H13.5v4.9L7.4 13.5 2.5 8.6Z"/><circle cx="10.6" cy="5.4" r=".9"/></svg>','op':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="5.6"/><path d="m5.6 8.1 1.7 1.7 3.2-3.4"/></svg>','app':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="2" width="7" height="12" rx="1.6"/><path d="M7.3 11.6h1.4"/></svg>'}
I={
 'pris':ic('<path d="M12.5 3.5H20.5v8L11 21 3 13Z"/><circle cx="16.5" cy="7.5" r="1.3"/>'),
 'terms':ic('<path d="M6 3.5h9l3.5 3.5v13.5H6Z"/><path d="M9 11h6M9 14.5h6M9 18h3.5"/>'),
 'feat':ic('<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>'),
 'shield':ic('<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6Z"/><path d="m9 12 2.2 2.2L15.5 10"/>'),
 'star':ic('<path d="M12 3.5 14.6 9l5.9.7-4.4 4.1 1.2 5.8L12 16.6 6.7 19.6l1.2-5.8L3.5 9.7 9.4 9Z"/>'),
 'heart':ic('<path d="M12 20s-7-4.3-7-9.6A3.9 3.9 0 0 1 12 8a3.9 3.9 0 0 1 7 2.4C19 15.7 12 20 12 20Z"/>'),
 'fifty':'<b class="t">50+</b>',
 'brain':ic('<circle cx="12" cy="12" r="8.5"/><path d="M9 10h.01M15 10h.01M8.5 14.5c1 1.3 2.2 2 3.5 2s2.5-.7 3.5-2"/>'),
 'flame':ic('<path d="M12 21c-3.6 0-6.5-2.7-6.5-6.3 0-3.2 2.3-5.2 3.6-7.7.4 1.7 1.3 2.8 2.4 3.4C11.8 7 13 4.5 15 3c-.2 3 3.5 5.3 3.5 11.7 0 3.6-2.9 6.3-6.5 6.3Z"/>'),
}
S=[
 dict(n='Dating.dk',slug='dating',logo='logo-dating.webp',lh='54px',sub='Bred datingside for dig, der søger en kæreste.',chips=['Alle aldre','Hele landet'],c='alle serios',price='129 kr. / 4 uger',free='Ja',app='iOS og Android',score='3,8',
  txt='En af de ældste danske datingsider, online siden 1998. Det er gratis at oprette en profil, søge og like, mens en +PlusProfil giver adgang til at læse beskeder og se dine matches. Profiler og billeder godkendes manuelt, og kundeservice svarer alle ugens dage.',
  pros=['Mange danske profiler i alle aldre','Manuel godkendelse af profiler og billeder','App til både iPhone og Android'],cons=['Betaling kræves for at læse beskeder','Introtilbuddet har 84 dages binding']),
 dict(n='Single.dk',slug='single',logo='logo-single.svg',lh='22px',sub='Matcher dig på personlighed, humor og værdier.',chips=['Singler','Personlighedsmatch'],c='alle serios',price='[PRIS]',free='Ja',app='iOS og Android',score='[x,x]',
  txt='Single.dk matcher dig ud fra quizzer om personlighed, humor og værdier og viser, hvor godt I passer sammen i procent. Siden har været online siden 1999 og oplyser selv over 50.000 aktive singler.',
  pros=['Matchprocent ud fra personlighed og interesser','Appen har 4,0 i App Store fra over 2.500 bedømmelser','Gratis at oprette en profil'],cons=['Lav bedømmelse på Trustpilot (1,1 ud af 5)','[Pris og vilkår tjekkes i anmeldelsen]']),
 dict(n='Senior.dk',slug='senior',logo='logo-senior.webp',lh='26px',sub='Datingside og mødested for dig over 50.',chips=['50+','Kæreste eller ven'],c='50',price='125 kr. / md.',free='Ja',app='[JA/NEJ]',score='[x,x]',
  txt='Senior.dk er kun for singler over 50, uanset om du søger en kæreste eller en ven. Det er gratis at oprette sig, og et VIP-medlemskab giver adgang til at læse og skrive beskeder. VIP koster 125 kr. for en måned eller 250 kr. for tre måneder.',
  pros=['Kun for singler over 50','Gratis at oprette en profil','Lav månedspris ved 3 måneder'],cons=['VIP kræves for at læse og skrive beskeder','[Ét punkt mere fra anmeldelsen]']),
 dict(n='Singles50',slug='singles50',logo=None,lh=None,sub='Matchning for singler over 50.',chips=['50+','Seriøst forhold'],c='50 serios',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om Singles50: hvem siden er til, hvordan matchningen fungerer, og hvad et medlemskab koster.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
 dict(n='Academic Singles',slug='academic',logo=None,lh=None,sub='Dating for singler med uddannelse.',chips=['Elitedating','Seriøst forhold'],c='serios',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om Academic Singles: målgruppe, personlighedstest og pris.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
 dict(n='be2',slug='be2',logo=None,lh=None,sub='Matchning til dig, der søger et seriøst forhold.',chips=['Seriøst forhold','Personlighedstest'],c='serios',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om be2: hvordan personlighedstesten og matchforslagene fungerer, og hvad det koster.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
]
def lg(s,h=None):
    if s['logo']: return '<img src="img/%s" alt="" style="height:%s">'%(s['logo'],h or s['lh'])
    return '<b>%s</b>'%s['n']
def cf(k,lab,v): return '<div class="cfact"><small>%s%s</small><b>%s</b></div>'%(FI[k],lab,v)

hero='''<section class="rhero lhero">
  <div class="glow" aria-hidden="true"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Brødkrummer"><a href="#">Forside</a><span>/</span><span aria-current="page">Bedste datingsider</span></nav>
    <div class="rhero-grid">
      <div>
        <h1>Bedste datingsider i 2026</h1>
        <p class="verdict">Vi har sammenlignet pris, vilkår og funktioner hos de datingtjenester, vi samarbejder med. Her er vores bud på, hvor du skal starte, alt efter hvad du leder efter.</p>
        <p class="meta"><span>Opdateret 11. november 2026</span><span>Af Dateworld-redaktionen</span><span>6 datingsider sammenlignet</span></p>
      </div>
      <aside class="picks" aria-label="Vores bud">
        <p class="picks-h">Vores bud</p>
        <a href="#s-dating"><span class="plg">'''+lg(S[0],'34px')+'''</span><span><small>Bredest udvalg</small><b>Dating.dk</b></span>'''+ARS+'''</a>
        <a href="#s-senior"><span class="plg">'''+lg(S[2],'16px')+'''</span><span><small>Til dig over 50</small><b>Senior.dk</b></span>'''+ARS+'''</a>
        <a href="#s-single"><span class="plg">'''+lg(S[1],'14px')+'''</span><span><small>Match på personlighed</small><b>Single.dk</b></span>'''+ARS+'''</a>
        <p class="adl"><span>Reklame</span>Vi får betaling, hvis du opretter dig via vores links.</p>
      </aside>
    </div>
  </div>
</section>'''

rows=''
for i,s in enumerate(S):
    rows+='<article class="tr%s" data-c="%s">%s<span class="no">%d</span><span class="lg">%s</span><div class="nm"><h3>%s</h3><p>%s</p><div class="chips">%s</div></div><div class="cfacts">%s%s%s</div><div class="act"><a class="visit" href="#" rel="sponsored nofollow" aria-label="Besøg %s"><span>Besøg siden</span><i>%s</i></a><div class="under"><span>Reklamelink</span><a href="#s-%s">Se gennemgang</a></div></div></article>'%(' top' if i==0 else '',s['c'],'<span class="pick-tab">Vores anbefaling</span>' if i==0 else '',i+1,lg(s),s['n'],s['sub'],''.join('<span>%s</span>'%c for c in s['chips']),cf('pris','Pris fra',s['price']),cf('op','Gratis oprettelse',s['free']),cf('app','App',s['app']),s['n'],ARS,s['slug'])
cnt=lambda f:sum(1 for s in S if f in s['c'].split())
over='''<section class="cmp lsec" id="oversigt">
  <div class="wrap">
    <div class="sec-head"><h2>Sammenlign datingsiderne</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="cmp-top">
      <p class="cmp-lede">Rangeret ud fra vores samlede vurdering. Brug filtrene, hvis du leder efter noget bestemt.</p>
      <div class="filters" role="group" aria-label="Filtrér datingsider"><button type="button" data-f="" aria-pressed="true">Alle <small>%d</small></button><button type="button" data-f="serios" aria-pressed="false">Seriøst forhold <small>%d</small></button><button type="button" data-f="50" aria-pressed="false">50+ <small>%d</small></button><button type="button" data-f="alle" aria-pressed="false">Alle aldre <small>%d</small></button></div>
    </div>
    <div class="tbl" id="tbl">%s</div>
    <p class="cmp-note">Knapperne fører til tjenestens egen side. Priserne er tjenestens egne, senest tjekket november 2026.</p>
  </div>
</section>'''%(len(S),cnt('serios'),cnt('50'),cnt('alle'),rows)

cards=''
for i,s in enumerate(S):
    cards+='''<article class="lcard" id="s-%s">
      <div class="lc-head"><span class="lc-no">%d</span><span class="lc-lg">%s</span><div class="lc-t"><h3>%s</h3><div class="chips">%s</div></div><div class="lc-score"><b>%s</b><span>ud af 5</span></div></div>
      <p class="lc-txt">%s</p>
      <div class="lc-pc"><div><h4>%sFordele</h4><ul>%s</ul></div><div><h4>%sUlemper</h4><ul>%s</ul></div></div>
      <div class="lc-foot"><dl><div><dt>Pris fra</dt><dd>%s</dd></div><div><dt>Gratis oprettelse</dt><dd>%s</dd></div><div><dt>App</dt><dd>%s</dd></div></dl>
        <div class="lc-act"><a class="read" href="#">Læs anmeldelsen</a><a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a></div></div>
    </article>'''%(s['slug'],i+1,lg(s),s['n'],''.join('<span>%s</span>'%c for c in s['chips']),s['score'],s['txt'],CHK,''.join('<li>%s</li>'%p for p in s['pros']),MIN,''.join('<li>%s</li>'%p for p in s['cons']),s['price'],s['free'],s['app'],s['n'],ARS)
gen='''<section class="lsec lgray" id="gennemgang">
  <div class="wrap">
    <div class="sec-head"><h2>Datingsiderne gennemgået</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="lcards">'''+cards+'''</div>
  </div>
</section>'''

ch=[('heart','Du vil finde en kæreste','Start på en bred datingside med mange profiler i alle aldre, fx Dating.dk.','#s-dating'),('fifty','Du er over 50','Vælg en side, hvor alle er samme sted i livet, fx Senior.dk eller Singles50.','#s-senior'),('brain','Personlighed betyder mest','Gå efter matchning på personlighed og værdier, fx Single.dk eller be2.','#s-single'),('flame','Du vil have noget uforpligtende','Så er en almindelig datingside ikke det rigtige sted. Se vores side om fræk dating.','#')]
choose='''<section class="lsec" id="vaelg">
  <div class="wrap">
    <div class="sec-head"><h2>Hvilken datingside passer til dig?</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="choose">'''+''.join('<a class="ch" href="%s"><span class="fi">%s</span><h3>%s</h3><p>%s</p><span class="go">Se forslag %s</span></a>'%(h,I[k],t,d,ARS) for k,t,d,h in ch)+'''</div>
  </div>
</section>'''

crit=[('pris','Pris','Hvad koster et medlemskab pr. måned og i alt, og hvad kan du gratis?'),('terms','Vilkår','Binding, automatisk fornyelse og hvor let det er at melde fra.'),('feat','Funktioner','Søgning, beskeder, matchforslag, app og events.'),('shield','Sikkerhed','Godkendelse af profiler, anmeldelse af brugere og privatliv.'),('star','Brugernes bedømmelse','Samlet bedømmelse på Trustpilot og i app-butikkerne.')]
method='''<section class="lsec ldark" id="metode">
  <div class="wrap lmeth">
    <div><h2>Sådan har vi sammenlignet</h2><p>Vi gennemgår hver tjenestes hjemmeside, priser, vilkår og brugernes anmeldelser og vurderer dem ud fra de samme fem områder. Rækkefølgen følger vores samlede vurdering.</p><a class="more" href="#">Sådan arbejder vi</a></div>
    <ol class="crit">'''+''.join('<li><span class="fi">%s</span><div><h3>%s</h3><p>%s</p></div></li>'%(I[k],t,d) for k,t,d in crit)+'''</ol>
  </div>
</section>'''

qs=[('Hvad er den bedste datingside i Danmark?','Det afhænger af, hvad du leder efter. Søger du en kæreste og vil have mange profiler at vælge imellem, er en bred side som Dating.dk et godt sted at starte. Er du over 50, eller betyder personlighed mest, passer en mere specialiseret side ofte bedre.'),('Hvilke datingsider er gratis?','De fleste datingsider lader dig oprette en profil gratis, også dem i vores sammenligning, vi har gennemgået. Vil du læse og skrive beskeder frit, kræver det som regel et medlemskab.'),('Hvad koster en datingside?','Det afhænger af tjenesten og af, hvor lang en periode du vælger. Hos Dating.dk koster et abonnement 129 kr. pr. 4 uger, og hos Senior.dk koster en måned 125 kr. Se prisen ved hver tjeneste i sammenligningen ovenfor.'),('Hvilken datingside er bedst for 50+?','Senior.dk er kun for singler over 50 og koster 125 kr. for en måned. Singles50 er et alternativ, hvis du søger et seriøst forhold.'),('Er det sikkert at date på nettet?','Ja, når du bruger sund fornuft: del ikke adresse eller betalingsoplysninger, mød første gang et offentligt sted, og anmeld profiler, der virker mistænkelige.')]
faq='''<section class="lsec" id="faq">
  <div class="wrap faq-grid">
    <div><h2 class="lh2">Spørgsmål og svar</h2><p class="lede">Det, de fleste spørger om, før de vælger en datingside.</p></div>
    <div class="qa">'''+''.join('<details%s><summary><span>%s</span>%s</summary><p>%s</p></details>'%(' open' if i==0 else '',q,PLUS,a) for i,(q,a) in enumerate(qs))+'''</div>
  </div>
</section>'''

seo='''<section class="prose" id="mere">
  <div class="wrap">
    <h2>Datingsider i Danmark: sådan finder du den rigtige</h2>
    <div class="prose-cols">
      <div>
        <h3>Datingside eller dating app?</h3>
        <p>En datingside giver plads til længere profiler og søgning på alder, område og interesser, mens en dating app som regel bygger på billeder og hurtige swipes. De fleste danske datingsider har i dag også en app, så du kan bruge den samme profil på mobilen. Se vores oversigt over <a href="#">bedste dating apps</a>.</p>
        <h3>Gratis eller betalt?</h3>
        <p>Det er gratis at oprette en profil på de fleste datingsider. Forskellen ligger i, hvad du kan uden at betale: nogle steder kan du se og like profiler, men ikke læse beskeder. Læs mere om <a href="#">gratis dating</a>, og tjek altid, om medlemskabet fornyes automatisk.</p>
      </div>
      <div>
        <h3>Vælg efter alder og livsstil</h3>
        <p>Det er lettere at finde et match, når de andre medlemmer er samme sted i livet som dig. Derfor findes der sider til <a href="#">dating for unge</a>, <a href="#">dating 40+</a> og <a href="#">dating 50+</a>, og nichesider til fx <a href="#">kristen dating</a> og <a href="#">LGBT+ dating</a>.</p>
        <h3>Få mest ud af din profil</h3>
        <p>Et par vellignende billeder og en profiltekst, der siger noget konkret om dig, giver flere svar end en lang liste af egenskaber. Få hjælp i vores guides til <a href="#">profiltekst</a> og <a href="#">den første besked</a>.</p>
      </div>
    </div>
  </div>
</section>
<section class="lsec">
  <div class="wrap"><div class="lom"><h2>Om denne sammenligning</h2><p>Vi sammenligner de datingtjenester, vi samarbejder med, ud fra deres hjemmesider, priser, vilkår og brugernes anmeldelser. Dateworld får betaling, hvis du opretter et medlemskab via vores links. Det påvirker ikke rækkefølgen eller det, vi skriver. <a href="#">Sådan arbejder vi</a></p></div></div>
</section>'''

css=open('/home/claude/build/review.css',encoding='utf-8').read()+open('/home/claude/build/list.css',encoding='utf-8').read()
js=open('/home/claude/build/list.js',encoding='utf-8').read()
out=head+'<style>'+css+'</style>\n'+top+'<main>'+hero+over+gen+choose+method+faq+seo+'</main>\n'+foot+'\n<script>'+filter_js+'</script>\n<script>'+menu_js+'</script>\n<script>'+faq_js+'</script>\n<script>'+js+'</script>\n</body>\n</html>\n'
open('/home/claude/dw-list/index.html','w',encoding='utf-8').write(out)
print(len(out))
