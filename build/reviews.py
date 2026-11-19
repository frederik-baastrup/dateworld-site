import os,shutil
src=open('/home/claude/build/review.py',encoding='utf-8').read()
exec(compile(src[:src.index('H=[]')],'pre','exec'))
I['users2']=I['users']; I['gal']=ic('<rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m20.5 16-5-5-8 8"/>')
I['cam']=ic('<path d="M3.5 7.5h11v9h-11Z"/><path d="m14.5 10.5 6-3v9l-6-3"/>')
I['cal']=ic('<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 9.5h16M8.5 3v4M15.5 3v4"/>')
I['filter']=ic('<path d="M4 5h16l-6 7.5V19l-4-2v-4.5Z"/>')
I['id']=ic('<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 15.5c.6-1.3 1.7-2 3-2s2.4.7 3 2M14.5 10h3.5M14.5 13h3.5"/>')
def fmt(v): return '–' if v is None else ('%.1f'%v).replace('.',',')
R=[]
R.append(dict(slug='senior',n='Senior.dk',logo='logo-senior.webp',lw='76px',mw='52px',out='dw-senior',
 tag='Datingside og mødested kun for dig over 50.',meta='Læsetid ca. 6 min.',
 verdict='Et dansk mødested kun for singler over 50, med lav pris og plads til både kærlighed, venskab og fællesskab.',
 facts=[('Pris fra','125 kr. pr. md.'),('Gratis oprettelse','Ja'),('Målgruppe','Kun 50+'),('Søger','Kæreste, venner, rejsefælle'),('Kundeservice','Dansk')],
 price_short='Fra 125 kr. pr. md.',
 yes=['du er over 50 og vil møde folk samme sted i livet','du søger en kæreste, en ven, en dansepartner eller en rejsefælle','du vil have en lav pris og kan lide fællesskab med chat, events og forum'],
 no=['du er under 50','du vil skrive og læse beskeder uden at betale','du leder efter noget uforpligtende'],
 rates=[('Pris',4.4,'125 kr. for en måned, og prisen pr. måned falder, jo længere periode du køber.'),('Vilkår',3.4,'Prisen er offentlig, men vi har ikke kunnet finde regler for fornyelse og opsigelse uden at oprette en profil.'),('Funktioner',3.8,'Ud over søgning og breve er der chat, events og et stort debatforum.'),('Sikkerhed',3.6,'Kun for medlemmer over 50 og dansk kundeservice. Vi har ikke kunnet se, hvordan profiler godkendes.'),('Gennemsigtighed',3.8,'Firmaet svarer selv på Trustpilot og oplyser sine priser åbent.')],
 plans=[('1 måned','125 kr.','i alt','Ca. 4,20 kr. pr. dag.',False,''),('3 måneder','250 kr.','i alt','Svarer til ca. 83 kr. pr. måned.',True,'Bedste pris pr. måned'),('6 måneder','415 kr.','i alt','Svarer til ca. 69 kr. pr. måned. Oplyst af Senior.dk på Trustpilot.',False,'')],
 price_note='Priserne for 1 og 3 måneder står på Senior.dk. Prisen for 6 måneder har Senior.dk selv oplyst i et svar på Trustpilot. Tjek altid den aktuelle pris, før du betaler.',
 free='Det er gratis at oprette en profil, kigge rundt og søge blandt profilerne. Vil du skrive og læse breve, skal du være VIP. VIP giver fuld adgang til siden, som Senior.dk selv udtrykker det, for omkring 2,30 kr. om dagen.',
 feats=[('chat','Breve','Skriv og læs breve med andre medlemmer. Kræver VIP.'),('search','Søgning','Find profiler ud fra alder, område og interesser.'),('users','Chat og forum','Et stort debatforum og chat, hvor du kan møde andre uden at date.'),('cal','Events','Arrangementer, hvor du kan møde andre medlemmer i virkeligheden.')],
 who='Senior.dk er kun for singler over 50. Mange søger en kæreste, men siden er også et mødested for dig, der vil finde nye venner, en dansepartner eller en at rejse med. Det gør siden mere afslappet end mange andre datingsider.',
 safety=[('shield','Kun 50+','Medlemmerne er samme sted i livet, og yngre profiler bliver sorteret fra.'),('users','Dansk kundeservice','Du kan få hjælp på dansk, og firmaet svarer selv på anmeldelser.'),('info','Pas på kopisider','Senior.dk har selv advaret om udenlandske sider, der minder om deres. Opret dig kun via senior.dk.')],
 cancel=[('Gå til dit medlemskab','[Hvor du finder dit VIP-medlemskab, når du er logget ind.]'),('Stop fornyelsen','[Om VIP fornyes automatisk, og hvordan du stopper det.]'),('Slet profilen','[Hvor du sletter profilen under dine indstillinger.]')],
 cancel_note='Vi har ikke kunnet finde Senior.dk’s regler for fornyelse og opsigelse uden at oprette en profil. Tjek dem, før du køber VIP.',
 company='Senior.dk er en dansk datingside og kalder sig selv Danmarks største mødested for alle over 50 år.',
 alts=[('Dating.dk','logo-dating.webp','22px','Bred dansk datingside for alle aldre, hvis du vil have flere profiler at vælge imellem.'),('Singles50',None,None,'Matchning på personlighed for singler over 50, der søger et fast forhold.'),('Single.dk','logo-single.svg','14px','Matcher dig på personlighed, humor og værdier.')],
 qs=[('Hvad koster Senior.dk?','Et VIP-medlemskab koster 125 kr. for en måned og 250 kr. for tre måneder. Senior.dk har også oplyst en pris på 415 kr. for seks måneder.'),('Er Senior.dk gratis?','Det er gratis at oprette en profil, kigge rundt og søge. For at skrive og læse breve skal du være VIP.'),('Hvem kan bruge Senior.dk?','Siden er kun for dig, der er fyldt 50.'),('Kan jeg finde venner på Senior.dk?','Ja. Mange bruger siden til at finde en kæreste, men den er også et mødested for venskaber, rejsefæller og dansepartnere.')],
 concl='Senior.dk er et oplagt sted at starte, hvis du er over 50 og vil møde nogen, der er samme sted i livet. Prisen er lav, og siden er mere end en datingside med chat, forum og events. Tjek reglerne for fornyelse, før du betaler.',
 score=3.8,
 seo=[('Hvad er Senior.dk?','Senior.dk er en dansk datingside og et mødested for singler over 50. Her kan du lede efter en kæreste, men også efter venner, en dansepartner eller en rejsefælle. Det er gratis at oprette en profil, og et VIP-medlemskab giver adgang til at skrive og læse breve.'),('Senior dating på nettet','Det er lettere at finde et match, når de andre er samme sted i livet. Det er hele idéen bag Senior.dk: her skal du ikke sortere yngre profiler fra, og mange medlemmer kender livet efter skilsmisse, tab eller børn, der er flyttet hjemmefra.')],
))
R.append(dict(slug='scor',n='Scor.dk',logo=None,lw=None,mw=None,out='dw-scor',
 tag='Dansk side til sexdating for singler og par.',meta='Læsetid ca. 6 min. · Kun 18+',
 verdict='Danmarks ældste side til voksendating med åbne priser, ingen binding og krav om validering med MitID eller Yoti.',
 facts=[('Pris fra','83 kr. pr. md.'),('Gratis oprettelse','Ja'),('Binding','Nej'),('Validering','MitID eller Yoti'),('Online siden','1998')],
 price_short='Fra 83 kr. pr. md.',
 yes=['du søger noget frækt og vil være sikker på, at profilerne er validerede','du vil kunne opsige, når det passer dig','du er single eller søger sammen med en partner'],
 no=['du søger en kæreste på en almindelig datingside','du ikke vil validere dig med MitID eller Yoti','du vil skrive med andre uden at betale'],
 rates=[('Pris',3.6,'169 kr. for en måned er i den høje ende, men 12 måneder for 999 kr. svarer til 83 kr. pr. måned.'),('Vilkår',4.4,'Ingen binding, opsigelse når som helst på siden og mulighed for at sætte medlemskabet i bero.'),('Funktioner',3.6,'Profiler for singler og par, søgning og matchning. Vi har ikke set medlemsområdet.'),('Sikkerhed',4.4,'Alle nye profiler skal valideres med MitID eller Yoti, så alder og køn er tjekket.'),('Gennemsigtighed',4.4,'Priser, handelsbetingelser og firmaoplysninger ligger offentligt på siden.')],
 plans=[('1 måned','169 kr.','i alt','Godt til at prøve siden af.',False,''),('3 måneder','349 kr.','i alt','Svarer til ca. 116 kr. pr. måned.',False,''),('12 måneder','999 kr.','i alt','Svarer til ca. 83 kr. pr. måned.',True,'Billigst pr. måned')],
 price_note='Priserne står på Scor.dk. Alle medlemskaber tegnes som abonnement, der fornyes automatisk, men uden binding. Alle priser er inklusive moms.',
 free='Det er gratis at oprette en profil. Med et medlemskab får du ifølge Scor.dk fuld adgang til siden og ubegrænset kontakt med de andre profiler.',
 feats=[('users','Single eller par','Du vælger, om du søger alene eller sammen med en partner.'),('search','Søgning og matchning','Find profiler ud fra bl.a. orientering, civilstatus og område.'),('chat','Beskeder','Ubegrænset kontakt med andre profiler med et medlemskab.'),('pause','Pause','Medlemskabet kan sættes i bero, hvis du vil holde en pause.')],
 who='Scor.dk henvender sig til voksne singler og par, der søger noget frækt. Siden har været online siden 1998 og kalder sig selv Danmarks ældste voksen-datingsite. Alle skal være fyldt 18.',
 safety=[('id','Validering','Alle nye profiler skal valideres med MitID eller Yoti. Scor.dk oplyser, at CPR-nummeret ikke gemmes.'),('lock','Betaling','Betaling sker via betalingspartnere, så Scor.dk ikke håndterer dine kortoplysninger.'),('flag','Etiske regler','Siden har et etisk regelsæt for, hvordan medlemmerne skal behandle hinanden.')],
 cancel=[('Log ind og åbn medlemskab','Find dit medlemskab i profilmenuen.'),('Opsig abonnementet','Du kan opsige når som helst uden varsel, på siden eller via support.'),('Brug resten af perioden','Medlemskabet kører til udløbsdatoen. Allerede betalte perioder refunderes ikke.')],
 cancel_note='Abonnementet trækkes igen på udløbsdatoen omkring kl. 2 om natten, så opsig senest dagen før.',
 company='Scor.dk drives af SCOR ApS i Køge (CVR 24242986). Support kan kontaktes på telefon 7027 5959 mandag til torsdag kl. 10–16 og fredag kl. 10–14 eller via e-mail.',
 alts=[('Sexhunt.dk',None,None,'Dansk side til sexdating med chatrooms og kodebeskyttede gallerier.'),('Erox.dk',None,None,'Erotisk univers for singler og par med erotikfilter.'),('C-Date',None,None,'International side til diskrete, uforpligtende møder.')],
 qs=[('Hvad koster Scor.dk?','Et medlemskab koster 169 kr. for 1 måned, 349 kr. for 3 måneder og 999 kr. for 12 måneder.'),('Er der binding på Scor.dk?','Nej. Medlemskabet er et abonnement uden binding, som du kan opsige når som helst.'),('Skal jeg bruge MitID på Scor.dk?','Ja, nye profiler skal valideres med MitID eller Yoti. Ifølge Scor.dk bruges oplysningerne kun til at tjekke fødselsdag og køn.'),('Kan par bruge Scor.dk?','Ja, du kan vælge at oprette en profil sammen med en partner.')],
 concl='Scor.dk er et af de mest gennemsigtige valg til fræk dating: priserne er offentlige, der er ingen binding, og alle profiler er validerede. Til gengæld er en enkelt måned dyr, og du skal være klar til at validere dig med MitID eller Yoti.',
 score=4.1,
 seo=[('Hvad er Scor.dk?','Scor.dk er en dansk side til voksendating og sexdating for singler og par. Siden har været online siden 1998 og drives af SCOR ApS fra Køge. Det er gratis at oprette en profil, mens kontakt med andre kræver et medlemskab.'),('Sexdating med validerede profiler','Falske profiler er et kendt problem på sider til sexdating. Scor.dk kræver derfor, at alle nye profiler bliver valideret med MitID eller Yoti, så du ved, at alder og køn passer.')],
))
R.append(dict(slug='erox',n='Erox.dk',logo=None,lw=None,mw=None,out='dw-erox',
 tag='Dansk side til voksendating med erotisk univers.',meta='Læsetid ca. 5 min. · Kun 18+',
 verdict='Et erotisk univers for singler og par med diskrete profiler og erotikfilter. Prisen vises dog først, når du har oprettet dig.',
 facts=[('Pris','Vises efter oprettelse'),('Gratis oprettelse','Ja'),('Profiler','Over 300.000'),('Firma','Cyberfusion ApS'),('Kun for','18+')],
 price_short='Gratis oprettelse',
 yes=['du søger sexdating, en sexpartner eller noget helt tredje','du vil selv bestemme, hvad andre kan se om dig','du kan lide et erotisk univers med artikler og billeder'],
 no=['du vil kende prisen, før du opretter dig','du søger en kæreste på en almindelig datingside','du vil skrive med andre uden at betale'],
 rates=[('Pris',None,'Erox.dk viser ikke prisen offentligt, så vi kan ikke vurdere den.'),('Vilkår',2.8,'Vi har ikke kunnet finde regler for abonnement, fornyelse og opsigelse uden at oprette en profil.'),('Funktioner',3.8,'Diskrete profiler, erotikfilter, gallerier og artikler.'),('Sikkerhed',3.6,'Profiler gennemgås løbende, og visse typer indhold kræver kontrol af alder og identitet med MitID.'),('Gennemsigtighed',2.6,'Firma og regler er offentlige, men priser og opsigelse er det ikke.')],
 plans=None,
 price_note='Erox.dk viser ikke priserne, før du har oprettet en gratis profil. Andre sider nævner priser mellem 59 og 169 kr. pr. måned, men dem har vi ikke kunnet bekræfte. Tjek prisen og reglerne for fornyelse, før du betaler.',
 free='Det er gratis at oprette en profil og kigge rundt. Ifølge Erox.dk bestemmer du selv, hvad andre kan se om dig. Vil du skrive med andre, kræver det et betalt medlemskab.',
 feats=[('lock','Diskret profil','Du bestemmer selv, hvad andre kan se om dig.'),('filter','Erotikfilter','Slået til som standard, så du selv vælger, om du vil se erotiske billeder.'),('gal','Billeder og gallerier','Upload billeder, så længe de følger sidens regler.'),('pen','Artikler','Artikler om bl.a. swingere, affærer og sexdating.')],
 who='Erox.dk er for voksne singler og par, der søger en sexpartner, en bolleven, noget frækt eller måske en kæreste. Siden oplyser selv over 300.000 profiler. Du skal være fyldt 18.',
 safety=[('shield','Løbende gennemgang','Erox.dk gennemgår løbende profilerne for at holde siden fri for falske profiler og svindlere.'),('id','MitID ved visse indhold','Visse typer indhold kan først lægges op efter kontrol af alder og identitet med MitID.'),('flag','Faste regler','Det er bl.a. ikke tilladt at dele kontaktoplysninger i profilteksten eller at have mere end én profil.')],
 cancel=[('Log ind','[Hvor du finder dit medlemskab.]'),('Stop fornyelsen','[Om medlemskabet fornyes, og hvordan du stopper det.]'),('Slet profilen','[Hvor du sletter profilen.]')],
 cancel_note='Erox.dk oplyser ikke offentligt, hvordan du opsiger et medlemskab. Telefonnummeret på siden er ikke til support, så kontakt i stedet webmaster@erox.dk.',
 company='Erox.dk ejes af Cyberfusion ApS i Viborg (CVR 32269818), der også står bag Sexhunt.dk.',
 alts=[('Scor.dk',None,None,'Åbne priser, ingen binding og validering af alle profiler.'),('Sexhunt.dk',None,None,'Søstersiden fra samme firma med chatrooms og loger.'),('C-Date',None,None,'International side til diskrete, uforpligtende møder.')],
 qs=[('Hvad koster Erox.dk?','Erox.dk viser ikke prisen, før du har oprettet en gratis profil.'),('Er Erox.dk gratis?','Det er gratis at oprette en profil og kigge rundt. Det kræver et betalt medlemskab at skrive med andre.'),('Hvem står bag Erox.dk?','Siden ejes af Cyberfusion ApS i Viborg, som også står bag Sexhunt.dk.'),('Er profilerne på Erox.dk ægte?','Erox.dk oplyser, at de løbende gennemgår profilerne for at holde siden fri for falske profiler og svindlere. Brug altid sund fornuft, og anmeld profiler, der virker mistænkelige.')],
 concl='Erox.dk er et af de største danske steder til voksendating og giver dig god kontrol over, hvad andre ser. Det største minus er, at pris og opsigelse ikke er offentlige, så du skal oprette dig for at finde ud af, hvad det koster.',
 score=3.3,
 seo=[('Hvad er Erox.dk?','Erox.dk er en dansk side til voksendating og sexdating. Her kan singler og par finde en sexpartner, en bolleven eller noget helt tredje, og du kan være så anonym, som du vil. Siden ejes af Cyberfusion ApS i Viborg.'),('Erox.dk og Sexhunt.dk','Erox.dk og Sexhunt.dk er søstersider fra samme firma. De ligner hinanden på mange punkter, men har hver deres medlemmer og deres eget univers.')],
))
R.append(dict(slug='sexhunt',n='Sexhunt.dk',logo=None,lw=None,mw=None,out='dw-sexhunt',
 tag='Dansk side til sexdating for singler og par.',meta='Læsetid ca. 5 min. · Kun 18+',
 verdict='En dansk side til sexdating med chatrooms, loger og kodebeskyttede gallerier. Gratis at prøve, men VIP kræves for at skrive.',
 facts=[('Pris','Vises efter oprettelse'),('Gratis oprettelse','Ja'),('Skrive med andre','Kræver VIP'),('Firma','Cyberfusion ApS'),('Kun for','18+')],
 price_short='Gratis oprettelse',
 yes=['du vil prøve sexdating uden at betale fra start','du kan lide chatrooms og fællesskab','du vil styre, hvem der ser dine billeder'],
 no=['du vil kende prisen, før du opretter dig','du søger en kæreste','du vil skrive direkte med andre uden VIP'],
 rates=[('Pris',None,'Sexhunt.dk viser ikke prisen offentligt, så vi kan ikke vurdere den.'),('Vilkår',2.8,'Vi har ikke kunnet finde regler for fornyelse og opsigelse af VIP uden at oprette en profil.'),('Funktioner',4.0,'Chatrooms, private beskeder, SHOUT, loger og kodebeskyttede gallerier.'),('Sikkerhed',3.6,'Kun for voksne over 18, MitID ved visse typer indhold og mulighed for at anmelde falske profiler.'),('Gennemsigtighed',2.8,'Det er tydeligt, hvad du kan gratis, men ikke hvad VIP koster.')],
 plans=None,
 price_note='Sexhunt.dk viser ikke VIP-priserne, før du har oprettet en gratis profil. Andre anmeldelser nævner 99 kr. for en måned, men det har vi ikke kunnet bekræfte. Tjek prisen og reglerne for fornyelse, før du betaler.',
 free='Med en gratis profil kan du ifølge Sexhunt.dk se siden an, oprette et galleri og se, hvilke muligheder der er. For at skrive direkte med andre medlemmer skal du være VIP.',
 feats=[('chat','Chatrooms','Snak med andre medlemmer i fælles chatrum.'),('users','SHOUT og loger','Fællesskaber og opslag, hvor du kan finde ligesindede.'),('lock','Gallerier med kode','Del billeder i private gallerier, som kun dem med koden kan se.'),('pen','Private beskeder','Skriv direkte med andre. Kræver VIP.')],
 who='Sexhunt.dk henvender sig til voksne singler og par i Danmark, der søger en sexpartner eller noget frækt. Ifølge vilkårene skal alle brugere være fyldt 18 uden undtagelse.',
 safety=[('id','MitID ved visse indhold','Vil du lægge visse typer indhold op, skal du vise alder og identitet med MitID.'),('flag','Anmeld falske profiler','Du kan anmelde profiler, der virker falske, og det er ikke tilladt at have mere end én profil.'),('lock','Private gallerier','Dine billeder kan beskyttes med en kode, så kun dem, du giver koden, kan se dem.')],
 cancel=[('Log ind','[Hvor du finder dit VIP-medlemskab.]'),('Stop fornyelsen','[Om VIP fornyes, og hvordan du stopper det.]'),('Slet profilen','[Hvor du sletter profilen.]')],
 cancel_note='Sexhunt.dk oplyser ikke offentligt, om VIP fornyes af sig selv, eller hvordan du melder dig ud. Tjek det, før du køber.',
 company='Sexhunt.dk drives af Cyberfusion ApS i Viborg (CVR 32269818), der også står bag Erox.dk.',
 alts=[('Scor.dk',None,None,'Åbne priser, ingen binding og validering af alle profiler.'),('Erox.dk',None,None,'Søstersiden fra samme firma med erotikfilter og diskrete profiler.'),('C-Date',None,None,'International side til diskrete, uforpligtende møder.')],
 qs=[('Hvad koster Sexhunt.dk?','Sexhunt.dk viser ikke VIP-prisen, før du har oprettet en gratis profil.'),('Er Sexhunt.dk gratis?','Det er gratis at oprette en profil, se siden an og oprette et galleri. Det kræver VIP at skrive direkte med andre.'),('Hvem står bag Sexhunt.dk?','Siden drives af Cyberfusion ApS i Viborg, som også står bag Erox.dk.'),('Kan par bruge Sexhunt.dk?','Ja, siden henvender sig til både singler og par.')],
 concl='Sexhunt.dk er et godt bud, hvis du vil prøve sexdating gratis og kan lide chatrooms og fællesskab. Det trækker ned, at prisen og reglerne for opsigelse ikke er offentlige.',
 score=3.4,
 seo=[('Hvad er Sexhunt.dk?','Sexhunt.dk er en dansk side til sexdating for singler og par over 18. Det er gratis at oprette en profil, og et VIP-medlemskab giver adgang til at skrive direkte med andre. Siden drives af Cyberfusion ApS i Viborg.'),('Sexdating i chatrooms','Mange bruger Sexhunt.dk som et socialt sted med chatrooms, SHOUT og loger, hvor man kan lære andre at kende, før man skriver privat.')],
))
exec(open('/home/claude/build/rv_more.py',encoding='utf-8').read())
I['pause']=ic('<circle cx="12" cy="12" r="8.5"/><path d="M10 9v6M14 9v6"/>')
I['pen']=ic('<path d="M4 20h4L19 9l-4-4L4 16Z"/><path d="m13.5 6.5 4 4"/>')
I['brain']=ic('<circle cx="12" cy="12" r="8.5"/><path d="M9 10h.01M15 10h.01M8.5 14.5c1 1.3 2.2 2 3.5 2s2.5-.7 3.5-2"/>')
EXTRA='''.realshot{margin:0;border:1px solid var(--line);border-radius:6px;overflow:hidden;background:#F6F3F4}
.realshot img{display:block;width:100%;height:auto}
.realshot figcaption{padding:10px 14px;font-size:13px;color:var(--mute);background:#fff;border-top:1px solid var(--line)}
.warnbox{display:flex;gap:14px;padding:20px 22px;border:1px solid #E8B4B4;border-radius:6px;background:#FDF3F3}
.warnbox svg{flex:none;color:#B42318}
.warnbox p{margin:0!important}
.rlogo b{font-family:var(--head);font-size:18px;font-weight:600;color:var(--ink);text-align:center;line-height:1.1;padding:0 6px}
.mini .tl{display:grid;place-items:center;width:52px;height:52px;border-radius:6px;background:#F6F3F4;font-family:var(--head);font-size:11px;font-weight:600}
.mbar .tl{display:none}
.rate-top span.na{color:var(--mute)}'''
import sys
ONLY=sys.argv[1:]
for d in R:
    if ONLY and d['slug'] not in ONLY: continue
    n=d['n']; L=lambda: ('<img src="img/%s" alt="%s">'%(d['logo'],n)) if d['logo'] else '<b>%s</b>'%n
    hero='''<section class="rhero"><div class="glow" aria-hidden="true"></div><div class="wrap">
    <nav class="crumbs" aria-label="Brødkrummer"><a href="#">Forside</a><span>/</span><a href="#">Anmeldelser</a><span>/</span><span aria-current="page">%s</span></nav>
    <div class="rhero-grid"><div><div class="rlogo">%s</div><h1>%s anmeldelse</h1><p class="verdict">%s</p>
    <p class="meta"><span>%sOpdateret 19. november 2026</span><span>Af Dateworld-redaktionen</span><span>%s</span></p></div>
    <aside class="fact" aria-label="Fakta om %s"><div class="score"><b>%s</b><span>ud af 5<small>Vores samlede vurdering</small></span></div><dl>%s</dl>
    <a class="cta" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a><p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p></aside></div></div></section>'''%(n,L(),n,d['verdict'],I['clock'].replace('22','16'),d['meta'],n,fmt(d['score']),''.join('<div><dt>%s</dt><dd>%s</dd></div>'%f for f in d['facts']),n,ARW)
    toc=[('kort','Kort fortalt'),('forside','Sådan ser siden ud'),('vurdering','Vores vurdering'),('priser','Priser'),('gratis','Gratis eller betalt'),('funktioner','Funktioner'),('medlemmer','Hvem er på %s'%n),('sikkerhed','Sikkerhed'),('opsig','Opsig og slet profil'),('alternativer','Alternativer'),('faq','Spørgsmål og svar'),('konklusion','Konklusion'),('baggrund','Mere om %s'%n)]
    A=[]
    A.append('<section id="kort" class="blk"><h2>Kort fortalt</h2><div class="fit"><div class="fit-yes"><h3>Passer til dig, hvis …</h3><ul>%s</ul></div><div class="fit-no"><h3>Passer mindre godt, hvis …</h3><ul>%s</ul></div></div></section>'%(''.join('<li>%s%s</li>'%(CHK,t) for t in d['yes']),''.join('<li>%s%s</li>'%(MIN,t) for t in d['no'])))
    if d.get('warn'): A.append('<section id="vigtigt" class="blk"><div class="warnbox">%s<p><b>Vigtigt:</b> %s</p></div></section>'%(I['info'],d['warn']))
    if d.get('shot'): A.append('<section id="forside" class="blk"><h2>Sådan ser %s ud</h2><figure class="realshot"><img src="img/%s" alt="Forsiden på %s" loading="lazy"><figcaption>Forsiden på %s, %s.</figcaption></figure></section>'%(n,d['shot'],n,n,'november 2026'))
    A.append('<section id="vurdering" class="blk"><h2>Vores vurdering</h2><p class="lede">Vi vurderer ud fra fem områder: pris, vilkår, funktioner, sikkerhed og hvor åbent tjenesten fortæller om det hele. Vurderingen bygger på offentlige oplysninger. <a href="#om">Sådan vurderer vi</a></p><div class="rates">%s</div></section>'%''.join('<div class="rate"><div class="rate-top"><b>%s</b><span%s>%s</span></div><div class="rbar"><i style="width:%d%%"></i></div><p>%s</p></div>'%(a,'' if v is not None else ' class="na"',fmt(v) if v is not None else 'Ikke oplyst',(v or 0)*20,t) for a,v,t in d['rates']))
    pl=''
    if d['plans']: pl='<div class="plans">'+''.join('<div class="plan%s">%s<h3>%s</h3><p class="pm"><b>%s</b> %s</p><p class="tot">%s</p></div>'%(' best' if b else '','<span class="pbadge">%s</span>'%bd if b else '',a,p,per,t) for a,p,per,t,b,bd in d['plans'])+'</div>'
    A.append('<section id="priser" class="blk"><h2>Priser</h2>%s<div class="note">%s<p>%s</p></div></section>'%(pl,I['info'],d['price_note']))
    A.append('<section id="gratis" class="blk"><h2>Gratis eller betalt</h2><p>%s</p></section>'%d['free'])
    A.append('<section id="funktioner" class="blk"><h2>Funktioner</h2><div class="secs">%s</div></section>'%''.join('<div class="sc"><span class="fi">%s</span><div><h3>%s</h3><p>%s</p></div></div>'%(I[a],b,c) for a,b,c in d['feats']))
    A.append('<section id="medlemmer" class="blk"><h2>Hvem er på %s</h2><p>%s</p></section>'%(n,d['who']))
    A.append('<section id="sikkerhed" class="blk"><h2>Sikkerhed</h2><div class="secs">%s</div></section>'%''.join('<div class="sc"><span class="fi">%s</span><div><h3>%s</h3><p>%s</p></div></div>'%(I[a],b,c) for a,b,c in d['safety']))
    A.append('<section id="opsig" class="blk"><h2>Opsig og slet profil</h2><ol class="vsteps">%s</ol><div class="note">%s<p>%s</p></div></section>'%(''.join('<li><span class="n">%d</span><div><h3>%s</h3><p>%s</p></div></li>'%(i+1,a,b) for i,(a,b) in enumerate(d['cancel'])),I['info'],d['cancel_note']))
    A.append('<section id="alternativer" class="blk"><h2>Alternativer</h2><div class="alts">%s</div></section>'%''.join('<a class="alt" href="#"><span class="alg">%s</span><h3>%s</h3><p>%s</p><span class="rgo">Læs anmeldelsen %s</span></a>'%(('<img src="img/%s" alt="" style="height:%s">'%(f,h)) if f else '<b>%s</b>'%a,a,t,ARW) for a,f,h,t in d['alts']))
    A.append('<section id="faq" class="blk"><h2>Spørgsmål og svar</h2><div class="qa">%s</div></section>'%''.join('<details><summary><span>%s</span>%s</summary><p>%s</p></details>'%(q,PLUS,a) for q,a in d['qs']))
    A.append('<section id="konklusion" class="blk"><div class="concl"><div><h2>Konklusion</h2><p>%s</p></div><div class="concl-cta"><div class="score sm"><b>%s</b><span>ud af 5<small>Vores samlede vurdering</small></span></div><a class="cta light" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a><p class="adl"><span>Reklamelink</span></p></div></div></section>'%(d['concl'],fmt(d['score']),n,ARW))
    A.append('<section id="baggrund" class="blk bg"><h2>Mere om %s</h2><div class="bggrid"><div class="seo">%s<h3>Hvem står bag?</h3><p>%s</p></div></div></section>'%(n,''.join('<h3>%s</h3><p>%s</p>'%x for x in d['seo']),d['company']))
    A.append('<section id="om" class="blk om"><h2>Om anmeldelsen</h2><p>Anmeldelsen bygger på offentlige oplysninger: %s’s egen hjemmeside, priser, vilkår og hjælpesider, læst 19. november 2026. Vi har ikke oprettet en profil, så vi har ikke set medlemsområdet. Dateworld får betaling, hvis du opretter et medlemskab via vores links. Det påvirker ikke, hvad vi skriver. <a href="#">Sådan arbejder vi</a></p></section>'%n)
    mini=('<img src="img/%s" alt="">'%d['logo']) if d['logo'] else '<span class="tl">%s</span>'%n.replace('.dk','')
    side='<aside class="side"><div class="sticky"><div class="mini">%s<div><b>%s</b><span>%s</span></div></div><a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a><p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p><nav class="toc" aria-label="Indhold"><p>Indhold</p><ol>%s</ol></nav></div></aside>'%(mini,n,d['price_short'],n,ARW,''.join('<li><a href="#%s">%s</a></li>'%x for x in toc))
    main='<section class="rbody"><div class="wrap rgrid"><article class="rart">'+'\n'.join(A)+'</article>'+side+'</div></section>'
    mbar='<div class="mbar" id="mbar">%s<div><b>%s</b><span>%s · Reklamelink</span></div><a href="#" rel="sponsored nofollow">Besøg siden</a></div>'%(mini,n,d['price_short'])
    css=open('review.css',encoding='utf-8').read()+EXTRA
    js=open('review.js',encoding='utf-8').read()
    h2=head.replace('Dating.dk anmeldelse – Dateworld','%s anmeldelse 2026: pris, fordele og ulemper – Dateworld'%n)
    out=h2+'<style>'+css+'</style>\n'+top+'<main>'+hero+main+'</main>\n'+foot+'\n'+mbar+'\n<script>'+menu_js+'</script>\n<script>'+faq_js+'</script>\n<script>'+js+'</script>\n</body>\n</html>\n'
    od='/home/claude/'+d['out']; os.makedirs(od+'/img',exist_ok=True)
    for f in ['logo-dating.webp','logo-senior.webp','logo-single.svg']: shutil.copy('/home/claude/dw-list/img/'+f,od+'/img/'+f)
    if d.get('shot'): shutil.copy('/home/claude/shots/'+d['shot'],od+'/img/'+d['shot'])
    open(od+'/index.html','w',encoding='utf-8').write(out); print(d['out'],len(out))
