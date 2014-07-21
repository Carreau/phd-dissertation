#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

with io.open('_build/latex/actingeldynamics.tex') as f:
    lines = f.readlines()

import re

t =[]
tpage = io.open('tpage.tex').read()
for l in lines :
    lcl=l.replace(u'chapter{P', u'chapter*{P')\
         .replace(u'chapter{Résumé', u'chapter*{Résumé')\
         .replace(u'\\renewcommand{\\releasename}{Release}', u'\\renewcommand{\\releasename}{}')\
         .replace(u'\maketitle\n',u'\maketitle\n'+tpage)
    lcl2 = re.sub(r']}}} \(\\autopageref\*{[a-zA-Z0-9/:-]+}\)',']}}}', lcl)
    lcl3 = re.sub(r'parts/[a-zA-Z0-92]+','index-latex',lcl2)
    t.append( lcl3 )


with io.open('_build/latex/actingeldynamics.tex','w') as f:
    for l in t:
        f.write(l)
