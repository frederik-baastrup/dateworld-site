import re
src=open('/home/claude/dw-page/index.html',encoding='utf-8').read()
head=src[:src.index('</head>')]
title_old=re.search(r'<title>.*?</title>',head).group(0)
head=head.replace(title_old,'<title>Dating.dk anmeldelse – Dateworld</title>')
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
def shot(label,ratio='16/10'): return '<figure class="shot" style="aspect-ratio:%s"><span>%s<small>[SKÆRMBILLEDE: %s]</small></span></figure>'%(ratio,ic('<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="m21 16-5-5-8 8"/>',26,1.3),label)

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
        <p class="verdict">En bred dansk datingside til dig, der søger en kæreste. [Én sætning om vores samlede vurdering.]</p>
        <p class="meta"><span>'''+I['clock'].replace('22','16')+'''Opdateret [DATO]</span><span>Af [NAVN]</span><span>Læsetid ca. 8 min.</span></p>
      </div>
      <aside class="fact" aria-label="Fakta om Dating.dk">
        <div class="score"><b>[4,2]</b><span>ud af 5<small>Vores samlede vurdering</small></span></div>
        <dl>
          <div><dt>Pris fra</dt><dd>[PRIS] pr. md.</dd></div>
          <div><dt>Gratis oprettelse</dt><dd>[JA/NEJ]</dd></div>
          <div><dt>App</dt><dd>[iOS og Android]</dd></div>
          <div><dt>Målgruppe</dt><dd>Alle aldre</dd></div>
          <div><dt>Typisk alder</dt><dd>[ALDER]</dd></div>
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
    <div class="fit-yes"><h3>Passer til dig, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(CHK,t) for t in ['du søger en kæreste og vil have mange profiler at vælge imellem','du vil i gang uden at betale med det samme','du foretrækker en dansk tjeneste med dansk support','[Fjerde punkt ud fra profilen]'])+'''</ul></div>
    <div class="fit-no"><h3>Passer mindre godt, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(MIN,t) for t in ['du kun leder efter noget uforpligtende','du vil skrive frit med andre uden medlemskab','[Tredje punkt ud fra profilen]'])+'''</ul></div>
  </div>
</section>''')
rows=[('Pris',3.8,'[Én linje: pris i forhold til, hvad medlemskabet giver adgang til.]'),('Vilkår',4.0,'[Én linje: binding, automatisk fornyelse og hvor let det er at opsige.]'),('Funktioner',4.2,'[Én linje: søgning, beskeder, matchforslag og app.]'),('Sikkerhed',4.0,'[Én linje: verificering, blokering, support og privatliv.]'),('Brugernes bedømmelse',4.4,'[Én linje: samlet bedømmelse på Trustpilot og i app-butikkerne.]')]
art.append('''<section id="vurdering" class="blk"><h2>Vores vurdering</h2>
  <p class="lede">Vi vurderer alle datingsider ud fra de samme fem områder: pris, vilkår, funktioner, sikkerhed og brugernes egne bedømmelser. <a href="#om">Sådan vurderer vi</a></p>
  <div class="rates">'''+''.join('<div class="rate"><div class="rate-top"><b>%s</b><span>[%s]</span></div><div class="rbar"><i style="width:%d%%"></i></div><p>%s</p></div>'%(n,str(v).replace('.',','),v*20,t) for n,v,t in rows)+'''</div>
</section>''')
steps=[('Vælg, hvem du søger','Angiv køn, alder og område på forsiden.'),('Opret login','E-mail og adgangskode, eller log ind med [Google/Apple].'),('Bekræft og udfyld','[Hvad Dating.dk beder om bagefter: e-mail, profiltekst og billeder.]')]
art.append('''<section id="opret" class="blk"><h2>Sådan opretter du en profil</h2>
  <p class="lede">Sådan ser de første trin ud på Dating.dk, fra forsiden til oprettelsen af dit login.</p>
  <ol class="steps">'''+''.join('<li><span class="n">%d</span>%s<h3>%s</h3><p>%s</p></li>'%(i+1,shot('Offentlig side, trin %d'%(i+1),'4/3'),a,b) for i,(a,b) in enumerate(steps))+'''</ol>
</section>''')
DAYS=[('Dag 1', 'Profilen kommer på plads', 'Du opretter dig, vælger hvem du søger, og skriver en kort profiltekst. [Om profilen skal godkendes, før andre kan se den.] Brug et par minutter ekstra på teksten og et par billeder, hvor du smiler. Det er dem, folk lægger mærke til først.'), ('Dag 2–3', 'Du kigger dig omkring', 'Søg på alder og område, gem de profiler, du synes om, og se, hvem der har kigget forbi din profil. Som gratis bruger kan du [hvad man kan uden medlemskab].'), ('Uge 1', 'Den første samtale', 'Vil du skrive frit med andre, kræver det [et medlemskab]. Start med en kort besked, der spørger ind til noget i profilen; det giver flere svar end et "hej". Få flere idéer i vores guide til <a href="#">den første besked</a>.'), ('Senere', 'Fortsæt eller stop', 'Har du fundet nogen, eller er siden ikke noget for dig, så husk at slå automatisk fornyelse fra i god tid. Se hvordan under <a href="#opsig">opsig og slet profil</a>.')]
art.append('''<section id="foerste" class="blk"><h2>Sådan kan dine første dage se ud</h2>
  <p class="lede">Et typisk forløb, når du er ny på Dating.dk, bygget på Dating.dk's egne sider og brugernes anmeldelser.</p>
  <ol class="diary">'''+''.join('<li><span class="when">%s</span><div><h3>%s</h3><p>%s</p></div></li>'%d for d in DAYS)+'''</ol>
  <div class="note">'''+I['info']+'''<p><b>Godt at vide:</b> [Én konkret ting, nye brugere ofte overser, fx at medlemskabet fornyes automatisk, eller at profiler uden billeder får færre svar.]</p></div>
</section>''')
feat=[('Oprette profil',1,1),('Se andres profiler',1,1),('Søge med filtre','[?]',1),('Modtage beskeder',1,1),('Læse beskeder',0,1),('Skrive beskeder',0,1),('Se, hvem der har besøgt dig',0,1)]
def cell(v):
    if v==1: return '<td class="y">%s<span class="sr">Ja</span></td>'%YES
    if v==0: return '<td class="x">%s<span class="sr">Nej</span></td>'%NO
    return '<td class="q">%s</td>'%v
art.append('''<section id="gratis" class="blk"><h2>Gratis eller betalt</h2>
  <p class="lede">Det er gratis at oprette en profil, men nogle funktioner kræver medlemskab. Her er forskellen.</p>
  <table class="ftbl"><thead><tr><th>Funktion</th><th>Gratis</th><th>Medlemskab</th></tr></thead><tbody>'''+''.join('<tr><th scope="row">%s</th>%s%s</tr>'%(n,cell(a),cell(b)) for n,a,b in feat)+'''</tbody></table>
</section>''')
plans=[('1 måned',False),('3 måneder',True),('6 måneder',False)]
art.append('''<section id="priser" class="blk"><h2>Priser</h2>
  <p class="lede">Jo længere periode, jo lavere månedspris. Priserne er fra [DATO].</p>
  <div class="plans">'''+''.join('<div class="plan%s">%s<h3>%s</h3><p class="pm"><b>[PRIS]</b> pr. md.</p><p class="tot">[PRIS] i alt</p></div>'%(' best' if b else '','<span class="pbadge">Lavest månedspris</span>' if b else '',n) for n,b in plans)+'''</div>
  <div class="note">'''+I['info']+'''<p><b>Fornyes medlemskabet automatisk?</b> [Ja/nej. Hvis ja: hvor længe før udløb, du skal opsige, og hvor du gør det.]</p></div>
</section>''')
fs=[('search','Søgning','Filtrér på alder, område og [andre filtre].'),('match','Matchforslag','[Hvordan Dating.dk foreslår profiler.]'),('chat','Beskeder','[Hvordan man skriver sammen, og hvad der er gratis.]'),('eye','Besøgende','[Se, hvem der har kigget på din profil.]'),('star','Favoritter','[Gem profiler, du vil vende tilbage til.]'),('phone','App','Alle funktioner [også i appen].')]
art.append('''<section id="funktioner" class="blk"><h2>Funktioner</h2>
  <p class="lede">Det får du adgang til som medlem, beskrevet ud fra Dating.dk's hjemmeside og hjælpecenter.</p>
  <div class="feats">'''+''.join('<div class="fcard"><span class="fi">%s</span><h3>%s</h3><p>%s</p></div>'%(I[a],b,c) for a,b,c in fs)+'''</div>
</section>''')
art.append('''<section id="medlemmer" class="blk"><h2>Hvem er på Dating.dk</h2>
  <div class="stats">
    <div>'''+I['users']+'''<b>[ANTAL]</b><span>Aktive profiler</span></div>
    <div>'''+I['cake']+'''<b>[ALDER]</b><span>Flest medlemmer</span></div>
    <div>'''+I['pin']+'''<b>Hele landet</b><span>[Flest i …]</span></div>
  </div>
  <p class="src">Kilde: Dating.dk, [DATO].</p>
  <p>[2–3 sætninger om målgruppen ud fra Dating.dk's egne oplysninger: aldersspænd, hvad medlemmerne søger, og hvor i landet de bor.]</p>
</section>''')
art.append('''<section id="app" class="blk"><h2>App</h2>
  <div class="appgrid">
    <div><p>[Om appen findes til iOS og Android, hvad den kan, og om noget kun virker på hjemmesiden.]</p>
      <ul class="stores"><li>'''+I['phone'].replace('22','18')+'''App Store</li><li>'''+I['phone'].replace('22','18')+'''Google Play</li></ul></div>
    '''+shot('Appen på mobil','9/16')+'''
  </div>
</section>''')
sec=[('shield','Verificering','[Om profiler bliver godkendt, og hvordan.]'),('block','Blokering','Bloker brugere, du ikke vil høre fra.'),('flag','Anmeld profiler','[Hvordan du anmelder en mistænkelig profil.]'),('lock','Privatliv','[Hvem der kan se dine billeder og oplysninger.]')]
art.append('''<section id="sikkerhed" class="blk"><h2>Sikkerhed og privatliv</h2>
  <div class="secs">'''+''.join('<div class="sc"><span class="fi">%s</span><div><h3>%s</h3><p>%s</p></div></div>'%(I[a],b,c) for a,b,c in sec)+'''</div>
</section>''')
op=[('Log ind','Log ind på Dating.dk, og gå til [Indstillinger].'),('Slå fornyelse fra','Vælg [Medlemskab], og slå automatisk fornyelse fra. [Hvad der sker med den periode, du har betalt for.]'),('Slet profilen','Vil du fjerne profilen helt, så vælg [Slet profil] nederst. [Om billeder og beskeder slettes med det samme.]'),('Gem bekræftelsen','Du får en bekræftelse på e-mail. Gem den, indtil medlemskabet er udløbet.')]
art.append('''<section id="opsig" class="blk"><h2>Opsig og slet profil</h2>
  <p class="lede">Sådan stopper du medlemskabet og fjerner din profil.</p>
  <ol class="diary">'''+''.join('<li><span class="when">Trin %d</span><div><h3>%s</h3><p>%s</p></div></li>'%(i+1,h,t) for i,(h,t) in enumerate(op))+'''</ol>
  <div class="note">'''+I['info']+'''<p><b>Tip:</b> Opsig medlemskabet mindst [X] dage før udløb, hvis du ikke vil fortsætte.</p></div>
</section>''')
art.append('''<section id="brugere" class="blk"><h2>Det siger brugerne</h2>
  <p class="lede">Sådan bedømmer brugerne Dating.dk på Trustpilot og i app-butikkerne. Tallene er hentet [DATO].</p>
  <div class="urates">
    <div><span class="usrc">Trustpilot</span><b>[x,x]</b><span class="uof">ud af 5</span><small>[ANTAL] anmeldelser</small></div>
    <div><span class="usrc">App Store</span><b>[x,x]</b><span class="uof">ud af 5</span><small>[ANTAL] bedømmelser</small></div>
    <div><span class="usrc">Google Play</span><b>[x,x]</b><span class="uof">ud af 5</span><small>[ANTAL] bedømmelser</small></div>
  </div>
  <div class="proscons">
    <div><h3>'''+CHK+'''Det roser brugerne</h3><ul><li>[Typisk ros, med egne ord]</li><li>[Typisk ros]</li><li>[Typisk ros]</li></ul></div>
    <div><h3>'''+MIN+'''Det klager brugerne over</h3><ul><li>[Typisk klage, med egne ord]</li><li>[Typisk klage]</li></ul></div>
  </div>
  <p class="src">Opsummeret ud fra de [ANTAL] nyeste anmeldelser på Trustpilot, [DATO].</p>
</section>''')
alts=[('logo-single.svg','Single.dk','For singler i hele landet','22px'),('logo-senior.webp','Senior.dk','Til dig over 50','24px'),(None,'Singles50','Matchning for singler over 50',None)]
art.append('''<section id="alternativer" class="blk"><h2>Alternativer til Dating.dk</h2>
  <div class="alts">'''+''.join('<a class="alt" href="#"><span class="alg">%s</span><h3>%s</h3><p>%s</p><span class="rgo">Læs anmeldelsen %s</span></a>'%(('<img src="img/%s" alt="" style="height:%s">'%(f,h)) if f else '<b>%s</b>'%n,n,t,ARW) for f,n,t,h in alts)+'''</div>
</section>''')
qs=[('Er Dating.dk gratis?','Du kan oprette en profil gratis. [Hvad man kan gratis, og hvad der kræver medlemskab.]'),('Hvad koster Dating.dk?','Et medlemskab koster fra [PRIS] pr. måned. Se alle priser ovenfor.'),('Hvordan sletter jeg min profil på Dating.dk?','Gå til [Indstillinger] og vælg [Slet profil]. Se trinene under "Opsig og slet profil".'),('Har Dating.dk en app?','[Ja/nej, og til hvilke telefoner.]'),('Hvem bruger Dating.dk?','[Kort om aldersgruppe og målgruppe.]')]
art.append('''<section id="faq" class="blk"><h2>Spørgsmål og svar</h2>
  <div class="qa">'''+''.join('<details><summary><span>%s</span>%s</summary><p>%s</p></details>'%(q,PLUS,a) for q,a in qs)+'''</div>
</section>''')
art.append('''<section id="konklusion" class="blk">
  <div class="concl">
    <div><h2>Konklusion</h2><p>[2–3 sætninger: hvem Dating.dk passer bedst til, og hvad man skal være opmærksom på.]</p></div>
    <div class="concl-cta"><div class="score sm"><b>[4,2]</b><span>ud af 5<small>Vores samlede vurdering</small></span></div><a class="cta light" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a><p class="adl"><span>Reklamelink</span></p></div>
  </div>
</section>
<section id="baggrund" class="blk bg"><h2>Mere om Dating.dk</h2>
  <div class="bggrid">
    <div class="seo">
      <h3>Hvad er Dating.dk?</h3>
      <p>Dating.dk er en dansk datingside for singler, der søger en kæreste. [2–3 sætninger om, hvornår siden startede, hvem der står bag, og hvilken målgruppe den henvender sig til.]</p>
      <h3>Hvad koster Dating.dk?</h3>
      <p>Det er gratis at oprette en profil, men vil du skrive frit med andre, kræver det et medlemskab. [1–2 sætninger om prisniveau og perioder.] Se den fulde oversigt under <a href="#priser">priser</a>.</p>
      <h3>Dating.dk login og app</h3>
      <p>[1–2 sætninger om, hvordan man logger ind, om man kan bruge Google eller Apple, og om der findes en app til iOS og Android.]</p>
      <h3>Er Dating.dk seriøst?</h3>
      <p>[2 sætninger om, hvad Dating.dk gør for at holde falske profiler ude, og hvordan man anmelder en profil.] Læs mere under <a href="#sikkerhed">sikkerhed og privatliv</a>.</p>
      <h3>Dating.dk erfaringer</h3>
      <p>[1–2 sætninger, der opsummerer brugernes bedømmelser med egne ord.] Se tallene under <a href="#brugere">det siger brugerne</a>, og sammenlign med andre tjenester i vores oversigt over <a href="#">bedste datingsider</a>.</p>
    </div>
    <dl class="bgfacts">
      <div><dt>Startet</dt><dd>[ÅR]</dd></div>
      <div><dt>Ejer</dt><dd>[VIRKSOMHED]</dd></div>
      <div><dt>Land</dt><dd>Danmark</dd></div>
      <div><dt>Hjemmeside</dt><dd>dating.dk</dd></div>
    </dl>
  </div>
</section>
<section id="om" class="blk om">
  <h2>Om anmeldelsen</h2>
  <p>Vi har gennemgået Dating.dk's hjemmeside, priser, vilkår, hjælpecenter og brugernes anmeldelser [DATO]. Dateworld får betaling, hvis du opretter et medlemskab via vores links. Det påvirker ikke, hvad vi skriver. <a href="#">Sådan arbejder vi</a></p>
</section>''')

side='''<aside class="side">
  <div class="sticky">
    <div class="mini"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Fra [PRIS] pr. md.</span></div></div>
    <a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a>
    <p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p>
    <nav class="toc" aria-label="Indhold"><p>Indhold</p><ol>'''+''.join('<li><a href="#%s">%s</a></li>'%(a,b) for a,b in toc)+'''</ol></nav>
  </div>
</aside>'''
main='<section class="rbody"><div class="wrap rgrid"><article class="rart">'+'\n'.join(art)+'</article>'+side+'</div></section>'
mbar='<div class="mbar" id="mbar"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Fra [PRIS] pr. md. · Reklamelink</span></div><a href="#" rel="sponsored nofollow">Besøg siden</a></div>'

css=open('/home/claude/build/review.css',encoding='utf-8').read()
js=open('/home/claude/build/review.js',encoding='utf-8').read()
out=head+'<style>'+css+'</style>\n'+top.replace('<main','<main')
out=out+'<main>'+'\n'.join(H)+'\n'+main+'</main>\n'+foot+'\n'+mbar+'\n<script>'+menu_js+'</script>\n<script>'+faq_js+'</script>\n<script>'+js+'</script>\n</body>\n</html>\n'
open('/home/claude/dw-review/index.html','w',encoding='utf-8').write(out)
print(len(out))
