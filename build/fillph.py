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
