src=open('/home/claude/build/review.py',encoding='utf-8').read()
pre=src[:src.index('H=[]')]
exec(compile(pre.replace('Dating.dk anmeldelse – Dateworld','Sådan skriver du en god datingprofil (med eksempler) – Dateworld'),'pre','exec'))
I['pen']=ic('<path d="M4 20h4L19 9l-4-4L4 16Z"/><path d="m13.5 6.5 4 4"/>')
I['cam']=ic('<path d="M4 8h3l1.5-2h7L17 8h3v11H4Z"/><circle cx="12" cy="13" r="3.4"/>')
I['bulb']=ic('<path d="M9 17.5h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3Z"/>')
toc=[('kort','Kort fortalt'),('hvorfor','Derfor betyder profilen så meget'),('billeder','Vælg de rigtige billeder'),('tekst','Skriv en profiltekst, der skiller sig ud'),('eksempler','Eksempler på profiltekster'),('fejl','Det skal du undgå'),('tilpas','Tilpas profilen til siden'),('opdater','Hold profilen frisk'),('tjekliste','Tjekliste før du går live'),('faq','Spørgsmål og svar')]
hero='''<section class="rhero ghero">
  <div class="glow" aria-hidden="true"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Brødkrummer"><a href="#">Forside</a><span>/</span><a href="#">Guides</a><span>/</span><span aria-current="page">Datingprofil</span></nav>
    <p class="gkick">Guide · Din profil</p>
    <h1>Sådan skriver du en god datingprofil</h1>
    <p class="verdict">Din profil er det første, andre ser. Her får du konkrete råd til billeder og profiltekst, eksempler du kan lade dig inspirere af, og de fejl, der koster flest svar.</p>
    <p class="meta"><span>'''+I['clock'].replace('22','16')+'''Opdateret [DATO]</span><span>Af [NAVN]</span><span>Læsetid ca. 6 min.</span></p>
  </div>
</section>'''
A=[]
A.append('''<section id="kort" class="blk"><h2>Kort fortalt</h2>
  <ol class="gsum">'''+''.join('<li><span>%d</span><p>%s</p></li>'%(i+1,t) for i,t in enumerate(['Brug 3–5 nye billeder, hvor dit ansigt tydeligt kan ses, og mindst ét, der viser, hvad du laver.','Skriv konkret: fortæl om noget, du faktisk gør, frem for at liste egenskaber som "sjov" og "glad".','Slut med noget, der er let at svare på, så den anden har en grund til at skrive.']))+'''</ol>
</section>''')
A.append('''<section id="hvorfor" class="blk"><h2>Derfor betyder profilen så meget</h2>
  <p>På en datingside bladrer de fleste hurtigt. Et par sekunder på et billede, et blik på de første linjer af teksten, og så er de videre. Din profil skal derfor gøre to ting: fange opmærksomheden og give den anden en grund til at skrive.</p>
  <p>Det handler ikke om at virke så perfekt som muligt. En profil, der føles ægte og personlig, får som regel flere og bedre svar end en, der prøver at passe til alle. Jo tydeligere du er, desto lettere er det for de rigtige at finde dig, og for de forkerte at lade være.</p>
  <p>Tænk på profilen som en åbning til en samtale, ikke som et CV. Målet er ikke at fortælle alt om dig selv, men at gøre den anden nysgerrig nok til at sende den første besked.</p>
</section>''')
A.append('''<section id="billeder" class="blk"><h2>Vælg de rigtige billeder</h2>
  <p>Billederne afgør, om nogen overhovedet læser din tekst. Det vigtigste er, at de ligner dig, som du ser ud i dag. Vælg et hovedbillede, hvor du kigger mod kameraet i godt dagslys, og hvor du er alene på billedet.</p>
  <div class="gtips">'''+''.join('<div class="gt"><span class="fi">%s</span><h3>%s</h3><p>%s</p></div>'%(I[k],t,d) for k,t,d in [('cam','Hovedbillede','Ansigtet fylder, du smiler, og der er ingen solbriller.'),('users','Ét billede med andre','Gerne med venner, men så det er tydeligt, hvem du er.'),('match','Noget, du holder af','En tur i naturen, en koncert eller dit værksted giver noget at spørge ind til.')])+'''</div>
  <h3>Hvor mange billeder?</h3>
  <p>Tre til fem billeder er et godt udgangspunkt. Ét billede gør det svært at danne sig et indtryk, mens ti næsten ens selfies trækker ned. Vælg variation: et tydeligt portræt, et billede i hel figur og et eller to, der viser dig i gang med noget, du holder af.</p>
  <h3>Gamle billeder og filtre</h3>
  <p>Brug billeder, der er højst et par år gamle, og spring de kraftige filtre over. Det kan føles fristende at vælge det mest flatterende billede fra for fem år siden, men det skaber en skuffelse, når I mødes. Ærlige billeder giver dates, der starter på den rigtige fod.</p>
  <div class="note">'''+I['info']+'''<p><b>Tip:</b> Bed en ven tage billederne. Selfies taget fra lav vinkel eller i bilen virker sjældent så godt som et billede, en anden har taget.</p></div>
</section>''')
A.append('''<section id="tekst" class="blk"><h2>Skriv en profiltekst, der skiller sig ud</h2>
  <p>De fleste profiltekster ligner hinanden: "Jeg er glad, sjov og lige så glad for en aften på sofaen som en tur i byen." Det fortæller ikke noget. Skriv i stedet om konkrete ting, så den anden kan se dig for sig.</p>
  <p>Forskellen er stor. "Jeg elsker at rejse" står på tusindvis af profiler, mens "jeg har lige været i Lissabon og spist alt for mange pastel de nata" giver et billede af dig og et oplagt spørgsmål at stille. Det konkrete er både lettere at huske og lettere at svare på.</p>
  <ol class="gsteps">'''+''.join('<li><span class="n">%d</span><div><h3>%s</h3><p>%s</p></div></li>'%(i+1,t,d) for i,(t,d) in enumerate([('Start med noget konkret','Fx hvad du laver en typisk søndag, eller hvad du er i gang med lige nu.'),('Vis, hvad du søger','Skriv ærligt, om du søger en kæreste, en at gå ture med eller noget helt tredje.'),('Hold det kort','3–6 sætninger er nok. Resten kan I tale om, når I skriver sammen.'),('Giv en åbning','Slut med et spørgsmål eller en udfordring, der er let at svare på.')]))+'''</ol>
  <h3>Find den rigtige tone</h3>
  <p>Skriv, som du ville tale med en ny bekendt over en kop kaffe. Humor virker godt, hvis det falder dig naturligt, men tving det ikke. Hold tonen positiv: fortæl, hvad du gerne vil, frem for hvad du ikke gider. En profil fuld af krav og forbehold virker hurtigt afvisende, også selvom det ikke er meningen.</p>
  <h3>Vær ærlig om, hvad du søger</h3>
  <p>Søger du et fast forhold, så skriv det. Er du mest til en kop kaffe og en gåtur for at se, hvad det bliver til, så skriv det. Ærlighed fra start sparer jer begge for tid og misforståelser, og den tiltrækker dem, der søger det samme som dig.</p>
</section>''')
EX=[('Kort og konkret','Søndag morgen finder du mig på en løbetur langs havnen, og søndag aften laver jeg for meget mad. Jeg søger en, der gider gå med på begge dele. Skriv, hvis du har et bud på den bedste bager i byen.'),('Med humor','Jeg kan samle et IKEA-skab uden at skændes, men ikke uden at have en skrue til overs. Søger en kæreste, der griner af det samme som mig. Hvad er dit mest unyttige talent?'),('Til dig over 50','Børnene er flyttet hjemmefra, og jeg har fået tid til det, jeg har udskudt: rejser, havearbejde og en god bog. Jeg savner en at dele hverdagen og de små udflugter med.')]
A.append('''<section id="eksempler" class="blk"><h2>Eksempler på profiltekster</h2>
  <p>Brug eksemplerne som inspiration, ikke som skabelon. Den bedste tekst lyder som dig, så skift detaljerne ud med dine egne: dine vaner, dine interesser og det, du søger.</p>
  <div class="gex">'''+''.join('<figure><figcaption>%s</figcaption><blockquote>%s</blockquote></figure>'%(t,d) for t,d in EX)+'''</div>
</section>''')
A.append('''<section id="fejl" class="blk"><h2>Det skal du undgå</h2>
  <div class="fit">
    <div class="fit-yes"><h3>Gør sådan her</h3><ul>'''+''.join('<li>%s%s</li>'%(CHK,t) for t in ['Brug nye billeder, der ligner dig','Skriv om noget, du faktisk gør','Vær ærlig om, hvad du søger','Læs teksten højt, før du gemmer'])+'''</ul></div>
    <div class="fit-no"><h3>Undgå det her</h3><ul>'''+''.join('<li>%s%s</li>'%(MIN,t) for t in ['Gruppebilleder som hovedbillede','Lister med egenskaber som "sjov og spontan"','Krav til den anden, fx "ingen dramaqueens"','Snak om ekskæresten'])+'''</ul></div>
  </div>
</section>''')
picks=[('Dating.dk','logo-dating.webp','28px','Bredest udvalg'),('Senior.dk','logo-senior.webp','14px','Til dig over 50'),('Single.dk','logo-single.svg','12px','Match på personlighed')]
gcta='''<aside class="gcta"><div><h3>Klar til at prøve din nye profil?</h3><p>Det er gratis at oprette en profil hos de datingsider, vi anbefaler.</p></div><div class="gcta-l">'''+''.join('<a href="#" rel="sponsored nofollow"><span class="plg"><img src="img/%s" alt="" style="height:%s"></span><span><small>%s</small><b>%s</b></span>%s</a>'%(l,h,s,n,ARW) for n,l,h,s in picks)+'''</div><p class="adl"><span>Reklamelinks</span>Vi får betaling, hvis du opretter dig.</p></aside>'''
A.append('''<section id="tilpas" class="blk"><h2>Tilpas profilen til siden</h2>
  <p>Hvor meget tekst du skal skrive, afhænger af, hvor du dater. På en dating app, hvor man swiper, ser de fleste kun billederne og et par linjer, så her skal du være kort og præcis. På en klassisk datingside er der plads til mere, og mange læser hele profilen, før de skriver.</p>
  <p>Nogle sider, fx dem med personlighedstest, bruger dine svar til at foreslå matches. Brug tid på testen og svar ærligt. Forslagene bliver kun så gode som de svar, du giver.</p>
  <p>Er du over 50, er profilteksten ofte vigtigere end billederne. Her er det helt naturligt at skrive lidt om, hvor du er i livet, fx om børn, arbejde og hvad du gerne vil bruge din tid på fremover.</p>
</section>''')
A.append('''<section id="opdater" class="blk"><h2>Hold profilen frisk</h2>
  <p>En profil er ikke færdig, når du trykker gem. Får du få svar efter et par uger, så prøv at skifte hovedbillede eller omskrive de første linjer af teksten. Små ændringer kan gøre en stor forskel.</p>
  <p>Mange datingsider viser også nyligt opdaterede og aktive profiler højere oppe. Kig forbi jævnligt, svar på beskeder, og opdater billederne, når du har nogle nye, der viser dig fra en god side.</p>
</section>''')
A.append(gcta)
A.append('''<section id="tjekliste" class="blk"><h2>Tjekliste før du går live</h2>
  <ul class="gcheck">'''+''.join('<li>%s%s</li>'%(CHK,t) for t in ['Hovedbilledet viser tydeligt dit ansigt','Du har 3–5 billeder, der er under to år gamle','Teksten nævner mindst én konkret ting, du laver','Det står klart, hvad du søger','Der er ingen stavefejl','Teksten slutter med noget, der er let at svare på'])+'''</ul>
</section>''')
qs=[('Hvor lang skal en profiltekst være?','3–6 sætninger er nok for de fleste. Det vigtigste er, at teksten er konkret og giver den anden noget at skrive om.'),('Hvor mange billeder skal jeg have?','3–5 billeder er et godt udgangspunkt: et tydeligt hovedbillede, et helfigursbillede og et eller to, der viser, hvad du laver.'),('Skal jeg skrive, at jeg har børn?','Ja, hvis det betyder noget for dit liv og for, hvem du søger. Det sparer jer begge for skuffelser senere.'),('Hvad skriver jeg i den første besked?','Spørg ind til noget konkret fra den andens profil. Læs vores guide til <a href="#">den første besked</a>.')]
A.append('''<section id="faq" class="blk"><h2>Spørgsmål og svar</h2>
  <div class="qa">'''+''.join('<details><summary><span>%s</span>%s</summary><p>%s</p></details>'%(q,PLUS,a) for q,a in qs)+'''</div>
</section>''')
A.append('''<section class="blk gauthor"><div class="gav">[FOTO]</div><div><b>[NAVN]</b><p>[Én–to linjer om skribenten og Dateworld-redaktionen.]</p></div></section>''')
rel=[('Den første besked','Sådan skriver du en besked, der får svar.'),('Falske profiler','Sådan spotter du dem, før du bliver snydt.'),('Den første date','Idéer og råd til første møde.')]
related='''<section class="lsec lgray" id="relaterede"><div class="wrap"><div class="sec-head"><h2>Flere guides</h2><span class="rule" aria-hidden="true"></span></div><div class="grel">'''+''.join('<a class="gr" href="#"><span class="gimg">[BILLEDE]</span><small>Guide</small><h3>%s</h3><p>%s</p><span class="go">Læs guiden %s</span></a>'%(t,d,ARW) for t,d in rel)+'''</div></div></section>'''
side='''<aside class="side"><div class="sticky"><nav class="toc" aria-label="Indhold" style="margin-top:0;padding-top:0;border:0"><p>Indhold</p><ol>'''+''.join('<li><a href="#%s">%s</a></li>'%(a,b) for a,b in toc)+'''</ol></nav>
<div class="gside"><p>Vores anbefaling</p><div class="mini"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Gratis at oprette en profil</span></div></div><a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>'''+ARW+'''</i></a><p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p></div></div></aside>'''
main='<section class="rbody"><div class="wrap rgrid"><article class="rart">'+'\n'.join(A)+'</article>'+side+'</div></section>'
css=open('/home/claude/build/review.css',encoding='utf-8').read()+open('/home/claude/build/list.css',encoding='utf-8').read()+open('/home/claude/build/guide.css',encoding='utf-8').read()
js=open('/home/claude/build/review.js',encoding='utf-8').read()
out=head+'<style>'+css+'</style>\n'+top+'<main>'+hero+main+related+'</main>\n'+foot+'\n<script>'+menu_js+'</script>\n<script>'+faq_js+'</script>\n<script>'+js+'</script>\n</body>\n</html>\n'
open('/home/claude/dw-guide/index.html','w',encoding='utf-8').write(out)
print(len(out))
