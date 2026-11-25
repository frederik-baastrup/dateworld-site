import re
exec(open('/home/claude/dateworld-site/build/brands.py').read())
NM={v['n']:v for v in B.values()}
NAMERX=re.compile('|'.join(re.escape('>'+n+'<') for n in sorted(NM,key=len,reverse=True))+r'|\[(PRIS|JA/NEJ|Fordel|Ulempe|x,x|Bedst til …)\]')
OPS={'finder':'Log ind og åbn dine kontoindstillinger. Medlemskab og betaling ligger typisk under punktet "Medlemskab" eller "Abonnement".',
 'fornyes':'Tjek, om medlemskabet fornyes automatisk. Slå fornyelsen fra i god tid før næste periode, så du ikke bliver trukket igen.',
 'sletter':'Under indstillingerne kan du slette profilen. Opsig medlemskabet først – en slettet profil stopper ikke altid en betaling.'}
def fill(t):
    cur=[None];cnt={}
    def rep(m):
        s=m.group(0)
        if s.startswith('>'):
            cur[0]=NM[s[1:-1]];return s
        v=cur[0];k=m.group(1)
        if not v: return s
        i=cnt[(v['n'],k)]=cnt.get((v['n'],k),-1)+1
        if k=='PRIS': return v['price']
        if k=='x,x': return v['score']
        if k=='Bedst til …': return v['chips'][-1]
        if k=='JA/NEJ': return v['free'] if i%2==0 else ('Nej' if v['app']=='Web' else 'Ja')
        L=v['pros'] if k=='Fordel' else v['cons']
        return L[i] if i<len(L) else '\x00'
    t=NAMERX.sub(rep,t)
    t=re.sub(r'<li>\x00</li>','',t)
    t=re.sub(r'<section class="lsec lgray" id="produkter">.*?</section>','',t,flags=re.S)
    t=t.replace('<span class="gimg">[BILLEDE]</span>','')
    t=re.sub(r'<section class="blk gauthor">.*?</section>','',t,flags=re.S)
    t=t.replace('[DATO]','november 2026').replace('[NAVN]','Dateworld-redaktionen')
    t=t.replace('[Pris og vilkår tjekkes i anmeldelsen]','Prisen vises først efter oprettelse')
    t=t.replace('[Hvordan siderne vises på kontoudtoget, fx under et neutralt firmanavn. Tjekkes for hver side.]','Det varierer fra side til side. Mange voksensider trækker betalingen under et neutralt firmanavn – navnet står typisk på betalingssiden, så tjek det, før du betaler.')
    for a,b in [(r'\[Hvor du finder[^\]]*\]',OPS['finder']),(r'\[Om [^\]]*(?:fornyes|abonnement)[^\]]*\]',OPS['fornyes']),(r'\[Hvor du sletter[^\]]*\]',OPS['sletter'])]: t=re.sub(a,b,t)
    return t
_fill0=fill
def fill(t):
    t=_fill0(t)
    def fx(m):
        n=m.group(3);v=NM.get(n)
        if m.group(1)==n: return m.group(0)
        return '<span class="plg"><b>%s</b></span><span><small>%s</small><b>%s</b>'%(n,v['chips'][-1] if v else m.group(2),n)
    return re.sub(r'<span class="plg"><b>([^<]*)</b></span><span><small>([^<]*)</small><b>([^<]*)</b>',fx,t)
HOME={'Dating.dk':'https://www.dating.dk/','Single.dk':'https://www.single.dk/','Senior.dk':'https://www.senior.dk/','Scor.dk':'https://www.scor.dk/','Sexhunt.dk':'https://www.sexhunt.dk/','Erox.dk':'https://www.erox.dk/','Victoria Milan':'https://www.victoriamilan.dk/','C-Date':'https://www.c-date.dk/','Singles50':'https://www.singles50.dk/','Academic Singles':'https://www.academicsingles.dk/','be2':'https://www.be2.dk/','NextLove':'https://www.nextlove.com/','Tinder':'https://tinder.com/','Hinge':'https://hinge.co/','Bumble':'https://bumble.com/','Badoo':'https://badoo.com/','Happn':'https://www.happn.com/','Grindr':'https://www.grindr.com/','40plus.dk':'https://www.40plus.dk/','iDates':'https://www.idates.com/','Only-flirts':'https://www.only-flirts.com/','Meet-n-Hook':'https://www.meet-n-hook.com/','Swirvy':'https://www.swirvy.com/'}
LP='/wp-content/uploads/dw-logos/'
LOGO={'Scor.dk':('scor2.svg',1),'Sexhunt.dk':('sexhunt.png',1),'Erox.dk':('erox.png',1),'Victoria Milan':('vm.png',0),'C-Date':('cdate.svg',0),'Singles50':('singles50.svg',0),'Academic Singles':('academic.svg',0),'be2':('be2.svg',0),'NextLove':('nextlove.png',0),'Hinge':('hinge.gif',0),'Grindr':('grindr.svg',0),'Badoo':('badoo.svg',0),'Bumble':('bumble.svg',0),'40plus.dk':('40plus.png',0),'iDates':('idates.svg',0)}
def limg(n):
    f,d=LOGO[n];st='max-width:84%;max-height:58%;object-fit:contain'+(';background:#1d1418;padding:5px 8px;border-radius:5px;box-sizing:content-box;max-height:44%' if d else '')
    return '<img src="%s%s" alt="%s" style="%s">'%(LP,f,n,st)
_fill1=fill
def fill(t):
    # links uden affiliate -> tjenestens forside
    names=sorted(HOME,key=len,reverse=True);cur=[None]
    rx=re.compile('|'.join(re.escape('>'+n+'<') for n in names)+r'|<a ([^>]*)href="#"([^>]*)>')
    def lk(m):
        s=m.group(0)
        if not s.startswith('<a'):
            cur[0]=s[1:-1];return s
        tail=t[m.end():m.end()+400]
        b=re.search(r'Besøg ('+'|'.join(re.escape(n) for n in names)+')',s+tail[:200])
        n=b.group(1) if b else cur[0]
        if not n or 'Besøg' not in s+tail[:250] and 'visit' not in s and 'cta' not in s: return s
        return ('<a %shref="%s"%s>'%(m.group(1),HOME[n],m.group(2))).replace('rel="sponsored nofollow"','rel="nofollow noopener"')
    t=rx.sub(lk,t)
    t=_fill1(t)
    for n in LOGO:
        t=re.sub(r'(<(?:span|div) class="(?:alg|lc-lg|lg|plg|rlogo)"[^>]*>)<b>%s</b>'%re.escape(n),lambda m:m.group(1)+limg(n),t)
        t=t.replace('<span class="tl">%s</span>'%n.replace('.dk',''),limg(n))
    return t
_fill2=fill
def fill(t):
    t=_fill2(t)
    def r(m):
        n=m.group(1)
        return '<a href="%s" rel="nofollow noopener">%s<b>%s</b>'%(HOME[n],m.group(2),n) if n in HOME else m.group(0)
    return re.sub(r'<a href="#" rel="sponsored nofollow">((?:(?!</a>).){0,400}?)<b>([^<]+)</b>',lambda m:r(type('M',(),{'group':lambda s,i:[m.group(0),m.group(2),m.group(1)][i]})()),t,flags=re.S)
_fill3=fill
def fill(t):
    t=_fill3(t)
    for a,b in [('Det påvirker ikke rækkefølgen eller det, vi skriver.','Tjenester, vi samarbejder med, vises først, og betalingen påvirker rækkefølgen. Den påvirker ikke, hvad vi skriver om tjenesterne.'),
                ('Betalingen påvirker ikke vores vurderinger eller rækkefølgen.','Tjenester, vi samarbejder med, vises først, og betalingen påvirker rækkefølgen på vores sammenligninger. Den påvirker ikke, hvad vi skriver om tjenesterne.'),
                ('Rangeret ud fra vores samlede vurdering af de tjenester, vi har gennemgået.','Tjenester, vi samarbejder med, vises først. Rækkefølgen er påvirket af den betaling, vi får fra dem.'),
                ('Rækkefølgen følger vores samlede vurdering.','Tjenester, vi samarbejder med, vises først, og rækkefølgen er påvirket af den betaling, vi får fra dem.'),
                ('Rangeret ud fra vores samlede vurdering.','Tjenester, vi samarbejder med, vises først. Rækkefølgen er påvirket af den betaling, vi får fra dem.')]:
        t=t.replace(a,b)
    return t
