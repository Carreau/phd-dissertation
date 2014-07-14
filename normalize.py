import io

with io.open('_build/latex/actingeldynamics.tex') as f:
    lines = f.readlines()

t =[]
for l in lines :
    t.append(
        l.replace(u'chapter{P', u'chapter*{P')\
         .replace(u'\\renewcommand{\\releasename}{Release}', u'\\renewcommand{\\releasename}{}')

             )


with io.open('_build/latex/actingeldynamics.tex','w') as f:
    for l in t:
        f.write(l)
