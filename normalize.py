#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

with io.open('_build/latex/actingeldynamics.tex') as f:
    lines = f.readlines()

t =[]
tpage = io.open('tpage.tex').read()
for l in lines :
    t.append(
        l.replace(u'chapter{P', u'chapter*{P')\
         .replace(u'chapter{Résumé', u'chapter*{Résumé')\
         .replace(u'\\renewcommand{\\releasename}{Release}', u'\\renewcommand{\\releasename}{}')
         .replace(u'\maketitle\n',u'\maketitle\n'+tpage)
             )


with io.open('_build/latex/actingeldynamics.tex','w') as f:
    for l in t:
        f.write(l)
