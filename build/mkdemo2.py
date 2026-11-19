s=open('demo.py',encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
R("'Vælg på forsiden, om du er kvinde eller mand, og hvem du søger.'","'Vælg på forsiden, hvem du er, og hvem du søger.'")
R("'Angiv e-mail og en adgangskode. Ifølge Dating.dk tager det omkring 3 minutter.'","'Angiv e-mail og adgangskode. Dating.dk lover, at du er i gang på 3 minutter.'")
R('<p class="lede">Sådan ser de første trin ud på Dating.dk, fra forsiden til oprettelsen af dit login.</p>','<p class="lede">Det er gratis og hurtigt at oprette en profil. Sådan ser de første trin ud.</p>')
# første dage
R("'Du opretter dig, vælger hvem du søger, og skriver en kort profiltekst. [Om profilen skal godkendes, før andre kan se den.] Brug","'Du opretter dig, vælger hvem du søger, og skriver en kort profiltekst. Dine billeder bliver godkendt manuelt, så der kan gå lidt tid, før de er synlige. Brug")
R("'Søg på alder og område, gem de profiler, du synes om, og se, hvem der har kigget forbi din profil. Som gratis bruger kan du [hvad man kan uden medlemskab].'","'Søg på alder og område, like de profiler, du synes om, og prøv Singler i nærheden. Alt det kan du gratis, men du kan ikke se, hvem der har liket dig, eller hvem du har matchet med.'")
R("'Vil du skrive frit med andre, kræver det [et medlemskab]. Start","'Vil du læse dine beskeder og skrive frit med andre, kræver det en +PlusProfil. Start")
R("<p><b>Godt at vide:</b> [Én konkret ting, nye brugere ofte overser, fx at medlemskabet fornyes automatisk, eller at profiler uden billeder får færre svar.]</p>","<p><b>Godt at vide:</b> Introtilbuddet til 29 kr. har 84 dages binding og fortsætter derefter til 129 kr. pr. 4 uger. Vil du bare prøve, er engangsbetalingen uden fornyelse det sikre valg.</p>")
# gratis/betalt
i=s.index("feat=[('Oprette profil'");j=s.index("\n",i)
s=s[:i]+"feat=[('Oprette profil og uploade billeder',1,1),('Søge efter profiler',1,1),('Like andre profiler',1,1),('Singler i nærheden',1,1),('Bruge appen',1,1),('Se, hvem der har liket dig',0,1),('Se dine matches',0,1),('Læse beskeder',0,1),('Skrive frit til alle',0,1),('Blive vist oftere i søgninger',0,1)]"+s[j:]
R('<p class="lede">Det er gratis at oprette en profil, men nogle funktioner kræver medlemskab. Her er forskellen.</p>','<p class="lede">Det er gratis at oprette en profil og kigge sig omkring. Vil du se, hvem der er interesseret, og skrive sammen, kræver det en +PlusProfil.</p>')
# priser
i=s.index("plans=[('1 måned',False)");j=s.index("</section>''')",i)
s=s[:i]+'''plans=[('Introtilbud','29 kr.','første 4 uger','Derefter 129 kr. pr. 4 uger. 84 dages binding.',True,'Billigst at starte'),('Abonnement','129 kr.','pr. 4 uger','Fornyes automatisk. Kan også betales med MobilePay.',False,''),('Engangsbetaling','239 kr.','for 28 dage','Ingen fornyelse. Betales med kort.',False,'')]
art.append(\'\'\'<section id="priser" class="blk"><h2>Priser</h2>
  <p class="lede">Medlemskabet hedder +PlusProfil og fås i tre varianter. Priserne er fra Dating.dk's prisside, november 2026.</p>
  <div class="plans">\'\'\'+''.join('<div class="plan%s">%s<h3>%s</h3><p class="pm"><b>%s</b> %s</p><p class="tot">%s</p></div>'%(' best' if b else '','<span class="pbadge">%s</span>'%bd if b else '',n,p,per,t) for n,p,per,t,b,bd in plans)+\'\'\'</div>
  <div class="note">\'\'\'+I['info']+\'\'\'<p><b>Fornyes medlemskabet automatisk?</b> Ja, abonnementer fornyes automatisk, indtil du melder fra i betalingscentret, og fornyelsen sker et par timer før din profiltid udløber. Har du valgt et tilbud med binding, betaler du perioden ud, selv om du melder fra.</p></div>
'''+s[j:]
# funktioner
i=s.index("fs=[('search'");j=s.index("\n",i)
s=s[:i]+"fs=[('search','Søgning','Find profiler efter alder og område, og like dem, du synes om.'),('pin','Singler i nærheden','Se, hvem der er single tæt på dig lige nu.'),('match','Likes og matches','Se, hvem der har liket dig, og hvem du har matchet med (+PlusProfil).'),('chat','Beskeder','Læs og skriv beskeder til alle profiler med +PlusProfil.'),('users','Events','Singlearrangementer og temasider til fx Valentinsdag og Singles Day.'),('phone','App','Profil, beskeder, likes og anbefalinger i appen til iOS og Android.')]"+s[j:]
# medlemmer
R("'''<b>[ANTAL]</b><span>Aktive profiler</span>","'''<b>Siden 1998</b><span>En af de ældste danske datingsider</span>")
R("'''<b>[ALDER]</b><span>Flest medlemmer</span>","'''<b>18+</b><span>Alle aldre over 18 år</span>")
R("'''<b>Hele landet</b><span>[Flest i …]</span>","'''<b>Hele landet</b><span>Egne sider for de største byer</span>")
R('<p class="src">Kilde: Dating.dk, [DATO].</p>','<p class="src">Kilde: Dating.dk, november 2026.</p>')
R("<p>[2–3 sætninger om målgruppen ud fra Dating.dk's egne oplysninger: aldersspænd, hvad medlemmerne søger, og hvor i landet de bor.]</p>","<p>Dating.dk henvender sig bredt til singler i hele Danmark, der søger en kæreste eller nye bekendtskaber, og har egne sider for København, Aarhus, Odense, Aalborg og Esbjerg. Siden oplyser ikke et medlemstal, men fremhæver selv, at den har flest aktive profiler i nærheden af dig. Der er også en særskilt indgang til seniordating.</p>")
# app
R("<div><p>[Om appen findes til iOS og Android, hvad den kan, og om noget kun virker på hjemmesiden.]</p>","<div><p>Appen er gratis til både iPhone og Android og giver adgang til det samme som hjemmesiden: profil, beskeder, likes, matches og anbefalinger. Du kan købe +PlusProfil direkte i appen. I App Store har den 3,8 ud af 5 fra omkring 1.300 bedømmelser, og på Google Play er den hentet over 100.000 gange.</p>")
# sikkerhed
i=s.index("sec=[('shield'");j=s.index("\n",i)
s=s[:i]+"sec=[('shield','Manuel godkendelse','Profiler og billeder godkendes manuelt. Billeder skal være aktuelle og kun vise dig.'),('flag','Anmeld profiler','Anmeld mistænkelige profiler til kundeservice, som kan slette profiler og give karantæne.'),('chat','Dansk kundeservice','Kundeservice svarer alle ugens dage på kundeservice@dating.dk.'),('lock','18 år og privatliv','Du skal være mindst 18 år. Du kan altid trække dit samtykke tilbage ved at slette profilen.')]"+s[j:]
# opsig
i=s.index("op=[('Log ind'");j=s.index("\n",i)
s=s[:i]+"op=[('Log ind','Log ind på Dating.dk, og gå til betalingscentret.'),('Meld dig fra','Slå den automatiske fornyelse fra. Den profiltid, du allerede har betalt for, kan du bruge til den udløber.'),('Slet profilen','Vil du fjerne profilen helt, så slet den under dine indstillinger. Først da er den ikke længere synlig for andre.'),('Gem bekræftelsen','Gem din kvittering, indtil medlemskabet er udløbet, så du kan dokumentere, at du har meldt fra.')]"+s[j:]
R("<p><b>Tip:</b> Opsig medlemskabet mindst [X] dage før udløb, hvis du ikke vil fortsætte.</p>","<p><b>Tip:</b> Meld fra i god tid. Abonnementet fornyes et par timer før din profiltid udløber, så vent ikke til sidste dag.</p>")
# brugere
R("Tallene er hentet [DATO].</p>","Tallene er hentet november 2026.</p>")
R("<b>[x,x]</b><span class=\"uof\">ud af 5</span><small>[ANTAL] anmeldelser</small>","<b>3,6</b><span class=\"uof\">ud af 5</span><small>Ca. 3.500 anmeldelser</small>")
R("<span class=\"usrc\">App Store</span><b>[x,x]</b><span class=\"uof\">ud af 5</span><small>[ANTAL] bedømmelser</small>","<span class=\"usrc\">App Store</span><b>3,8</b><span class=\"uof\">ud af 5</span><small>Ca. 1.300 bedømmelser</small>")
R("<span class=\"usrc\">Google Play</span><b>[x,x]</b><span class=\"uof\">ud af 5</span><small>[ANTAL] bedømmelser</small>","<span class=\"usrc\">Google Play</span><b>100.000+</b><span class=\"uof\">downloads</span><small>Hentet over 100.000 gange</small>")
R("<li>[Typisk ros, med egne ord]</li><li>[Typisk ros]</li><li>[Typisk ros]</li>","<li>En overskuelig side, der er nem at finde rundt på</li><li>Mange seriøse profiler og gode chancer for at få kontakt</li><li>Hjælpsom kundeservice, der svarer hurtigt</li>")
R("<li>[Typisk klage, med egne ord]</li><li>[Typisk klage]</li>","<li>Man skal betale for at læse beskeder, og abonnementet fornyes automatisk</li><li>En del inaktive profiler og profiler uden billede</li>")
R('<p class="src">Opsummeret ud fra de [ANTAL] nyeste anmeldelser på Trustpilot, [DATO].</p>','<p class="src">Opsummeret ud fra anmeldelser på Trustpilot, november 2026. 86 % af anmeldelserne giver 4 eller 5 stjerner.</p>')
# faq
i=s.index("qs=[('Er Dating.dk gratis?'");j=s.index("\n",i)
s=s[:i]+"qs=[('Er Dating.dk gratis?','Det er gratis at oprette en profil, søge, like andre og bruge appen. Vil du se, hvem der har liket dig, læse beskeder og skrive frit, kræver det en +PlusProfil.'),('Hvad koster Dating.dk?','En +PlusProfil koster 129 kr. pr. 4 uger som abonnement eller 239 kr. for 28 dage som engangsbetaling. Nye brugere kan starte med 4 uger for 29 kr. mod 84 dages binding.'),('Hvordan sletter jeg min profil på Dating.dk?','Meld først fra i betalingscentret, så abonnementet ikke fornyes. Slet derefter profilen under dine indstillinger.'),('Har Dating.dk en app?','Ja, appen er gratis til både iPhone og Android og giver adgang til profil, beskeder, likes og matches.'),('Hvem bruger Dating.dk?','Singler i alle aldre over 18 år fra hele landet, som oftest søger en kæreste eller et seriøst forhold.')]"+s[j:]
# konklusion
R("<p>[2–3 sætninger: hvem Dating.dk passer bedst til, og hvad man skal være opmærksom på.]</p>","<p>Dating.dk er et godt sted at starte, hvis du søger en kæreste og vil have en dansk tjeneste med mange profiler, manuel godkendelse og kundeservice, der svarer. Vær opmærksom på, at du skal betale for at læse beskeder, og at introtilbuddet har binding.</p>")
R('<div class="score sm"><b>[4,2]</b>','<div class="score sm"><b>3,8</b>')
# seo
R("[2–3 sætninger om, hvornår siden startede, hvem der står bag, og hvilken målgruppe den henvender sig til.]","Siden har været online siden 1998 og drives af Dating.dk ApS fra Viborg, så den er en af de ældste datingsider herhjemme. Den henvender sig bredt til singler over 18 år i hele landet.")
R("[1–2 sætninger om prisniveau og perioder.]","Et abonnement koster 129 kr. pr. 4 uger, og nye brugere kan starte med 29 kr. for de første 4 uger mod binding.")
R("<p>[1–2 sætninger om, hvordan man logger ind, om man kan bruge Google eller Apple, og om der findes en app til iOS og Android.]</p>","<p>Du logger ind på dating.dk med din e-mail og adgangskode, og du kan bruge den samme profil i appen til iPhone og Android. Appen er gratis at hente, og du kan købe +PlusProfil direkte i den.</p>")
R("[2 sætninger om, hvad Dating.dk gør for at holde falske profiler ude, og hvordan man anmelder en profil.]","Dating.dk godkender profiler og billeder manuelt og afviser billeder, der ikke ser ægte ud. Ser du en mistænkelig profil, kan du anmelde den til kundeservice.")
R("[1–2 sætninger, der opsummerer brugernes bedømmelser med egne ord.]","De fleste brugere er tilfredse, især med hvor nem siden er, og med kundeservice. De mest kritiske anmeldelser handler om betaling for beskeder og automatisk fornyelse.")
R("<div><dt>Startet</dt><dd>[ÅR]</dd></div>","<div><dt>Startet</dt><dd>1998</dd></div>")
R("<div><dt>Ejer</dt><dd>[VIRKSOMHED]</dd></div>","<div><dt>Ejer</dt><dd>Dating.dk ApS</dd></div>")
R("<div><dt>Land</dt><dd>Danmark</dd></div>","<div><dt>Hovedsæde</dt><dd>Viborg</dd></div>")
R("brugernes anmeldelser [DATO].","brugernes anmeldelser i november 2026.")
R("<span>Fra [PRIS] pr. md.</span>","<span>Fra 129 kr. pr. 4 uger</span>")
R("<span>Fra [PRIS] pr. md. · Reklamelink</span>","<span>Fra 129 kr. pr. 4 uger · Reklamelink</span>")
# screenshots: tydeligere pladsholder
R("<small>[SKÆRMBILLEDE: %s]</small>","<small>Skærmbillede: %s</small>")
R("open('/home/claude/dw-review/index.html','w',encoding='utf-8')","open('/home/claude/dw-demo/index.html','w',encoding='utf-8')")
R("<title>Dating.dk anmeldelse – Dateworld</title>","<title>Dating.dk anmeldelse 2026 – Dateworld</title>")
open('demo.py','w',encoding='utf-8').write(s)
