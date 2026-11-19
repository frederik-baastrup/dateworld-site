import re
src=open('/home/claude/build/list.py',encoding='utf-8').read()
a=src.index('S=['); b=src.index('def lg(')
S_NEW='''S=[
 dict(n='Scor.dk',slug='scor',logo=None,lh=None,sub='Dansk side til flirt og uforpligtende møder.',chips=['Fræk dating','Danske profiler'],c='dk',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om Scor.dk: hvem er på siden, hvad du kan gratis, og hvad et medlemskab koster.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
 dict(n='Sexhunt.dk',slug='sexhunt',logo=None,lh=None,sub='Kontaktside for voksne, der søger noget frækt.',chips=['Sexdating','Danske profiler'],c='dk sex',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om Sexhunt.dk: målgruppe, funktioner og pris.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
 dict(n='Erox.dk',slug='erox',logo=None,lh=None,sub='Dansk kontaktside for par og singler.',chips=['Par og singler','Swingere'],c='dk par sex',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om Erox.dk: hvem siden er til, fx par og swingere, og hvad det koster.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
 dict(n='C-Date',slug='cdate',logo=None,lh=None,sub='International side til diskrete, uforpligtende møder.',chips=['Diskret','International'],c='int',price='[PRIS]',free='[JA/NEJ]',app='[JA/NEJ]',score='[x,x]',
  txt='[2–3 sætninger om C-Date: hvordan matchningen fungerer, diskretion og pris.]',pros=['[Fordel]','[Fordel]','[Fordel]'],cons=['[Ulempe]','[Ulempe]']),
]
'''
src=src[:a]+S_NEW+src[b:]
R=[
 ('Bedste datingsider 2026 – sammenlign pris og vilkår – Dateworld','Fræk dating 2026 – de bedste sider til uforpligtende møder – Dateworld'),
 ('<span aria-current="page">Bedste datingsider</span>','<a href="#">Datingsider</a><span>/</span><span aria-current="page">Fræk dating</span>'),
 ('<h1>Bedste datingsider i 2026</h1>','<h1>Fræk dating: de bedste sider i 2026</h1>'),
 ('Vi har sammenlignet pris, vilkår og funktioner hos de datingtjenester, vi samarbejder med. Her er vores bud på, hvor du skal starte, alt efter hvad du leder efter.','Søger du noget uforpligtende, er en almindelig datingside sjældent det rigtige sted. Her sammenligner vi de sider til fræk dating, vi samarbejder med, på pris, diskretion og hvem der er på dem.'),
 ('<span>6 datingsider sammenlignet</span>','<span>4 sider sammenlignet</span><span class="age18">Kun 18+</span>'),
 ("'34px')+'''</span><span><small>Bredest udvalg</small><b>Dating.dk</b>","'34px')+'''</span><span><small>[Bedst til …]</small><b>Scor.dk</b>"),
 ("'16px')+'''</span><span><small>Til dig over 50</small><b>Senior.dk</b>","'16px')+'''</span><span><small>[Bedst til …]</small><b>Erox.dk</b>"),
 ("'14px')+'''</span><span><small>Match på personlighed</small><b>Single.dk</b>","'14px')+'''</span><span><small>[Bedst til …]</small><b>C-Date</b>"),
 ('href="#s-dating"><span class="plg">','href="#s-scor"><span class="plg">'),('href="#s-senior"><span class="plg">','href="#s-erox"><span class="plg">'),('href="#s-single"><span class="plg">','href="#s-cdate"><span class="plg">'),
 ('<h2>Sammenlign datingsiderne</h2>','<h2>Sammenlign siderne til fræk dating</h2>'),
 ('''<button type="button" data-f="serios" aria-pressed="false">Seriøst forhold <small>%d</small></button><button type="button" data-f="50" aria-pressed="false">50+ <small>%d</small></button><button type="button" data-f="alle" aria-pressed="false">Alle aldre <small>%d</small></button>''','''<button type="button" data-f="dk" aria-pressed="false">Danske sider <small>%d</small></button><button type="button" data-f="par" aria-pressed="false">Par og swingere <small>%d</small></button><button type="button" data-f="int" aria-pressed="false">Internationale <small>%d</small></button>'''),
 ("%(len(S),cnt('serios'),cnt('50'),cnt('alle'),rows)","%(len(S),cnt('dk'),cnt('par'),cnt('int'),rows)"),
 ('<h2>Datingsiderne gennemgået</h2>','<h2>Siderne gennemgået</h2>'),
 ('<h2>Hvilken datingside passer til dig?</h2>','<h2>Hvad leder du efter?</h2>'),
]
for o,n in R:
    assert o in src,o[:60]; src=src.replace(o,n)
# chooser
a=src.index('ch=['); b=src.index('\n',a)
src=src[:a]+"""ch=[('flame','En hurtig flirt','Gå efter en dansk side med mange aktive profiler i dit område, fx Scor.dk.','#s-scor'),('heart','I er et par','Vælg en side, hvor par og swingere er velkomne, fx Erox.dk.','#s-erox'),('lock','Diskretion betyder mest','Vælg en side med skjulte billeder og diskret betaling, fx C-Date.','#s-cdate'),('star','Du søger en kæreste','Så er en almindelig datingside et bedre sted. Se de bedste datingsider.','#')]"""+src[b:]
src=src.replace("'flame':ic(","'lock':ic('<rect x=\"5\" y=\"10.5\" width=\"14\" height=\"10\" rx=\"2\"/><path d=\"M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5\"/>'),\n 'flame':ic(",1)
# method
src=src.replace("('feat','Funktioner','Søgning, beskeder, matchforslag, app og events.'),('shield','Sikkerhed','Godkendelse af profiler, anmeldelse af brugere og privatliv.')","('feat','Funktioner','Søgning, beskeder, chat, webcam og events.'),('shield','Diskretion','Skjulte billeder, diskret betaling på kontoudtog og falske profiler.')")
# faq
a=src.index('qs=['); b=src.index('\n',a)
src=src[:a]+"""qs=[('Hvad er fræk dating?','Fræk dating er sider til voksne, der søger noget uforpligtende, fx en flirt, et engangsmøde eller en fast legekammerat, frem for et fast forhold.'),('Er fræk dating gratis?','Det er som regel gratis at oprette en profil, men for at skrive med andre kræver de fleste sider et medlemskab. Se prisen ved hver side i sammenligningen ovenfor.'),('Står det på mit kontoudtog?','[Hvordan siderne vises på kontoudtoget, fx under et neutralt firmanavn. Tjekkes for hver side.]'),('Hvordan undgår jeg falske profiler?','Vær skeptisk over for profiler, der skriver først med lange beskeder, beder dig skifte til en anden app eller beder om penge. Brug sidens funktion til at anmelde mistænkelige profiler.'),('Hvordan dater jeg sikkert?','Del ikke adresse, arbejdsplads eller betalingsoplysninger i starten, mød første gang et offentligt sted, og sig til en ven, hvor du er. Aftal grænser på forhånd, og husk, at et ja altid kan trækkes tilbage.')]"""+src[b:]
src=src.replace('Det, de fleste spørger om, før de vælger en datingside.','Det, de fleste spørger om, før de prøver fræk dating.')
# seo + om
a=src.index("seo='''"); b=src.index("css=open")
src=src[:a]+r"""PRODS=[('Vibrator','Sinful'),('Massageolie','Sinful'),('Spil til par','Private Play'),('Lingeri','Private Play')]
pc=''.join('<a class="prod" href="#" rel="sponsored nofollow"><span class="pimg">[PRODUKTBILLEDE]</span><small>%s</small><b>[Produktnavn: %s]</b><span class="pp"><b>[PRIS]</b><i>Se produktet %s</i></span></a>'%(s,n.lower(),ARS) for n,s in PRODS)
shop='''<section class="lsec lgray" id="produkter">
  <div class="wrap">
    <div class="sec-head"><h2>Gør daten lidt frækkere</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="cmp-top"><p class="cmp-lede">Et lille udvalg fra de webshops, vi samarbejder med, til dig, der vil krydre aftenen.</p><a class="more" href="#">Se flere produkter</a></div>
    <div class="prods">'''+pc+'''</div>
    <p class="cmp-note">Reklamelinks. Priserne hentes fra butikkernes produktfeeds.</p>
  </div>
</section>'''
seo='''<section class="prose" id="mere">
  <div class="wrap">
    <h2>Fræk dating i Danmark: det skal du vide</h2>
    <div class="prose-cols">
      <div>
        <h3>Fræk dating, sexdating eller swingerklub?</h3>
        <p>Fræk dating dækker over alt fra en uskyldig flirt til et engangsmøde. Sider til <a href="#">sexdating</a> er mere direkte, og er I et par, der vil møde andre, er en side til <a href="#">swingere</a> eller en <a href="#">swingerklub</a> et bedre sted at starte.</p>
        <h3>Diskretion</h3>
        <p>Vælg en side, hvor du selv bestemmer, hvem der kan se dine billeder, og tjek, hvordan betalingen står på kontoudtoget. Brug gerne en mailadresse, du kun bruger til dating.</p>
      </div>
      <div>
        <h3>Pas på falske profiler</h3>
        <p>Falske profiler findes på de fleste sider til fræk dating. Typiske tegn er perfekte billeder, lange beskeder fra start og ønsker om at skifte til en anden app. Læs mere i vores guide til <a href="#">falske profiler</a>.</p>
        <h3>Respekt og samtykke</h3>
        <p>Vær tydelig om, hvad du søger, og respektér et nej. Aftal grænser, før I mødes, og brug altid beskyttelse.</p>
      </div>
    </div>
  </div>
</section>
<section class="lsec">
  <div class="wrap"><div class="lom"><h2>Om denne sammenligning</h2><p>Siderne er kun for voksne over 18. Vi sammenligner de tjenester, vi samarbejder med, ud fra deres hjemmesider, priser, vilkår og brugernes anmeldelser. Dateworld får betaling, hvis du opretter et medlemskab eller køber via vores links. Det påvirker ikke rækkefølgen eller det, vi skriver. <a href="#">Sådan arbejder vi</a></p></div></div>
</section>'''
"""+src[b:]
src=src.replace("css=open('/home/claude/build/review.css',encoding='utf-8').read()+open('/home/claude/build/list.css',encoding='utf-8').read()","css=open('/home/claude/build/review.css',encoding='utf-8').read()+open('/home/claude/build/list.css',encoding='utf-8').read()+open('/home/claude/build/fraek.css',encoding='utf-8').read()")
src=src.replace("hero+over+gen+choose+method+faq+seo","hero+over+gen+shop+choose+method+faq+seo")
src=src.replace("'/home/claude/dw-list/index.html'","'/home/claude/dw-fraek/index.html'")
src=src.replace("['.ch',''],","['.ch',''],['.prod',''],") if False else src
exec(compile(src,'fraek_gen','exec'))
