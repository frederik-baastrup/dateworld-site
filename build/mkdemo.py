import re
lines=open('demo.py',encoding='utf-8').read().split('\n')
def setline(prefix,new,count=1):
    idx=[i for i,l in enumerate(lines) if l.lstrip().startswith(prefix)]
    assert len(idx)==count,(prefix,len(idx))
    for i in idx:
        ind=lines[i][:len(lines[i])-len(lines[i].lstrip())]
        lines[i]=ind+new
L=setline
L('<p class="verdict">','<p class="verdict">En bred dansk datingside til dig, der søger en kæreste. Solide funktioner og manuel godkendelse af profiler, men du skal betale for at læse beskeder, og vilkårene kræver opmærksomhed.</p>')
L("<p class=\"meta\"><span>'''+I['clock']","<p class=\"meta\"><span>'''+I['clock'].replace('22','16')+'''Opdateret 11. november 2026</span><span>Af Dateworld-redaktionen</span><span>Læsetid ca. 8 min.</span></p>")
L('<div class="score"><b>[4,2]</b>','<div class="score"><b>3,8</b><span>ud af 5<small>Vores samlede vurdering</small></span></div>')
L('<div><dt>Pris fra</dt>','<div><dt>Pris fra</dt><dd>129 kr. pr. 4 uger</dd></div>')
L('<div><dt>Gratis oprettelse</dt>','<div><dt>Gratis oprettelse</dt><dd>Ja</dd></div>')
L('<div><dt>App</dt>','<div><dt>App</dt><dd>iOS og Android</dd></div>')
L('<div><dt>Typisk alder</dt>','<div><dt>Online siden</dt><dd>1998</dd></div>')
L("<div class=\"fit-yes\">","<div class=\"fit-yes\"><h3>Passer til dig, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(CHK,t) for t in ['du søger en kæreste og gerne vil have mange danske profiler at vælge imellem','du vil i gang uden at betale med det samme','du sætter pris på, at billeder og profiler bliver godkendt manuelt','du vil have dansk kundeservice, som svarer alle ugens dage'])+'''</ul></div>")
L("<div class=\"fit-no\">","<div class=\"fit-no\"><h3>Passer mindre godt, hvis …</h3><ul>'''+''.join('<li>%s%s</li>'%(MIN,t) for t in ['du kun leder efter noget uforpligtende','du vil læse og besvare beskeder uden at betale','du ikke vil binde dig: det billigste tilbud kræver 84 dages binding'])+'''</ul></div>")
L("rows=[('Pris'","rows=[('Pris',3.8,'Gratis at oprette sig, og +PlusProfil koster 129 kr. pr. 4 uger. Rimeligt for en bred dansk tjeneste.'),('Vilkår',3.2,'Automatisk fornyelse og binding på det billigste tilbud. Læs betingelserne, før du køber.'),('Funktioner',4.2,'Søgning, likes, matches, Singler i nærheden, events og en app til begge platforme.'),('Sikkerhed',4.3,'Manuel godkendelse af profiler, krav om ægte billeder og dansk kundeservice alle dage.'),('Brugernes bedømmelse',3.7,'3,6 på Trustpilot og 3,8 i App Store: flest gode anmeldelser, men tydelige klager over vilkår.')]")
L("steps=[(","steps=[('Fortæl, hvem du er','Vælg på forsiden, om du er kvinde eller mand, og hvem du søger.'),('Opret dit login','Angiv e-mail og en adgangskode. Ifølge Dating.dk tager det omkring 3 minutter.'.replace('Ifølge Dating.dk tager det','Det tager'),'),('Udfyld profilen','Skriv om dig selv, og tilføj billeder. Billederne godkendes manuelt, før andre kan se dem.')]".replace("'.replace('Ifølge Dating.dk tager det','Det tager'),'),","'),"))
open('demo.py','w',encoding='utf-8').write('\n'.join(lines))
