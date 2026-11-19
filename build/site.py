import re,os,shutil,html as H_
exec(open('brands.py',encoding='utf-8').read())
exec(open('hubs.py',encoding='utf-8').read())
OUT='/home/claude/dateworld-site/public'
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT+'/img')
src=open('/home/claude/dw-page/index.html',encoding='utf-8').read()
HEAD=src[:src.index('</head>')]
TOP=src[src.index('</head>'):src.index('<section class="hero">')]
FOOT=src[src.index('<footer'):src.index('</footer>')+9]
SC=re.findall(r'<script>(.*?)</script>',src,re.S)
MENU_JS,FAQ_JS=SC[1],SC[3]
# ---------- URL map (label -> url)
U={'Bedste datingsider':'/datingsider/','Se alle datingsider':'/datingsider/','Datingsider':'/datingsider/','Bedste dating apps':'/bedste-dating-apps/','Gratis dating':'/gratis-dating/','Gratis dating apps':'/gratis-dating-apps/',
'Seriøs dating':'/serioes-dating/','Elitedating':'/elitedating/','Netdating':'/netdating/','Tinder-alternativer':'/tinder-alternativer/','Tinder alternativer':'/tinder-alternativer/',
'Dating for unge':'/dating-for-unge/','Dating 40+':'/dating-40-plus/','Dating 50+':'/dating-50-plus/','Dating 60+':'/dating-60-plus/','Dating for seniorer':'/dating-for-seniorer/','Senior dating':'/senior-dating/',
'Bøsse dating':'/boesse-dating/','Lesbisk dating':'/lesbisk-dating/','Biseksuel dating':'/biseksuel-dating/','Kristen dating':'/kristen-dating/','Landmand dating':'/landmand-dating/','Enlige forældre':'/dating-for-enlige-foraeldre/','Dating for handicappede':'/dating-for-handicappede/',
'Dating.dk eller Single.dk?':'/dating-dk-eller-single-dk/','Se sammenligningen':'/dating-dk-eller-single-dk/',
'Sexdating':'/sexdating/','Fræk dating':'/sexdating/','Se alt om fræk dating':'/sexdating/','Start med sammenligningen':'/sexdating/','Find en bolleven':'/find-bolleven/','Utro dating':'/utro-dating/','Sugardating':'/sugardating/','Swingerdating':'/swingerdating/',
'Se alle anmeldelser':'/anmeldelser/','Anmeldelser':'/anmeldelser/','Alle anmeldelser':'/anmeldelser/',
'Date ideer':'/date-ideer/','Find date ideer':'/date-ideer/','Tinder bio':'/tinder-bio/','Hvordan får man en kæreste?':'/hvordan-faar-man-en-kaereste/','Første date':'/foerste-date/','Den første date':'/foerste-date/','Spørgsmål til daten':'/spoergsmaal-til-date/','Date ideer hjemme':'/date-ideer-hjemme/',
'Dating profiltekst':'/dating-profiltekst/','profiltekst':'/dating-profiltekst/','Kan han lide mig?':'/kan-han-lide-mig/','10 tegn på, at han er vild med dig':'/10-tegn-paa-at-han-er-vild-med-dig/','Kærestesorg':'/kaerestesorg/','Se alle guides':'/artikler/','Alle guides':'/artikler/','Guides':'/artikler/',
'Om Dateworld':'/om-os/','Om os':'/om-os/','Sådan arbejder vi':'/saadan-arbejder-vi/','Sådan tjener vi penge':'/saadan-arbejder-vi/','Sådan vurderer vi':'/saadan-arbejder-vi/','Kontakt':'/om-os/#kontakt','Cookies og privatliv':'/privatlivspolitik/','Privatlivspolitik':'/privatlivspolitik/','Forside':'/',
'Dating apps':'/datingapps/','Datingformer':'/datingformer/','Den første besked':'/artikler/','Falske profiler':'/artikler/'}
REV={}
for k,b in B.items(): U[b['n']]=b['url']; REV[b['n']]=b['url']
EXTRA_REV={'Dating.dk':'/dating-dk-anmeldelse/','Scor':'/scor-dk-anmeldelse/','40plus.dk':'/40plus-dk-anmeldelse/','Nextlove':'/nextlove-anmeldelse/','iDates':'/idates-anmeldelse/','Only-flirts':'/only-flirts-anmeldelse/','Meet-n-Hook':'/meet-n-hook-anmeldelse/','Swirvy Date':'/swirvy-date-anmeldelse/'}
U.update(EXTRA_REV); REV.update(EXTRA_REV)
U.update({'LGBT+ dating':'/boesse-dating/','Siden indeholder affiliatelinks':'/saadan-arbejder-vi/','Læs, hvordan vi arbejder':'/saadan-arbejder-vi/','Sikker netdating':'/artikler/','Læs anmeldelserne':'/anmeldelser/','sammenligning af datingsider':'/datingsider/','guides til dating':'/artikler/','dating app':'/bedste-dating-apps/','anmeldelser af datingsider':'/anmeldelser/','Sammenlign datingsider':'/datingsider/','Se forslag':None,'swingere':'/swingerdating/','swingerklub':'/swingerdating/','falske profiler':'/artikler/','Du søger en kæreste':'/datingsider/'})
UL={k.lower():v for k,v in U.items() if v}
AFF={}  # brand name -> affiliate url (fase 4)
def strip(s): return re.sub(r'\s+',' ',H_.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def fix_links(p):
    def rep(m):
        a,inner=m.group(1),m.group(2); t=strip(inner)
        if 'sponsored' in a:
            for n in sorted(REV,key=len,reverse=True):
                if n in t: return '<a'+a.replace('href="#"','href="%s"'%AFF.get(n,'#'))+'>'+inner+'</a>'
            return m.group(0)
        url=UL.get(t.lower())
        if not url:
            hm=re.search(r'<(h3|h2|b|strong)[^>]*>(.*?)</\1>',inner,re.S)
            if hm: url=UL.get(strip(hm.group(2)).lower()) or REV.get(strip(hm.group(2)))
        if not url:
            for n in sorted(REV,key=len,reverse=True):
                if n in t and ('anmeld' in t.lower() or len(t)<=len(n)+2): url=REV[n];break
        if not url and ('Læs anmeldelsen' in t or 'Læs guiden' in t):
            ctx=strip(m.string[max(0,m.start()-3000):m.start()])
            best=None;bi=-1
            for n in REV:
                i=ctx.rfind(n)
                if i>bi: bi=i;best=n
            if best: url=REV[best]
        return '<a'+a.replace('href="#"','href="%s"'%url)+'>'+inner+'</a>' if url else m.group(0)
    return re.sub(r'<a([^>]*href="#"[^>]*)>(.*?)</a>',rep,p,flags=re.S)
UJS='var U='+__import__('json').dumps(U,ensure_ascii=False)+';function uu(t){return U[t]||"#";}'
MENU2=MENU_JS.replace("'<a href=\"#\"><span class=\"sico\">'+(I[s[2]]||esc(s[2]))","'<a href=\"'+uu(s[0])+'\"><span class=\"sico\">'+(I[s[2]]||esc(s[2]))")
MENU2=MENU2.replace("return '<a href=\"#\">'+esc(t)+'</a>';","return '<a href=\"'+uu(t)+'\">'+esc(t)+'</a>';")
MENU2=MENU2.replace("' <a href=\"#\">'+esc(p.foot[1])","' <a href=\"'+uu(p.foot[1])+'\">'+esc(p.foot[1])")
MENU2=MENU2.replace("'</span><a href=\"#\">'+esc(p.foot[2])","'</span><a href=\"'+uu(p.foot[2])+'\">'+esc(p.foot[2])")
MENU2=MENU2.replace("return '<a href=\"#\"><span class=\"ico\">'","return '<a href=\"'+(U[c[2]]||U[c[1]]||'#')+'\"><span class=\"ico\">'")
MENU2=MENU2.replace("return '<a class=\"cat\" href=\"#\">","return '<a class=\"cat\" href=\"'+(U[c[1]]||'#')+'\">")
U.update({'Flirt og fræk dating':'/sexdating/','Bøsse og lesbisk dating':'/boesse-dating/','Gratis at starte':'/gratis-dating/'})
UJS='var U='+__import__('json').dumps(U,ensure_ascii=False)+';function uu(t){return U[t]||"#";}'
MENU2=UJS+MENU2
assert MENU2.count('uu(')>=5, MENU2.count('uu(')
def finish(p,title=None,desc=None,canon=None):
    p=re.sub(r'<script>(?:(?!</script>).)*?var panels=.*?</script>',lambda m:'<script>'+MENU2+'</script>',p,flags=re.S)
    p=re.sub(r'(src|href)="img/',r'\1="/img/',p)
    p=re.sub(r"url\((['\"]?)img/",r"url(\1/img/",p)
    if title: p=re.sub(r'<title>.*?</title>','<title>%s</title>'%title,p,count=1)
    if desc:
        p=re.sub(r'<meta name="description"[^>]*>','',p)
        p=p.replace('</title>','</title>\n<meta name="description" content="%s">'%H_.escape(desc,quote=True),1)
    if canon: p=p.replace('</title>','</title>\n<link rel="canonical" href="https://dateworld.dk%s">'%canon,1)
    p=p.replace('class="logo" href="#"','class="logo" href="/"')
    return fix_links(p)
PAGES={}
def put(url,p,title=None,desc=None):
    d=OUT+url; os.makedirs(d,exist_ok=True)
    open(d+'index.html','w',encoding='utf-8').write(finish(p,title,desc,url)); PAGES[url]=title
def copy_imgs(folder):
    if os.path.isdir(folder+'/img'):
        for f in os.listdir(folder+'/img'): shutil.copy(folder+'/img/'+f,OUT+'/img/'+f)
def ic(d,w=22,sw=1.5): return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%(w,w,sw,d)
ARS='<svg aria-hidden="true" width="18" height="18" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11h14M12.5 5.5 18 11l-5.5 5.5"/></svg>'
CHK=ic('<circle cx="12" cy="12" r="9"/><path d="m8 12.3 2.6 2.6L16 9.4"/>',20)
MIN=ic('<circle cx="12" cy="12" r="9"/><path d="M8.5 12h7"/>',20)
INFO=ic('<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8h.01"/>')
PLUS='<svg aria-hidden="true" width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M11 4v14M4 11h14"/></svg>'
FI={'pris':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.6 2.5H13.5v4.9L7.4 13.5 2.5 8.6Z"/><circle cx="10.6" cy="5.4" r=".9"/></svg>','op':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="5.6"/><path d="m5.6 8.1 1.7 1.7 3.2-3.4"/></svg>','app':'<svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="2" width="7" height="12" rx="1.6"/><path d="M7.3 11.6h1.4"/></svg>'}
CSS='.plg b{font-family:var(--head);font-size:11px;font-weight:600;text-align:center;line-height:1.1;padding:0 4px}'+''.join(open(f,encoding='utf-8').read() for f in ['review.css','list.css','guide.css','fraek.css'])+'.warnbox{display:flex;gap:14px;padding:20px 22px;border:1px solid #E8B4B4;border-radius:6px;background:#FDF3F3;margin-bottom:28px}.warnbox svg{flex:none;color:#B42318}.warnbox p{margin:0}.ovgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.ov{display:flex;flex-direction:column;padding:22px 22px 18px;border:1px solid var(--line);border-radius:6px;background:#fff;transition:border-color .15s}.ov:hover{border-color:#CFC4C9}.ov small{font-family:var(--text);font-size:12px;font-weight:600;color:var(--accent-d)}.ov h3{margin:6px 0 6px;font-family:var(--head);font-size:20px;font-weight:500}.ov p{margin:0 0 14px;font-size:14.5px;color:var(--mute)}.ov .go{margin-top:auto;display:inline-flex;gap:6px;align-items:center;font-family:var(--text);font-size:14px;font-weight:600}.pg{max-width:780px}.pg h2{font-family:var(--head);font-weight:500;font-size:28px;margin:40px 0 12px}.pg p,.pg li{font-size:17px;line-height:1.7;color:#4F4148}@media (max-width:900px){.ovgrid{grid-template-columns:1fr}}'
LJS=open('list.js',encoding='utf-8').read()
def shell(main,title):
    return HEAD+'<style>'+CSS+'</style>\n'+TOP+'<main>'+main+'</main>\n'+FOOT+'\n<script>'+MENU_JS+'</script>\n<script>'+FAQ_JS+'</script>\n<script>'+LJS+'</script>\n</body>\n</html>\n'
def lg(b,h=None):
    if b.get('logo'): return '<img src="img/%s" alt="" style="height:%s">'%(b['logo'],h or b.get('lh','30px'))
    return '<b>%s</b>'%b['n']
def cf(k,lab,v): return '<div class="cfact"><small>%s%s</small><b>%s</b></div>'%(FI[k],lab,v)
def crumbs(c): return '<nav class="crumbs" aria-label="Brødkrummer"><a href="/">Forside</a><span>/</span><span aria-current="page">%s</span></nav>'%c
def faqsec(qs,lede='Det, de fleste spørger om.'):
    return '<section class="lsec" id="faq"><div class="wrap faq-grid"><div><h2 class="lh2">Spørgsmål og svar</h2><p class="lede">%s</p></div><div class="qa">%s</div></div></section>'%(lede,''.join('<details%s><summary><span>%s</span>%s</summary><p>%s</p></details>'%(' open' if i==0 else '',q,PLUS,a) for i,(q,a) in enumerate(qs)))
def hub(c):
    bs=[B[k] for k in c['brands']]
    picks=''.join('<a href="#s-%s"><span class="plg">%s</span><span><small>%s</small><b>%s</b></span>%s</a>'%(k,lg(B[k],'16px' if not B[k].get('logo') else None),lab,B[k]['n'],ARS) for k,lab in c['picks'])
    aside='<aside class="picks" aria-label="Vores bud"><p class="picks-h">Vores bud</p>%s<p class="adl"><span>Reklame</span>Vi får betaling, hvis du opretter dig via vores links.</p></aside>'%picks if picks else ''
    hero='<section class="rhero lhero"><div class="glow" aria-hidden="true"></div><div class="wrap">%s<div class="rhero-grid"><div><h1>%s</h1><p class="verdict">%s</p><p class="meta"><span>Opdateret 19. november 2026</span><span>Af Dateworld-redaktionen</span>%s</p></div>%s</div></div></section>'%(crumbs(c['crumb']),c['h1'],c['lede'],'<span>%d tjenester sammenlignet</span>'%len(bs) if bs else '',aside)
    body=hero
    if c.get('warn'): body+='<section class="lsec" style="padding-bottom:0"><div class="wrap"><div class="warnbox">%s<p>%s</p></div></div></section>'%(INFO,c['warn'])
    if bs:
        rows=''.join('<article class="tr%s">%s<span class="no">%d</span><span class="lg">%s</span><div class="nm"><h3>%s</h3><p>%s</p><div class="chips">%s</div></div><div class="cfacts">%s%s%s</div><div class="act"><a class="visit" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a><div class="under"><span>Reklamelink</span><a href="%s">Læs anmeldelsen</a></div></div></article>'%(' top' if i==0 else '','<span class="pick-tab">Vores anbefaling</span>' if i==0 else '',i+1,lg(b),b['n'],b['sub'],''.join('<span>%s</span>'%x for x in b['chips']),cf('pris','Pris fra',b['price']),cf('op','Gratis oprettelse',b['free']),cf('app','App',b['app']),b['n'],ARS,b['url']) for i,b in enumerate(bs))
        body+='<section class="cmp lsec" id="oversigt"><div class="wrap"><div class="sec-head"><h2>Sammenlign</h2><span class="rule" aria-hidden="true"></span></div><div class="cmp-top"><p class="cmp-lede">Rangeret ud fra vores samlede vurdering af de tjenester, vi har gennemgået.</p></div><div class="tbl">%s</div><p class="cmp-note">Knapperne fører til tjenestens egen side. Priserne er tjenestens egne, senest tjekket november 2026.</p></div></section>'%rows
        cards=''.join('''<article class="lcard" id="s-%s"><div class="lc-head"><span class="lc-no">%d</span><span class="lc-lg">%s</span><div class="lc-t"><h3>%s</h3><div class="chips">%s</div></div><div class="lc-score"><b>%s</b><span>ud af 5</span></div></div><p class="lc-txt">%s</p><div class="lc-pc"><div><h4>%sFordele</h4><ul>%s</ul></div><div><h4>%sUlemper</h4><ul>%s</ul></div></div><div class="lc-foot"><dl><div><dt>Pris fra</dt><dd>%s</dd></div><div><dt>Gratis oprettelse</dt><dd>%s</dd></div><div><dt>App</dt><dd>%s</dd></div></dl><div class="lc-act"><a class="read" href="%s">Læs anmeldelsen</a><a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg %s</span><i>%s</i></a></div></div></article>'''%([k for k in c['brands']][i],i+1,lg(b),b['n'],''.join('<span>%s</span>'%x for x in b['chips']),b['score'],b['txt'],CHK,''.join('<li>%s</li>'%x for x in b['pros']),MIN,''.join('<li>%s</li>'%x for x in b['cons']),b['price'],b['free'],b['app'],b['url'],b['n'],ARS) for i,b in enumerate(bs))
        body+='<section class="lsec lgray" id="gennemgang"><div class="wrap"><div class="sec-head"><h2>Gennemgang</h2><span class="rule" aria-hidden="true"></span></div><div class="lcards">%s</div></div></section>'%cards
    body+=faqsec(c['faq'])
    seo=c['seo']; half=(len(seo)+1)//2
    body+='<section class="prose" id="mere"><div class="wrap"><h2>%s: det skal du vide</h2><div class="prose-cols"><div>%s</div><div>%s</div></div></div></section>'%(c['crumb'],''.join('<h3>%s</h3><p>%s</p>'%x for x in seo[:half]),''.join('<h3>%s</h3><p>%s</p>'%x for x in seo[half:]))
    body+='<section class="lsec"><div class="wrap"><div class="lom"><h2>Om denne side</h2><p>Vi sammenligner de tjenester, vi har gennemgået, ud fra deres hjemmesider, priser, vilkår og brugernes anmeldelser. Dateworld får betaling, hvis du opretter et medlemskab via vores links. Det påvirker ikke rækkefølgen eller det, vi skriver. <a href="/saadan-arbejder-vi/">Sådan arbejder vi</a></p></div></div></section>'
    return shell(body,c['title'])
for c in H: put(c['url'],hub(c),c['title'],c['lede'][:155])
def simple(url,title,h1,lede,inner,crumb=None,desc=None):
    body='<section class="rhero"><div class="glow" aria-hidden="true"></div><div class="wrap">%s<h1>%s</h1><p class="verdict">%s</p></div></section><section class="lsec"><div class="wrap"><div class="pg">%s</div></div></section>'%(crumbs(crumb or h1),h1,lede,inner)
    put(url,shell(body,title),title,desc or lede[:155])
def ovpage(url,title,h1,lede,items,crumb=None):
    inner='<div class="ovgrid">'+''.join('<a class="ov" href="%s"><small>%s</small><h3>%s</h3><p>%s</p><span class="go">%s %s</span></a>'%(u,k,t,d,g,ARS) for k,t,d,u,g in items)+'</div>'
    body='<section class="rhero"><div class="glow" aria-hidden="true"></div><div class="wrap">%s<h1>%s</h1><p class="verdict">%s</p></div></section><section class="lsec"><div class="wrap">%s</div></section>'%(crumbs(crumb or h1),h1,lede,inner)
    put(url,shell(body,title),title,lede[:155])
# ---- copy existing builds
SRC=[('/', '/home/claude/dw-page','Dateworld – sammenlign datingsider, dating apps og fræk dating','Find den rigtige datingside. Vi sammenligner pris, vilkår og funktioner hos danske datingsider og dating apps.'),
('/datingsider/','/home/claude/dw-list','Datingsider 2026: de bedste datingsider i Danmark – Dateworld','Sammenlign de bedste datingsider i Danmark på pris, vilkår og funktioner, og find den, der passer til dig.'),
('/sexdating/','/home/claude/dw-fraek','Sexdating 2026: de bedste sider til fræk dating – Dateworld','Sammenlign de danske sider til sexdating og fræk dating på pris, diskretion og hvem der er på dem.'),
('/dating-profiltekst/','/home/claude/dw-guide','Dating profiltekst: sådan skriver du en god datingprofil (med eksempler) – Dateworld','Konkrete råd til billeder og profiltekst, eksempler og de fejl, der koster flest svar.')]
RV=[('/dating-dk-anmeldelse/','dw-demo','Dating.dk'),('/single-dk-anmeldelse/','dw-single','Single.dk'),('/senior-dk-anmeldelse/','dw-senior','Senior.dk'),('/scor-dk-anmeldelse/','dw-scor','Scor.dk'),('/sexhunt-anmeldelse/','dw-sexhunt','Sexhunt.dk'),('/erox-anmeldelse/','dw-erox','Erox.dk'),('/victoria-milan-anmeldelse/','dw-victoriamilan','Victoria Milan'),('/idates-anmeldelse/','dw-idates','iDates'),('/only-flirts-anmeldelse/','dw-onlyflirts','Only-flirts'),('/meet-n-hook-anmeldelse/','dw-meetnhook','Meet-n-Hook'),('/swirvy-date-anmeldelse/','dw-swirvy','Swirvy Date'),('/be2-anmeldelse/','dw-be2','be2'),('/academic-singles-anmeldelse/','dw-academic','Academic Singles'),('/singles50-anmeldelse/','dw-singles50','Singles50'),('/c-date-anmeldelse/','dw-cdate','C-Date'),('/nextlove-anmeldelse/','dw-nextlove','NextLove'),('/40plus-dk-anmeldelse/','dw-40plus','40plus.dk'),('/tinder-anmeldelse/','dw-tinder','Tinder'),('/hinge-anmeldelse/','dw-hinge','Hinge'),('/bumble-anmeldelse/','dw-bumble','Bumble'),('/badoo-anmeldelse/','dw-badoo','Badoo'),('/happn-anmeldelse/','dw-happn','Happn'),('/grindr-anmeldelse/','dw-grindr','Grindr')]
for u,f,t,d in SRC:
    copy_imgs(f); put(u,open(f+'/index.html',encoding='utf-8').read(),t,d)
for u,f,n in RV:
    copy_imgs('/home/claude/'+f); put(u,open('/home/claude/'+f+'/index.html',encoding='utf-8').read(),'%s anmeldelse 2026: pris, fordele og ulemper – Dateworld'%n,'Læs vores anmeldelse af %s: pris, gratis funktioner, sikkerhed, opsigelse og alternativer.'%n)
simple('/om-os/','Om Dateworld – hvem står bag – Dateworld','Om Dateworld','Dateworld hjælper dig med at finde den datingside eller dating app, der passer til dig.',
'''<h2>Hvem er vi?</h2><p>Dateworld.dk er en dansk side, der sammenligner og anmelder datingsider, dating apps og sider til fræk dating. Vi skriver også guides om alt fra profiltekst til den første date.</p>
<p>Dateworld drives af Mondae (CVR 37208329) i Odense.</p>
<h2>Hvad vi gør</h2><p>Vi gennemgår tjenesternes egne hjemmesider, priser, vilkår og hjælpesider og samler det, du har brug for at vide, ét sted. Når vi ikke har haft en profil på en tjeneste, skriver vi det tydeligt i anmeldelsen.</p>
<h2 id="kontakt">Kontakt</h2><p>Har du spørgsmål, rettelser eller forslag, er du velkommen til at skrive til os på <a href="mailto:kontakt@dateworld.dk">kontakt@dateworld.dk</a>.</p>''')
simple('/saadan-arbejder-vi/','Sådan arbejder vi – og sådan tjener vi penge – Dateworld','Sådan arbejder vi','Her kan du læse, hvordan vi vurderer datingsider, og hvordan Dateworld tjener penge.',
'''<h2>Sådan vurderer vi</h2><p>Vi vurderer alle tjenester ud fra de samme fem områder:</p><ul><li><b>Pris:</b> hvad et medlemskab koster pr. måned og i alt, og hvad du kan gratis.</li><li><b>Vilkår:</b> binding, automatisk fornyelse og hvor let det er at opsige.</li><li><b>Funktioner:</b> søgning, beskeder, matchning, app og events.</li><li><b>Sikkerhed:</b> godkendelse af profiler, validering og privatliv.</li><li><b>Gennemsigtighed:</b> hvor åbent tjenesten fortæller om priser, vilkår og hvem der står bag.</li></ul>
<p>Vores anmeldelser bygger på tjenesternes egne offentlige oplysninger, læst på den dato, der står i anmeldelsen. Hvis en pris eller et vilkår ikke er offentligt, skriver vi det, i stedet for at gætte.</p>
<h2>Sådan tjener vi penge</h2><p>Dateworld indeholder reklamelinks. Når du opretter et medlemskab eller køber noget via et af vores links, kan vi få betaling fra tjenesten. Det koster ikke dig noget ekstra.</p><p>Betalingen påvirker ikke vores vurderinger eller rækkefølgen. Vi skriver også om tjenester, vi ikke samarbejder med, og vi advarer tydeligt, når en tjeneste ikke er det, den giver sig ud for, fx chattjenester med fiktive profiler.</p>
<h2>Rettelser</h2><p>Priser og vilkår ændrer sig. Finder du en fejl, så skriv til <a href="mailto:kontakt@dateworld.dk">kontakt@dateworld.dk</a>, så retter vi den.</p>''')
simple('/privatlivspolitik/','Privatlivspolitik og cookies – Dateworld','Privatlivspolitik og cookies','Sådan behandler Dateworld oplysninger om dig, og hvilke cookies vi bruger.',
'''<h2>Dataansvarlig</h2><p>Mondae, CVR 37208329, Rønnevej 19 B, kl., 5270 Odense N. E-mail: <a href="mailto:kontakt@dateworld.dk">kontakt@dateworld.dk</a>.</p>
<h2>Hvilke oplysninger vi behandler</h2><p>Du kan bruge Dateworld uden at oprette dig eller give os personoplysninger. Skriver du til os, behandler vi din e-mail og din henvendelse for at kunne svare dig.</p>
<h2>Cookies</h2><p>Vi bruger kun cookies, når du har givet samtykke, bortset fra cookies, der er nødvendige for, at siden virker. Når du klikker på et reklamelink, kan affiliatenetværket (fx Partner-ads, Daisycon, Insparx og LoveRevenue) sætte en cookie for at registrere, at du kom fra os. [Liste over cookies og evt. statistikværktøj indsættes, når det er valgt.]</p>
<h2>Dine rettigheder</h2><p>Du har ret til indsigt i, berigtigelse og sletning af de oplysninger, vi har om dig. Du kan klage til Datatilsynet.</p>''',crumb='Privatlivspolitik')
ovpage('/datingapps/','Dating apps 2026: guides og anmeldelser – Dateworld','Dating apps','Alt om dating apps samlet ét sted: sammenligninger, gratis apps og anmeldelser.',
 [('Sammenligning','Bedste dating apps','De populære apps sammenlignet.','/bedste-dating-apps/','Se listen'),('Gratis','Gratis dating apps','Apps du kan bruge uden at betale.','/gratis-dating-apps/','Se listen'),('Alternativer','Tinder alternativer','Når du er træt af swipe.','/tinder-alternativer/','Se listen'),('Guide','Tinder bio','Skriv en profil, der får svar.','/tinder-bio/','Læs guiden'),('Anmeldelse','Tinder','Flest brugere.','/tinder-anmeldelse/','Læs anmeldelsen'),('Anmeldelse','Hinge','Til noget seriøst.','/hinge-anmeldelse/','Læs anmeldelsen')])
ovpage('/datingformer/','Datingformer: find den type dating, der passer dig – Dateworld','Datingformer','Seriøs dating, fræk dating, seniordating eller noget helt fjerde? Find den type dating, der passer til dig.',
 [('Type','Seriøs dating','Til dig, der søger et fast forhold.','/serioes-dating/','Se siderne'),('Type','Elitedating','For højtuddannede.','/elitedating/','Se siderne'),('Type','Sexdating','Uforpligtende og frækt.','/sexdating/','Se siderne'),('Type','Utro dating','Diskret dating for folk i forhold.','/utro-dating/','Se siderne'),('Alder','Dating 50+','Til dig over 50.','/dating-50-plus/','Se siderne'),('Målgruppe','Bøsse dating','For homoseksuelle mænd.','/boesse-dating/','Se siderne'),('Målgruppe','Lesbisk dating','For kvinder, der søger kvinder.','/lesbisk-dating/','Se siderne'),('Målgruppe','Kristen dating','Når troen betyder noget.','/kristen-dating/','Se siderne'),('Type','Swingerdating','For par og swingere.','/swingerdating/','Se siderne')])
REVS=[(n,u) for u,f,n in RV]
ovpage('/anmeldelser/','Anmeldelser af datingsider og dating apps – Dateworld','Anmeldelser','Vores anmeldelser af datingsider, dating apps og sider til fræk dating, med pris, vilkår og alternativer.',
 [('Flirtchat' if n in ('iDates','Only-flirts','Meet-n-Hook','Swirvy Date') else 'Anmeldelse',n,'Pris, fordele, ulemper og alternativer.',u,'Læs anmeldelsen') for n,u in REVS])
ovpage('/artikler/','Guides om dating, dates og kærlighed – Dateworld','Guides og artikler','Råd til profilen, den første date og livet i et forhold.',
 [('Din profil','Dating profiltekst','Sådan skriver du en god datingprofil.','/dating-profiltekst/','Læs guiden')])
# comparison
cmp='''<h2>Kort fortalt</h2><p>Dating.dk og Single.dk er begge danske datingsider for singler, der søger en kæreste. Dating.dk er bred med mange profiler i alle aldre, mens Single.dk matcher dig ud fra quizzer om personlighed, humor og livssyn.</p>
<h2>Pris</h2><p>Dating.dk viser sine priser åbent: en +PlusProfil koster 129 kr. pr. 4 uger, og nye brugere kan starte med 4 uger for 29 kr. mod 84 dages binding. Single.dk viser prisen først, når du har oprettet en profil, og købet er bindende for hele den valgte periode.</p>
<h2>Matchning</h2><p>På Dating.dk søger du selv og får forslag ud fra dine kriterier. På Single.dk er quizzerne kernen, og du ser, hvor godt I passer sammen i procent.</p>
<h2>Hvem skal vælge hvad?</h2><ul><li><b>Vælg Dating.dk</b>, hvis du vil have mange profiler at vælge imellem og kende prisen fra start.</li><li><b>Vælg Single.dk</b>, hvis personlighed betyder mest, og du kan lide en mere legende tilgang.</li></ul>
<p>Læs hele <a href="/dating-dk-anmeldelse/">anmeldelsen af Dating.dk</a> og <a href="/single-dk-anmeldelse/">anmeldelsen af Single.dk</a>.</p>'''
simple('/dating-dk-eller-single-dk/','Dating.dk eller Single.dk? Sammenligning 2026 – Dateworld','Dating.dk eller Single.dk?','To danske datingsider til dig, der søger en kæreste. Her er forskellene på pris, matchning og hvem de passer til.',cmp)
# 404, robots, sitemap
simple('/404/','Siden findes ikke – Dateworld','Siden findes ikke','Prøv forsiden eller vores sammenligning af datingsider.','<p><a href="/">Gå til forsiden</a> eller <a href="/datingsider/">se de bedste datingsider</a>.</p>')
shutil.move(OUT+'/404/index.html',OUT+'/404.html'); shutil.rmtree(OUT+'/404'); PAGES.pop('/404/',None)
open(OUT+'/robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://dateworld.dk/sitemap.xml\n')
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>https://dateworld.dk%s</loc><lastmod>2026-11-19</lastmod></url>\n'%u for u in sorted(PAGES))+'</urlset>\n')
print(len(PAGES),'pages')
# ---------- migrated articles
import json,unicodedata
ART=json.load(open('articles.json',encoding='utf-8'))
def slugify(s):
    s=s.lower().replace('æ','ae').replace('ø','oe').replace('å','aa')
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:60]
def esc(s): return H_.escape(s,quote=False)
def md2(m):
    m=re.sub(r'\[/?(vc_|uncode|ult_|rev_)[^\]]*\]','',m)
    lines=[l.strip() for l in m.split('\n') if l.strip()]
    secs=[];cur={'h':None,'b':[]};lst=None
    def flush_list():
        nonlocal lst
        if lst: cur['b'].append('<%s>%s</%s>'%(lst[0],''.join('<li>%s</li>'%esc(x) for x in lst[1]),lst[0])); lst=None
    for l in lines:
        if l.startswith('## ') or l.startswith('# '):
            flush_list()
            if cur['h'] or cur['b']: secs.append(cur)
            cur={'h':l.lstrip('# ').strip(),'b':[]}
        elif l.startswith('### ') or l.startswith('#### '):
            flush_list(); cur['b'].append('<h3>%s</h3>'%esc(l.lstrip('# ').strip()))
        elif re.match(r'^(- |\d+\. )',l):
            t='ol' if l[0].isdigit() else 'ul'
            if not lst or lst[0]!=t: flush_list(); lst=[t,[]]
            lst[1].append(re.sub(r'^(- |\d+\. )','',l))
        elif l.startswith('| '):
            flush_list(); cur['b'].append('<p>%s</p>'%esc(l.strip('| ').replace(' | ',' · ')))
        else:
            flush_list(); cur['b'].append('<p>%s</p>'%esc(l))
    flush_list(); secs.append(cur)
    return secs
GLINKS=[]
for a in ART:
    t=H_.unescape(a['t']).replace('Guide: ',''); t=re.sub(r'\s*\[.*?\]\s*','',t).strip()
    a['title']=t; GLINKS.append((a['s'],t))
LOGOS=[('Dating.dk','logo-dating.webp','28px','Bredest udvalg','/dating-dk-anmeldelse/'),('Senior.dk','logo-senior.webp','14px','Til dig over 50','/senior-dk-anmeldelse/'),('Single.dk','logo-single.svg','12px','Match på personlighed','/single-dk-anmeldelse/')]
def article(a,i):
    secs=md2(a['m'])
    intro=''
    if secs and secs[0]['h'] is None:
        first=secs.pop(0); intro=''.join(first['b'])
    plain=re.sub(r'<[^>]+>','',intro or (secs[0]['b'][0] if secs and secs[0]['b'] else ''))
    desc=(a['d'] or plain)[:155]
    toc=[(slugify(s['h'])+'-%d'%k,s['h']) for k,s in enumerate(secs)]
    gcta='<aside class="gcta"><div><h3>Klar til at møde nogen?</h3><p>Det er gratis at oprette en profil hos de datingsider, vi anbefaler.</p></div><div class="gcta-l">'+''.join('<a href="#" rel="sponsored nofollow"><span class="plg"><img src="img/%s" alt="" style="height:%s"></span><span><small>%s</small><b>%s</b></span>%s</a>'%(l,h,s,n,ARS) for n,l,h,s,u in LOGOS)+'</div><p class="adl"><span>Reklamelinks</span>Vi får betaling, hvis du opretter dig.</p></aside>'
    body=[]
    if intro: body.append('<section class="blk">%s</section>'%intro)
    for k,s in enumerate(secs):
        body.append('<section id="%s" class="blk"><h2>%s</h2>%s</section>'%(toc[k][0],esc(s['h']),''.join(s['b'])))
        if k==2: body.append(gcta)
    if len(secs)<=2: body.append(gcta)
    others=[g for g in GLINKS if g[0]!=a['s']][i%5:i%5+3] or GLINKS[:3]
    rel='<section class="lsec lgray"><div class="wrap"><div class="sec-head"><h2>Flere guides</h2><span class="rule" aria-hidden="true"></span></div><div class="ovgrid">'+''.join('<a class="ov" href="/%s/"><small>Guide</small><h3>%s</h3><span class="go">Læs guiden %s</span></a>'%(s,esc(t),ARS) for s,t in others)+'</div></div></section>'
    side='<aside class="side"><div class="sticky"><nav class="toc" aria-label="Indhold" style="margin-top:0;padding-top:0;border:0"><p>Indhold</p><ol>%s</ol></nav><div class="gside"><p>Vores anbefaling</p><div class="mini"><img src="img/logo-dating.webp" alt=""><div><b>Dating.dk</b><span>Gratis at oprette en profil</span></div></div><a class="cta sm" href="#" rel="sponsored nofollow"><span>Besøg Dating.dk</span><i>%s</i></a><p class="adl"><span>Reklamelink</span>Vi får betaling, hvis du opretter dig.</p></div></div></aside>'%(''.join('<li><a href="#%s">%s</a></li>'%(x,esc(y)) for x,y in toc),ARS)
    hero='<section class="rhero ghero"><div class="glow" aria-hidden="true"></div><div class="wrap"><nav class="crumbs" aria-label="Brødkrummer"><a href="/">Forside</a><span>/</span><a href="/artikler/">Guides</a><span>/</span><span aria-current="page">%s</span></nav><p class="gkick">Guide</p><h1>%s</h1><p class="meta"><span>Opdateret 19. november 2026</span><span>Af Dateworld-redaktionen</span></p></div></section>'%(esc(a['title'][:40]),esc(a['title']))
    main=hero+'<section class="rbody"><div class="wrap rgrid"><article class="rart">'+'\n'.join(body)+'</article>'+side+'</div></section>'+rel
    put('/%s/'%a['s'],shell(main,a['title']),a['title']+' – Dateworld',desc)
for i,a in enumerate(ART): article(a,i)
# rebuild artikler overview incl. migrated
ovpage('/artikler/','Guides om dating, dates og kærlighed – Dateworld','Guides og artikler','Råd til profilen, den første date og livet i et forhold.',
 [('Din profil','Dating profiltekst','Sådan skriver du en god datingprofil.','/dating-profiltekst/','Læs guiden')]+[('Guide',t,'',('/%s/'%s),'Læs guiden') for s,t in GLINKS])
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>https://dateworld.dk%s</loc><lastmod>2026-11-19</lastmod></url>\n'%u for u in sorted(PAGES))+'</urlset>\n')
print(len(PAGES),'pages total')
