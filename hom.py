import bibtexparser
import io
with io.open('library.bib') as bib:
    data = bib.read()
    prs = bibtexparser.bparser.BibTexParser(data)
prs
from  bibtexparser.bwriter import to_bibtex
with io.open('library.bib','w') as bib:
    bib.write(to_bibtex(prs))
