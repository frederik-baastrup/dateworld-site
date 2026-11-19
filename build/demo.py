import re
src=open('/home/claude/dw-page/index.html',encoding='utf-8').read()
head=src[:src.index('</head>')]
title_old=re.search(r'<title>.*?</title>',head).group(0)
head=head.replace(title_old,'<title>Dating.dk anmeldelse 2026 – Dateworld</title>')
body_start=src.index('</head>')
top=src[body_start:src.index('<section class="hero">')]
foot=src[src.index('<footer'):src.index('</footer>')+9]
scripts=re.findall(r'<script>(.*?)</script>',src,re.S)
menu_js=scripts[1]; faq_js=scripts[3]

def ic(d,w=22,sw=1.5): return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%(w,w,sw,d)
ARW='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11h14M12.5 5.5 18 11l-5.5 5.5"/></svg>'
CHK=ic('<circle cx="12" cy="12" r="9"/><path d="m8 12.3 2.6 2.6L16 9.4"/>',20)
MIN=ic('<circle cx="12" cy="12" r="9"/><path d="M8.5 12h7"/>',20)
YES=ic('<path d="m6 12.5 4 4L18 8"/>',18,2)
NO=ic('<path d="M7 7l10 10M17 7 7 17"/>',18,2)
PLUS='<svg aria-hidden="true" width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M11 4v14M4 11h14"/></svg>'
I={
 'search':ic('<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.4-4.4"/>'),
 'chat':ic('<path d="M4 5.5h16v11H10l-4 3.5v-3.5H4Z"/><path d="M8 9.5h8M8 12.5h5"/>'),
 'match':ic('<path d="M12 20s-7-4.3-7-9.6A3.9 3.9 0 0 1 12 8a3.9 3.9 0 0 1 7 2.4C19 15.7 12 20 12 20Z"/>'),
 'eye':ic('<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="2.8"/>'),
 'phone':ic('<rect x="7" y="3" width="10" height="18" rx="2.2"/><path d="M11 17.5h2"/>'),
 'star':ic('<path d="M12 3.5 14.6 9l5.9.7-4.4 4.1 1.2 5.8L12 16.6 6.7 19.6l1.2-5.8L3.5 9.7 9.4 9Z"/>'),
 'shield':ic('<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6Z"/><path d="m9 12 2.2 2.2L15.5 10"/>'),
 'block':ic('<circle cx="12" cy="12" r="8.5"/><path d="m6 6 12 12"/>'),
 'flag':ic('<path d="M5 21V4M5 4h12l-2.5 4L17 12H5"/>'),
 'lock':ic('<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/>'),
 'trash':ic('<path d="M4.5 7h15M9.5 7V4.5h5V7M6.5 7l1 13h9l1-13"/>'),
 'clock':ic('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'),
 'info':ic('<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8h.01"/>'),
 'users':ic('<circle cx="9" cy="8.5" r="3"/><path d="M3.5 19c.6-3 2.8-4.8 5.5-4.8s4.9 1.8 5.5 4.8"/><circle cx="16.5" cy="9.5" r="2.4"/><path d="M15.8 14.3c2.3.2 4.1 1.8 4.7 4.2"/>'),
 'cake':ic('<path d="M4 20h16M5 20v-7h14v7M5 16c1.5 1 3 1 4.5 0s3 1 4.5 0 3-1 4.5 0"/><path d="M12 13V9M12 6.5v.01"/>'),
 'pin':ic('<path d="M12 21s6.5-6 6.5-11A6.5 6.5 0 0 0 5.5 10c0 5 6.5 11 6.5 11Z"/><circle cx="12" cy="10" r="2.4"/>'),
}
def shot(label,ratio='16/10'): return '<figure class="shot" style="aspect-ratio:%s"><span>%s<small>Skærmbillede: %s</small></span></figure>'%(ratio,ic('<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="m21 16-5-5-8 8"/>',26,1.3),label)

toc=[('kort','Kort fortalt'),('vurdering','Vores vurdering'),('opret','Sådan opretter du en profil'),('foerste','Dine første dage'),('gratis','Gratis eller betalt'),('priser','Priser'),('funktioner','Funktioner'),('medlemmer','Hvem er på Dating.dk'),('app','App'),('sikkerhed','Sikkerhed og privatliv'),('opsig','Opsig og slet profil'),('brugere','Det siger brugerne'),('alternativer','Alternativer'),('faq','Spørgsmål og svar'),('konklusion','Konklusion'),('baggrund','Mere om Dating.dk')]

H=[]
H.append('''<section class="rhero">
  <div class="glow" aria-hidden="true"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Brødkrummer"><a href="#">Forside</a><span>/</span><a href="#">Anmeldelser</a><span>/</span><span aria-current="page">Dating.dk</span></nav>
    <div class="rhero-grid">
      <div>
        <div class="rlogo"><img src="img/logo-dating.webp" alt="Dating.dk"></div>
        <h1>Dating.dk anmeldelse</h1>
        <p class="verdict">En bred dansk datingside til dig, der søger en kæreste. Solide funktioner og manuel godkendelse af profiler, men du skal betale for at læse beskeder, og vilkårene kræver opmærksomhed.</p>
        <p class="meta"><span>'''+I['clock'].replace('22','16')+'''Opdateret 11. november 2026</span><span>Af Dateworld-redaktionen</span><span>Læsetid ca. 8 min.</span></p>
      </div>
      <aside class="fact" aria-label="Fakta om Dating.dk">
        <div class="score"><b>3,8</b><span>ud af 5<small>Vores samlede vurdering</small></span></div>
        <dl>
          <div><dt>Pris fra</dt><dd>129 kr. pr. 4 uger</dd></div>
          <div><dt>Gratis oprettelse</dt><dd>Ja</dd></div>
          <div><dt>App</dt><dd>iOS og Android</dd></div>
          <div><dt>Målgruppe</dt><dd>Alle aldre</dd></div>
          <div><dt>Online siden</dt><dd>1998</dd></div>
        </dl>
        <a class="cta" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a>
        <p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p>
      </aside>
    </div>
  </div>
</section>''')

art=[]
art.append('''<section id="kort" class="blk"><h2>Kort fortalt</h2>
  <div class="fit">
    <div class="fit-yes"><h3>Passer til dig, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(CHK,t) for t in ['du søger en kæreste og gerne vil have mange danske profiler at vælge imellem','du vil i gang uden at betale med det samme','du sætter pris på, at billeder og profiler bliver godkendt manuelt','du vil have dansk kundeservice, som svarer alle ugens dage'])+'''</ul></div>
    <div class="fit-no"><h3>Passer mindre godt, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(MIN,t) for t in ['du kun leder efter noget uforpligtende','du vil læse og besvare beskeder uden at betale','du ikke vil binde dig: det billigste tilbud kræver 84 dages binding'])+'''</ul></div>
  </div>
</section>''')
rows=[('Pris',3.8,'Gratis at oprette sig, og +PlusProfil koster 129 kr. pr. 4 uger. Rimeligt for en bred dansk tjeneste.'),('Vilkår',3.2,'Automatisk fornyelse og binding på det billigste tilbud. Læs betingelserne, før du køber.'),('Funktioner',4.2,'Søgning, likes, matches, Singler i nærheden, events og en app til begge platforme.'),('Sikkerhed',4.3,'Manuel godkendelse af profiler, krav om ægte billeder og dansk kundeservice alle dage.'),('Brugernes bedømmelse',3.7,'3,6 på Trustpilot og 3,8 i App Store: flest gode anmeldelser, men tydelige klager over vilkår.')]
art.append('''<section id="vurdering" class="blk"><h2>Vores vurdering</h2>
  <p class="lede">Vi vurderer alle datingsider ud fra de samme fem områder: pris, vilkår, funktioner, sikkerhed og brugernes egne bedømmelser. <a href="#om">Sådan vurderer vi</a></p>
  <div class="rates">'''+''.join('<div class="rate"><div class="rate-top"><b>%s</b><span>%s</span></div><div class="rbar"><i style="width:%d%%"></i></div><p>%s</p></div>'%(n,str(v).replace('.',','),v*20,t) for n,v,t in rows)+'''</div>
</section>''')
steps=[('Fortæl, hvem du er','Vælg på forsiden, hvem du er, og hvem du søger.'),('Opret dit login','Angiv e-mail og adgangskode. Dating.dk lover, at du er i gang på 3 minutter.'),('Udfyld profilen','Skriv om dig selv, og tilføj billeder. Billederne godkendes manuelt, før andre kan se dem.')]
art.append('''<section id="opret" class="blk"><h2>Sådan opretter du en profil</h2>
  <p class="lede">Det er gratis og hurtigt at oprette en profil. Sådan ser de første trin ud.</p>
  <ol class="steps">'''+''.join('<li><span class="n">%d</span>%s<h3>%s</h3><p>%s</p></li>'%(i+1,shot('Offentlig side, trin %d'%(i+1),'4/3'),a,b) for i,(a,b) in enumerate(steps))+'''</ol>
</section>''')
DAYS=[('Dag 1', 'Profilen kommer på plads', 'Du opretter dig, vælger hvem du søger, og skriver en kort profiltekst. Dine billeder bliver godkendt manuelt, så der kan gå lidt tid, før de er synlige. Brug et par minutter ekstra på teksten og et par billeder, hvor du smiler. Det er dem, folk lægger mærke til først.'), ('Dag 2–3', 'Du kigger dig omkring', 'Søg på alder og område, like de profiler, du synes om, og prøv Singler i nærheden. Alt det kan du gratis, men du kan ikke se, hvem der har liket dig, eller hvem du har matchet med.'), ('Uge 1', 'Den første samtale', 'Vil du læse dine beskeder og skrive frit med andre, kræver det en +PlusProfil. Start med en kort besked, der spørger ind til noget i profilen; det giver flere svar end et "hej". Få flere idéer i vores guide til <a href="#">den første besked</a>.'), ('Senere', 'Fortsæt eller stop', 'Har du fundet nogen, eller er siden ikke noget for dig, så husk at slå automatisk fornyelse fra i god tid. Se hvordan under <a href="#opsig">opsig og slet profil</a>.')]
art.append('''<section id="foerste" class="blk"><h2>Sådan kan dine første dage se ud</h2>
  <p class="lede">Et typisk forløb, når du er ny på Dating.dk, bygget på Dating.dk's egne sider og brugernes anmeldelser.</p>
  <ol class="diary">'''+''.join('<li><span class="when">%s</span><div><h3>%s</h3><p>%s</p></div></li>'%d for d in DAYS)+'''</ol>
  <div class="note">'''+I['info']+'''<p><b>Godt at vide:</b> Introtilbuddet til 29 kr. har 84 dages binding og fortsætter derefter til 129 kr. pr. 4 uger. Vil du bare prøve, er engangsbetalingen uden fornyelse det sikre valg.</p></div>
</section>''')
feat=[('Oprette profil og uploade billeder',1,1),('Søge efter profiler',1,1),('Like andre profiler',1,1),('Singler i nærheden',1,1),('Bruge appen',1,1),('Se, hvem der har liket dig',0,1),('Se dine matches',0,1),('Læse beskeder',0,1),('Skrive frit til alle',0,1),('Blive vist oftere i søgninger',0,1)]
def cell(v):
    if v==1: return '<td class="y">%s<span class="sr">Ja</span></td>'%YES
    if v==0: return '<td class="x">%s<span class="sr">Nej</span></td>'%NO
    return '<td class="q">%s</td>'%v
art.append('''<section id="gratis" class="blk"><h2>Gratis eller betalt</h2>
  <p class="lede">Det er gratis at oprette en profil og kigge sig omkring. Vil du se, hvem der er interesseret, og skrive sammen, kræver det en +PlusProfil.</p>
  <table class="ftbl"><thead><tr><th>Funktion</th><th>Gratis</th><th>Medlemskab</th></tr></thead><tbody>'''+''.join('<tr><th scope="row">%s</th>%s%s</tr>'%(n,cell(a),cell(b)) for n,a,b in feat)+'''</tbody></table>
</section>''')
plans=[('Introtilbud','29 kr.','første 4 uger','Derefter 129 kr. pr. 4 uger. 84 dages binding.',True,'Billigst at starte'),('Abonnement','129 kr.','pr. 4 uger','Fornyes automatisk. Kan også betales med MobilePay.',False,''),('Engangsbetaling','239 kr.','for 28 dage','Ingen fornyelse. Betales med kort.',False,'')]
art.append('''<section id="priser" class="blk"><h2>Priser</h2>
  <p class="lede">Medlemskabet hedder +PlusProfil og fås i tre varianter. Priserne er fra Dating.dk's prisside, november 2026.</p>
  <div class="plans">'''+''.join('<div class="plan%s">%s<h3>%s</h3><p class="pm"><b>%s</b> %s</p><p class="tot">%s</p></div>'%(' best' if b else '','<span class="pbadge">%s</span>'%bd if b else '',n,p,per,t) for n,p,per,t,b,bd in plans)+'''</div>
  <div class="note">'''+I['info']+'''<p><b>Fornyes medlemskabet automatisk?</b> Ja, abonnementer fornyes automatisk, indtil du melder fra i betalingscentret, og fornyelsen sker et par timer før din profiltid udløber. Har du valgt et tilbud med binding, betaler du perioden ud, selv om du melder fra.</p></div>
</section>''')
fs=[('search','Søgning','Find profiler efter alder og område, og like dem, du synes om.'),('pin','Singler i nærheden','Se, hvem der er single tæt på dig lige nu.'),('match','Likes og matches','Se, hvem der har liket dig, og hvem du har matchet med (+PlusProfil).'),('chat','Beskeder','Læs og skriv beskeder til alle profiler med +PlusProfil.'),('users','Events','Singlearrangementer og temasider til fx Valentinsdag og Singles Day.'),('phone','App','Profil, beskeder, likes og anbefalinger i appen til iOS og Android.')]
art.append('''<section id="funktioner" class="blk"><h2>Funktioner</h2>
  <p class="lede">Det får du adgang til som medlem, beskrevet ud fra Dating.dk's hjemmeside og hjælpecenter.</p>
  <div class="feats">'''+''.join('<div class="fcard"><span class="fi">%s</span><h3>%s</h3><p>%s</p></div>'%(I[a],b,c) for a,b,c in fs)+'''</div>
</section>''')
art.append('''<section id="medlemmer" class="blk"><h2>Hvem er på Dating.dk</h2>
  <div class="stats">
    <div>'''+I['users']+'''<b>Siden 1998</b><span>En af de ældste danske datingsider</span></div>
    <div>'''+I['cake']+'''<b>18+</b><span>Alle aldre over 18 år</span></div>
    <div>'''+I['pin']+'''<b>Hele landet</b><span>Egne sider for de største byer</span></div>
  </div>
  <p class="src">Kilde: Dating.dk, november 2026.</p>
  <p>Dating.dk henvender sig bredt til singler i hele Danmark, der søger en kæreste eller nye bekendtskaber, og har egne sider for København, Aarhus, Odense, Aalborg og Esbjerg. Siden oplyser ikke et medlemstal, men fremhæver selv, at den har flest aktive profiler i nærheden af dig. Der er også en særskilt indgang til seniordating.</p>
</section>''')
art.append('''<section id="app" class="blk"><h2>App</h2>
  <div class="appgrid">
    <div><p>Appen er gratis til både iPhone og Android og giver adgang til det samme som hjemmesiden: profil, beskeder, likes, matches og anbefalinger. Du kan købe +PlusProfil direkte i appen. I App Store har den 3,8 ud af 5 fra omkring 1.300 bedømmelser, og på Google Play er den hentet over 100.000 gange.</p>
      <ul class="stores"><li>'''+I['phone'].replace('22','18')+'''App Store</li><li>'''+I['phone'].replace('22','18')+'''Google Play</li></ul></div>
    '''+shot('Appen på mobil','9/16')+'''
  </div>
</section>''')
sec=[('shield','Manuel godkendelse','Profiler og billeder godkendes manuelt. Billeder skal være aktuelle og kun vise dig.'),('flag','Anmeld profiler','Anmeld mistænkelige profiler til kundeservice, som kan slette profiler og give karantæne.'),('chat','Dansk kundeservice','Kundeservice svarer alle ugens dage på kundeservice@dating.dk.'),('lock','18 år og privatliv','Du skal være mindst 18 år. Du kan altid trække dit samtykke tilbage ved at slette profilen.')]
art.append('''<section id="sikkerhed" class="blk"><h2>Sikkerhed og privatliv</h2>
  <div class="secs">'''+''.join('<div class="sc"><span class="fi">%s</span><div><h3>%s</h3><p>%s</p></div></div>'%(I[a],b,c) for a,b,c in sec)+'''</div>
</section>''')
op=[('Log ind','Log ind på Dating.dk, og gå til betalingscentret.'),('Meld dig fra','Slå den automatiske fornyelse fra. Den profiltid, du allerede har betalt for, kan du bruge til den udløber.'),('Slet profilen','Vil du fjerne profilen helt, så slet den under dine indstillinger. Først da er den ikke længere synlig for andre.'),('Gem bekræftelsen','Gem din kvittering, indtil medlemskabet er udløbet, så du kan dokumentere, at du har meldt fra.')]
art.append('''<section id="opsig" class="blk"><h2>Opsig og slet profil</h2>
  <p class="lede">Sådan stopper du medlemskabet og fjerner din profil.</p>
  <ol class="diary">'''+''.join('<li><span class="when">Trin %d</span><div><h3>%s</h3><p>%s</p></div></li>'%(i+1,h,t) for i,(h,t) in enumerate(op))+'''</ol>
  <div class="note">'''+I['info']+'''<p><b>Tip:</b> Meld fra i god tid. Abonnementet fornyes et par timer før din profiltid udløber, så vent ikke til sidste dag.</p></div>
</section>''')
art.append('''<section id="brugere" class="blk"><h2>Det siger brugerne</h2>
  <p class="lede">Sådan bedømmer brugerne Dating.dk på Trustpilot og i app-butikkerne. Tallene er hentet november 2026.</p>
  <div class="urates">
    <div><span class="usrc">Trustpilot</span><b>3,6</b><span class="uof">ud af 5</span><small>Ca. 3.500 anmeldelser</small></div>
    <div><span class="usrc">App Store</span><b>3,8</b><span class="uof">ud af 5</span><small>Ca. 1.300 bedømmelser</small></div>
    <div><span class="usrc">Google Play</span><b>100.000+</b><span class="uof">downloads</span><small>Hentet over 100.000 gange</small></div>
  </div>
  <div class="proscons">
    <div><h3>'''+CHK+'''Det roser brugerne</h3><ul><li>En overskuelig side, der er nem at finde rundt på</li><li>Mange seriøse profiler og gode chancer for at få kontakt</li><li>Hjælpsom kundeservice, der svarer hurtigt</li></ul></div>
    <div><h3>'''+MIN+'''Det klager brugerne over</h3><ul><li>Man skal betale for at læse beskeder, og abonnementet fornyes automatisk</li><li>En del inaktive profiler og profiler uden billede</li></ul></div>
  </div>
  <p class="src">Opsummeret ud fra anmeldelser på Trustpilot, november 2026. 86 % af anmeldelserne giver 4 eller 5 stjerner.</p>
</section>''')
alts=[('logo-single.svg','Single.dk','For singler i hele landet','22px'),('logo-senior.webp','Senior.dk','Til dig over 50','24px'),(None,'Singles50','Matchning for singler over 50',None)]
art.append('''<section id="alternativer" class="blk"><h2>Alternativer til Dating.dk</h2>
  <div class="alts">'''+''.join('<a class="alt" href="#"><span class="alg">%s</span><h3>%s</h3><p>%s</p><span class="rgo">Læs anmeldelsen %s</span></a>'%(('<img src="img/%s" alt="" style="height:%s">'%(f,h)) if f else '<b>%s</b>'%n,n,t,ARW) for f,n,t,h in alts)+'''</div>
</section>''')
qs=[('Er Dating.dk gratis?','Det er gratis at oprette en profil, søge, like andre og bruge appen. Vil du se, hvem der har liket dig, læse beskeder og skrive frit, kræver det en +PlusProfil.'),('Hvad koster Dating.dk?','En +PlusProfil koster 129 kr. pr. 4 uger som abonnement eller 239 kr. for 28 dage som engangsbetaling. Nye brugere kan starte med 4 uger for 29 kr. mod 84 dages binding.'),('Hvordan sletter jeg min profil på Dating.dk?','Meld først fra i betalingscentret, så abonnementet ikke fornyes. Slet derefter profilen under dine indstillinger.'),('Har Dating.dk en app?','Ja, appen er gratis til både iPhone og Android og giver adgang til profil, beskeder, likes og matches.'),('Hvem bruger Dating.dk?','Singler i alle aldre over 18 år fra hele landet, som oftest søger en kæreste eller et seriøst forhold.')]
art.append('''<section id="faq" class="blk"><h2>Spørgsmål og svar</h2>
  <div class="qa">'''+''.join('<details><summary><span>%s</span>%s</summary><p>%s</p></details>'%(q,PLUS,a) for q,a in qs)+'''</div>
</section>''')
art.append('''<section id="konklusion" class="blk">
  <div class="concl">
    <div><h2>Konklusion</h2><p>Dating.dk er et godt sted at starte, hvis du søger en kæreste og vil have en dansk tjeneste med mange profiler, manuel godkendelse og kundeservice, der svarer. Vær opmærksom på, at du skal betale for at læse beskeder, og at introtilbuddet har binding.</p></div>
    <div class="concl-cta"><div class="score sm"><b>3,8</b><span>ud af 5<small>Vores samlede vurdering</small></span></div><a class="cta light" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a><p class="adl"><span>Reklamelink</span></p></div>
  </div>
</section>
<section id="baggrund" class="blk bg"><h2>Mere om Dating.dk</h2>
  <div class="bggrid">
    <div class="seo">
      <h3>Hvad er Dating.dk?</h3>
      <p>Dating.dk er en dansk datingside for singler, der søger en kæreste. Siden har været online siden 1998 og drives af Dating.dk ApS fra Viborg, så den er en af de ældste datingsider herhjemme. Den henvender sig bredt til singler over 18 år i hele landet.</p>
      <h3>Hvad koster Dating.dk?</h3>
      <p>Det er gratis at oprette en profil, men vil du skrive frit med andre, kræver det et medlemskab. Et abonnement koster 129 kr. pr. 4 uger, og nye brugere kan starte med 29 kr. for de første 4 uger mod binding. Se den fulde oversigt under <a href="#priser">priser</a>.</p>
      <h3>Dating.dk login og app</h3>
      <p>Du logger ind på dating.dk med din e-mail og adgangskode, og du kan bruge den samme profil i appen til iPhone og Android. Appen er gratis at hente, og du kan købe +PlusProfil direkte i den.</p>
      <h3>Er Dating.dk seriøst?</h3>
      <p>Dating.dk godkender profiler og billeder manuelt og afviser billeder, der ikke ser ægte ud. Ser du en mistænkelig profil, kan du anmelde den til kundeservice. Læs mere under <a href="#sikkerhed">sikkerhed og privatliv</a>.</p>
      <h3>Dating.dk erfaringer</h3>
      <p>De fleste brugere er tilfredse, især med hvor nem siden er, og med kundeservice. De mest kritiske anmeldelser handler om betaling for beskeder og automatisk fornyelse. Se tallene under <a href="#brugere">det siger brugerne</a>, og sammenlign med andre tjenester i vores oversigt over <a href="#">bedste datingsider</a>.</p>
    </div>
    <dl class="bgfacts">
      <div><dt>Startet</dt><dd>1998</dd></div>
      <div><dt>Ejer</dt><dd>Dating.dk ApS</dd></div>
      <div><dt>Hovedsæde</dt><dd>Viborg</dd></div>
      <div><dt>Hjemmeside</dt><dd>dating.dk</dd></div>
    </dl>
  </div>
</section>
<section id="om" class="blk om">
  <h2>Om anmeldelsen</h2>
  <p>Vi har gennemgået Dating.dk's hjemmeside, priser, vilkår, hjælpecenter og brugernes anmeldelser i november 2026. Dateworld får betaling, hvis du opretter et medlemskab via vores links. Det påvirker ikke, hvad vi skriver. <a href="#">Sådan arbejder vi</a></p>
</section>''')

side='''<aside class="side">
  <div class="sticky">
    <div class="mini"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Fra 129 kr. pr. 4 uger</span></div></div>
    <a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a>
    <p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p>
    <nav class="toc" aria-label="Indhold"><p>Indhold</p><ol>'''+''.join('<li><a href="#%s">%s</a></li>'%(a,b) for a,b in toc)+'''</ol></nav>
  </div>
</aside>'''
main='<section class="rbody"><div class="wrap rgrid"><article class="rart">'+'\n'.join(art)+'</article>'+side+'</div></section>'
mbar='<div class="mbar" id="mbar"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Fra 129 kr. pr. 4 uger · Reklamelink</span></div><a href="#" rel="sponsored nofollow">Besøg siden</a></div>'

css=open('/home/claude/build/review.css',encoding='utf-8').read()
js=open('/home/claude/build/review.js',encoding='utf-8').read()
out=head+'<style>'+css+'</style>\n'+top.replace('<main','<main')
out=out+'<main>'+'\n'.join(H)+'\n'+main+'</main>\n'+foot+'\n'+mbar+'\n<script>'+menu_js+'</script>\n<script>'+faq_js+'</script>\n<script>'+js+'</script>\n</body>\n</html>\n'
open('/home/claude/dw-demo/index.html','w',encoding='utf-8').write(out)
print(len(out))
