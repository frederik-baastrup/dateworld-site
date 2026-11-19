H=[]
def h(url,title,h1,lede,brands,picks,faq,seo,crumb=None,warn=None,choose=None,intro=None):
    H.append(dict(url=url,title=title,h1=h1,lede=lede,brands=brands,picks=picks,faq=faq,seo=seo,crumb=crumb or h1.split(':')[0],warn=warn,choose=choose,intro=intro))
h('/bedste-dating-apps/','Bedste dating apps 2026: sammenlign de populære apps – Dateworld','Bedste dating apps i 2026',
 'Swipe, prompts eller matchforslag? Vi har sammenlignet de dating apps, danskerne bruger mest, på pris, funktioner og hvem du møder.',
 ['tinder','hinge','bumble','dating','single','badoo','happn'],[('tinder','Flest brugere'),('hinge','Til noget seriøst'),('dating','Dansk med app')],
 [('Hvad er den bedste dating app?','Det afhænger af, hvad du søger. Tinder har flest brugere, Hinge er bygget til forhold, og Bumble lader kvinden skrive først. Vil du have en dansk tjeneste, har Dating.dk og Single.dk begge apps.'),('Er dating apps gratis?','De fleste dating apps er gratis at bruge, men tilbyder abonnementer med ekstra funktioner som ubegrænsede likes eller at se, hvem der har liket dig.'),('Hvilken dating app er bedst til et seriøst forhold?','Hinge og apps med personlighedsmatch som Single.dk er bygget til folk, der søger noget seriøst.')],
 [('Dating app eller datingside?','En dating app er bygget til mobilen og hurtige valg, mens en datingside giver plads til længere profiler og søgning. Mange danske datingsider har i dag også en app, så du kan få det bedste fra begge.'),('Sådan vælger du den rigtige app','Tænk over, hvad du søger, før du vælger. Vil du hurtigt i gang og møde mange, er en stor app med swipe et godt sted. Søger du et fast forhold, giver apps med prompts eller personlighedstest bedre samtaler.')],crumb='Bedste dating apps')
h('/gratis-dating/','Gratis dating 2026: datingsider du kan bruge gratis – Dateworld','Gratis dating: det får du uden at betale',
 'Næsten alle datingsider er gratis at oprette sig på, men hvad kan du egentlig uden at betale? Her er de sider og apps, hvor du kommer længst gratis.',
 ['tinder','dating','single','senior','badoo','hinge','sexhunt'],[('tinder','Gratis at matche og skrive'),('dating','Gratis profil og likes'),('senior','Gratis profil for 50+')],
 [('Findes der helt gratis datingsider?','Der findes gratis dating apps som Tinder, Badoo og Hinge, hvor du kan matche og skrive uden at betale. På de fleste danske datingsider er profilen gratis, men beskeder kræver et medlemskab.'),('Hvad kan jeg på en gratis profil?','Typisk kan du oprette en profil, se andre profiler, søge og like. Det er oftest beskederne, der kræver betaling.'),('Hvorfor koster datingsider penge?','Betalingen er med til at holde falske profiler væk og betale for kundeservice og godkendelse af profiler.')],
 [('Gratis oprettelse er ikke det samme som gratis dating','Når en datingside skriver "gratis oprettelse", betyder det sjældent, at alt er gratis. Tjek altid, om du kan læse og sende beskeder uden at betale, før du bruger tid på profilen.'),('Pas på automatisk fornyelse','Køber du et medlemskab for at prøve, så tjek, om det fornyes automatisk, og hvornår du senest skal opsige. Det står i tjenestens vilkår og i vores anmeldelser.')],crumb='Gratis dating')
h('/gratis-dating-apps/','Gratis dating apps 2026: de bedste apps uden at betale – Dateworld','Gratis dating apps',
 'Vil du date fra mobilen uden at betale? Her er de dating apps, hvor du kan matche og skrive gratis, og hvad du får ved at opgradere.',
 ['tinder','hinge','bumble','badoo','happn','grindr'],[('tinder','Flest brugere'),('hinge','Gratis at skrive'),('badoo','Gratis chat')],
 [('Hvilken dating app er helt gratis?','Tinder, Hinge, Bumble, Badoo og Happn kan alle bruges gratis til at matche og skrive. Abonnementerne giver ekstra funktioner.'),('Er gratis dating apps sikre?','Ja, når du bruger sund fornuft. Del ikke personlige oplysninger med det samme, og mød første gang et offentligt sted.')],
 [('Hvad koster det at opgradere?','De fleste apps har flere niveauer af abonnement. De giver typisk ubegrænsede likes, mulighed for at se, hvem der har liket dig, og at blive vist for flere.'),('Sådan får du mest ud af en gratis app','Brug gode billeder, skriv en kort og konkret profiltekst, og vær aktiv. Apps viser ofte aktive profiler for flere.')],crumb='Gratis dating apps')
h('/serioes-dating/','Seriøs dating 2026: de bedste sider til et fast forhold – Dateworld','Seriøs dating: find et fast forhold',
 'Er du færdig med swipe og søger noget, der holder? Her er de datingsider, der er bygget til singler, som vil finde en kæreste.',
 ['dating','single','be2','academic','singles50','senior'],[('dating','Bredest udvalg'),('single','Match på personlighed'),('be2','Personlighedstest')],
 [('Hvilken datingside er bedst til et seriøst forhold?','Sider med personlighedstest som Single.dk, be2 og Academic Singles er bygget til seriøse forhold. Dating.dk er et godt bredt valg med mange danske profiler.'),('Hvorfor betale for seriøs dating?','Betalte medlemskaber holder mange useriøse profiler væk, og det giver ofte mere engagerede medlemmer.')],
 [('Hvad kendetegner en seriøs datingside?','En seriøs datingside har som regel længere profiler, matchning ud fra personlighed eller værdier og godkendelse af profiler. Medlemmerne betaler ofte for at skrive, hvilket holder mange useriøse profiler væk.'),('Sådan viser du, at du er seriøs','Skriv ærligt i din profil, at du søger et forhold, og brug nye billeder, der ligner dig. Læs vores guide til den gode <a href="/dating-profiltekst/">profiltekst</a>.')],crumb='Seriøs dating')
h('/elitedating/','Elitedating 2026: datingsider for højtuddannede – Dateworld','Elitedating: dating for højtuddannede',
 'Betyder uddannelse og karriere meget for dig? Elitedating samler singler med lang uddannelse, der søger en partner på samme niveau.',
 ['academic','be2','single','dating'],[('academic','For højtuddannede'),('be2','Personlighedstest'),('single','Match på værdier')],
 [('Hvad er elitedating?','Elitedating er datingsider for singler med en videregående uddannelse eller en karriere, hvor de fleste søger et fast forhold.'),('Er elitedating snobbet?','Det handler mest om at finde en, der har samme hverdag og værdier. Mange oplever, at det er lettere at finde fælles fodslag.')],
 [('Sådan fungerer elitedating','De fleste sider til elitedating bruger en grundig personlighedstest, når du opretter dig. Ud fra dine svar får du matchforslag med personer, der passer til dig.')],crumb='Elitedating')
h('/netdating/','Netdating 2026: sådan kommer du i gang – Dateworld','Netdating: sådan finder du kærligheden online',
 'Netdating er blevet den mest almindelige måde at møde en partner på. Her er de bedste steder at starte og vores råd til at komme godt i gang.',
 ['dating','single','tinder','hinge','senior'],[('dating','Dansk og bred'),('tinder','Flest brugere'),('single','Match på personlighed')],
 [('Hvad er netdating?','Netdating er dating via internettet, enten på en datingside eller i en dating app.'),('Hvor starter jeg med netdating?','Start på en bred side med mange profiler som Dating.dk eller en app som Tinder, og find ud af, hvad der passer dig.')],
 [('Fordele ved netdating','Du kan møde mange flere, end du ville i hverdagen, og du kan læse om folk, før I mødes. Det er også lettere at finde nogen, der søger det samme som dig.'),('Gode råd til netdating','Vær ærlig i din profil, skriv personligt til andre, og mød hellere hurtigt end at skrive i ugevis. Mød første gang et offentligt sted.')],crumb='Netdating')
h('/tinder-alternativer/','Tinder alternativer 2026: de bedste apps og sider – Dateworld','Tinder alternativer',
 'Træt af endeløs swipe? Her er alternativerne til Tinder, uanset om du vil have mere seriøse samtaler eller en dansk tjeneste.',
 ['hinge','bumble','single','dating','happn','badoo'],[('hinge','Til noget seriøst'),('bumble','Kvinden skriver først'),('single','Dansk med personlighedsmatch')],
 [('Hvad er det bedste alternativ til Tinder?','Hinge er det mest populære alternativ, hvis du søger et forhold. Bumble er godt, hvis du vil have, at kvinden skriver først.'),('Findes der danske alternativer til Tinder?','Ja, Dating.dk og Single.dk er danske tjenester med apps.')],
 [('Hvorfor skifte fra Tinder?','Mange oplever, at Tinder er meget fokuseret på billeder og hurtige valg. Andre apps giver mere plads til personlighed og samtale.')],crumb='Tinder alternativer')
h('/dating-40-plus/','Dating 40+ 2026: de bedste datingsider for dig over 40 – Dateworld','Dating 40+',
 'Midt i livet ved du, hvad du vil have. Her er de datingsider, hvor du møder andre singler over 40, der søger det samme.',
 ['dating','single','be2','senior'],[('dating','Bredest udvalg'),('single','Match på personlighed'),('be2','Personlighedstest')],
 [('Hvilken datingside er bedst for 40+?','Dating.dk har mange profiler over 40. Søger du et fast forhold, er sider med personlighedstest et godt valg.'),('Er det for sent at date som 40-årig?','Slet ikke. Mange finder en ny partner efter 40, og netdating er en af de mest almindelige måder at gøre det på.')],
 [('Dating efter 40','Efter 40 har mange en skilsmisse, børn eller en travl karriere i bagagen. Det gør det vigtigt at finde en, der passer ind i den hverdag, du har nu. Læs også <a href="/hvordan-finder-man-en-kaereste-som-40-aarig/">hvordan man finder en kæreste som 40-årig</a>.')],crumb='Dating 40+')
h('/dating-50-plus/','Dating 50+ 2026: de bedste datingsider for dig over 50 – Dateworld','Dating 50+',
 'Er du over 50 og klar til at møde en ny? Her er de datingsider, hvor de andre er samme sted i livet som dig.',
 ['senior','singles50','dating','single'],[('senior','Kun 50+'),('singles50','Personlighedstest'),('dating','Bredest udvalg')],
 [('Hvilken datingside er bedst for 50+?','Senior.dk er kun for singler over 50 og koster 125 kr. for en måned. Singles50 er et godt valg, hvis du søger et fast forhold og vil matches på personlighed.'),('Er det gratis at date over 50?','Det er gratis at oprette en profil på de fleste sider, men for at skrive med andre kræver det typisk et medlemskab.')],
 [('Dating efter 50','Mange over 50 søger ikke kun en kæreste, men også en at rejse eller gå ture med. Sider som Senior.dk er derfor også mødesteder for venskaber. Læs også <a href="/hvordan-finder-man-en-kaereste-som-50-aarig/">hvordan man finder en kæreste som 50-årig</a>.')],crumb='Dating 50+')
h('/dating-60-plus/','Dating 60+ 2026: datingsider for dig over 60 – Dateworld','Dating 60+',
 'Det er aldrig for sent at finde kærligheden. Her er de datingsider, hvor du møder andre singler over 60.',
 ['senior','singles50','dating'],[('senior','Kun 50+'),('singles50','Personlighedstest'),('dating','Dansk og bred')],
 [('Hvor kan man date som 60-årig?','Senior.dk er kun for singler over 50, så mange medlemmer er over 60. Singles50 og Dating.dk er også gode muligheder.'),('Er det svært at date på nettet som 60+?','De fleste sider er lette at bruge, og kundeservice hjælper gerne. Start med at udfylde profilen roligt og tilføje et par gode billeder.')],
 [('Dating efter 60','Efter 60 handler dating ofte om selskab, fælles oplevelser og en at dele hverdagen med. Mange søger både kærlighed og venskab. Læs også <a href="/hvordan-finder-man-en-kaereste-som-60-aarig/">hvordan man finder en kæreste som 60-årig</a>.')],crumb='Dating 60+')
h('/dating-for-seniorer/','Dating for seniorer 2026: de bedste seniordatingsider – Dateworld','Dating for seniorer',
 'Seniordating handler om at finde en at dele hverdagen, rejserne og de gode stunder med. Her er de bedste steder at starte.',
 ['senior','singles50','dating'],[('senior','Kun 50+'),('singles50','Personlighedstest'),('dating','Bredest udvalg')],
 [('Hvad er den bedste datingside for seniorer?','Senior.dk er kun for singler over 50, og Singles50 matcher på personlighed. Begge er gode steder at starte.'),('Kan man finde venner på seniordatingsider?','Ja, især Senior.dk bruges også til at finde venner, rejsefæller og dansepartnere.')],
 [('Seniordating på nettet','Flere og flere seniorer bruger nettet til at møde nye mennesker. En side, der er bygget til seniorer, gør det lettere, fordi alle er samme sted i livet.')],crumb='Dating for seniorer')
h('/senior-dating/','Senior dating 2026: sammenlign datingsider for 50+ – Dateworld','Senior dating',
 'Sammenlign de datingsider, der er bygget til singler over 50, på pris, vilkår og hvem du møder.',
 ['senior','singles50','dating','single'],[('senior','Kun 50+'),('singles50','Personlighedstest'),('dating','Bredest udvalg')],
 [('Hvad koster senior dating?','Senior.dk koster 125 kr. for en måned og 250 kr. for tre måneder. Andre sider viser prisen efter oprettelse.'),('Hvilken senior datingside har flest medlemmer?','Senior.dk kalder sig Danmarks største mødested for alle over 50. De brede sider som Dating.dk har også mange medlemmer over 50.')],
 [('Sådan vælger du en senior datingside','Kig på, om siden kun er for seniorer, hvad du kan gratis, og om medlemskabet fornyes automatisk. Læs vores anmeldelser, før du vælger.')],crumb='Senior dating')
h('/dating-for-unge/','Dating for unge 2026: de bedste apps og sider – Dateworld','Dating for unge',
 'For de fleste unge foregår dating i en app. Her er de mest populære apps og sider, og hvad du skal være opmærksom på.',
 ['tinder','hinge','bumble','badoo','dating'],[('tinder','Flest unge brugere'),('hinge','Til noget seriøst'),('bumble','Kvinden skriver først')],
 [('Hvilken dating app bruger unge mest?','Tinder er den mest brugte app blandt unge, efterfulgt af Hinge og Bumble.'),('Hvor gammel skal man være for at date på nettet?','Alle de apps og sider, vi anmelder, kræver, at du er mindst 18 år.')],
 [('Gode råd til dating som ung','Del ikke for meget om dig selv i starten, og mød første gang et offentligt sted. Sig til en ven, hvor du er.')],crumb='Dating for unge')
h('/boesse-dating/','Bøsse dating 2026: de bedste apps og sider for homoseksuelle mænd – Dateworld','Bøsse dating',
 'Her er de apps og sider, hvor homoseksuelle mænd møder hinanden, uanset om du søger en kæreste eller noget uforpligtende.',
 ['grindr','tinder','hinge','dating'],[('grindr','Flest brugere'),('hinge','Til noget seriøst'),('tinder','Bredt udvalg')],
 [('Hvad er den bedste app til bøsse dating?','Grindr har flest brugere i målgruppen. Hinge og Tinder er gode, hvis du søger et forhold.'),('Kan man finde en kæreste på Grindr?','Det kan man godt, men mange bruger Grindr til uforpligtende møder. Hinge er bedre, hvis du søger et forhold.')],
 [('Sikker dating for homoseksuelle','Vær opmærksom på, hvilke oplysninger du deler, og mød første gang et offentligt sted. Brug appens funktioner til at blokere og anmelde.')],crumb='Bøsse dating')
h('/lesbisk-dating/','Lesbisk dating 2026: de bedste apps og sider – Dateworld','Lesbisk dating',
 'Her er de apps og sider, hvor kvinder, der søger kvinder, møder hinanden.',
 ['hinge','bumble','tinder','dating'],[('hinge','Til noget seriøst'),('bumble','Også til venner'),('tinder','Flest brugere')],
 [('Hvilken app er bedst til lesbisk dating?','Hinge og Bumble er populære, fordi de giver plads til samtaler. Tinder har flest brugere.'),('Kan man søge kvinder på Dating.dk?','Ja, du vælger selv, om du søger mænd eller kvinder.')],
 [('Sådan finder du en kæreste som lesbisk','Vær tydelig i din profil om, hvad du søger, og brug apps, hvor du selv kan filtrere på køn og orientering.')],crumb='Lesbisk dating')
h('/biseksuel-dating/','Biseksuel dating 2026: apps og sider – Dateworld','Biseksuel dating',
 'Som biseksuel kan du på de fleste apps vælge, om du vil se mænd, kvinder eller begge. Her er de bedste steder.',
 ['tinder','hinge','bumble','grindr','scor'],[('tinder','Vis både mænd og kvinder'),('hinge','Til noget seriøst'),('scor','Fræk dating')],
 [('Hvilke apps passer til biseksuelle?','Tinder, Hinge og Bumble lader dig se både mænd og kvinder. Scor.dk har plads til alle orienteringer.')],
 [('Vær tydelig i din profil','Skriv gerne, at du er biseksuel, og hvad du søger. Det sparer jer begge for misforståelser.')],crumb='Biseksuel dating')
h('/kristen-dating/','Kristen dating 2026: datingsider for kristne – Dateworld','Kristen dating',
 'Er tro en vigtig del af dit liv, er det rart at møde en, der deler den. Her er de steder, hvor kristne singler mødes.',
 ['dating','single','be2'],[('dating','Bredt udvalg'),('single','Match på værdier'),('be2','Personlighedstest')],
 [('Findes der kristne datingsider i Danmark?','Ja, der findes nichesider som Kristendate. Du kan også bruge brede sider og skrive i din profil, at troen betyder meget for dig.')],
 [('Kristen dating på almindelige sider','På sider med matchning på værdier, fx Single.dk, kan du gøre troen til en del af din profil og dine svar.')],crumb='Kristen dating')
h('/landmand-dating/','Landmand dating 2026: dating for landmænd – Dateworld','Landmand dating',
 'Lange arbejdsdage og langt til byen gør det svært at møde nogen. Her er de bedste muligheder for dating på landet.',
 ['dating','single','senior'],[('dating','Hele landet'),('single','Match på personlighed'),('senior','Hvis du er over 50')],
 [('Findes der datingsider for landmænd?','Ja, fx Farmerdating. Mange landmænd bruger også brede danske sider som Dating.dk, hvor du kan søge i hele landet.')],
 [('Dating på landet','Søg i en større radius, og skriv i din profil, hvordan din hverdag ser ud. Det tiltrækker dem, der kan se sig selv i livet på landet.')],crumb='Landmand dating')
h('/dating-for-handicappede/','Dating for handicappede 2026: gode råd og sider – Dateworld','Dating for handicappede',
 'Alle fortjener kærlighed. Her er gode råd og de datingsider, der er nemmest at bruge, uanset hvad du har med i bagagen.',
 ['dating','single','tinder'],[('dating','Dansk og bred'),('single','Match på personlighed'),('tinder','Flest brugere')],
 [('Skal jeg skrive om mit handicap i profilen?','Det bestemmer du selv. Mange vælger at nævne det kort, så de møder folk, der er åbne fra start.')],
 [('Find en, der ser dig','Matchning på personlighed og værdier gør det lettere at blive set for den, du er. Skriv om det, du brænder for.')],crumb='Dating for handicappede')
h('/dating-for-enlige-foraeldre/','Dating for enlige forældre 2026 – Dateworld','Dating for enlige forældre',
 'Med børn i hverdagen er tid en mangelvare. Her er de datingsider, hvor det er nemt at møde andre, der forstår livet som forælder.',
 ['nextlove','dating','single','senior'],[('nextlove','Kun for enlige forældre'),('dating','Bredest udvalg'),('single','Match på værdier')],
 [('Skal jeg skrive, at jeg har børn?','Ja. Det er en stor del af dit liv og sparer jer begge for skuffelser.'),('Hvornår skal en ny kæreste møde mine børn?','Tag det roligt, og vent til I er sikre på hinanden.')],
 [('Dating med børn','Planlæg dates, når børnene er hos den anden forælder eller passes, og vær ærlig om, hvor meget tid du har.')],crumb='Enlige forældre')
h('/find-bolleven/','Find en bolleven 2026: de bedste sider – Dateworld','Find en bolleven',
 'Søger du en fast, uforpligtende aftale? Her er de sider, hvor du finder andre, der vil det samme.',
 ['scor','sexhunt','erox','cdate','40plus'],[('scor','Validerede profiler'),('sexhunt','Gratis at prøve'),('cdate','Diskret')],
 [('Hvor finder man en bolleven?','På sider til sexdating som Scor.dk, Sexhunt.dk og Erox.dk, hvor alle ved, hvad de søger.'),('Hvordan undgår jeg falske profiler?','Vælg sider med validering, fx Scor.dk, og vær skeptisk over for profiler, der beder dig skifte app eller beder om penge.')],
 [('Hvad er en bolleven?','En bolleven er en, du har en fast, uforpligtende aftale med. Det kræver, at I er ærlige om forventningerne fra start.'),('Aftal reglerne','Tal om grænser, eksklusivitet og beskyttelse, før I mødes. Det gør det lettere for jer begge.')],crumb='Find en bolleven')
h('/utro-dating/','Utro dating 2026: diskrete sider til en affære – Dateworld','Utro dating',
 'Sider til diskret dating for folk i forhold. Her er de tjenester, der har mest fokus på anonymitet.',
 ['vm','cdate','scor'],[('vm','Mest fokus på anonymitet'),('cdate','Diskret'),('scor','Dansk')],
 [('Hvilken side bruges til affærer?','Victoria Milan er bygget til gifte og folk i forhold og har et anonymiseringsværktøj.'),('Står det på kontoudtoget?','Victoria Milan opkræves under navnet Digisecbilling. Tjek altid, hvordan betalingen vises.')],
 [('Diskretion','Brug en separat e-mail, og tjek, hvordan betalingen står på kontoudtoget. Vær opmærksom på, hvilke billeder du deler.')],crumb='Utro dating')
h('/swingerdating/','Swingerdating 2026: sider for par og swingere – Dateworld','Swingerdating',
 'Er I et par, der vil møde andre? Her er de danske sider, hvor par og swingere er velkomne.',
 ['scor','erox','sexhunt'],[('scor','Profiler for par'),('erox','Singler og par'),('sexhunt','Chatrooms')],
 [('Hvor finder man swingere?','På danske sider som Scor.dk, Erox.dk og Sexhunt.dk kan I oprette en parprofil.'),('Er swingerklubber et alternativ?','Ja, mange starter online og tager senere i klub.')],
 [('Kom godt i gang som swingerpar','Tal grundigt om grænser og regler, før I opretter profilen, og tag det i jeres eget tempo.')],crumb='Swingerdating')
h('/sugardating/','Sugardating 2026: hvad er det, og hvad skal du vide? – Dateworld','Sugardating',
 'Sugardating handler om forhold, hvor den ene part giver den anden økonomisk støtte eller gaver. Her er, hvad du bør vide, før du overvejer det.',
 [],[],
 [('Er sugardating lovligt?','At date og give gaver er lovligt. Bliver det betaling for sex, er det reguleret af lovgivningen om prostitution, og det kan have alvorlige konsekvenser.'),('Hvad er risikoen?','Svindel, afpresning og pres er kendte problemer. Del aldrig nøgenbilleder eller bankoplysninger med folk, du ikke kender.')],
 [('Hvad er sugardating?','Sugardating er en form for dating, hvor en ældre og mere velstående person, en sugardaddy eller sugarmommy, støtter en yngre person økonomisk eller med gaver.'),('Vær opmærksom','Grænsen mellem dating og betaling for sex kan blive uklar. Tænk dig godt om, og sæt tydelige grænser.')],crumb='Sugardating',warn='Vi anbefaler ikke specifikke sider til sugardating. Siden her er til information.')
H_extra=['/datingsider/','/sexdating/']
