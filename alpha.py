 def format_lab_names(self, persons):
        # see alpha.bst format.lab.names
        # s = persons
        
        lpers = len(persons)

        lim = 1

        result = ''

        for i,person in enumerate(persons[:lim]):
            result += _strip_nonalnum(
                 person.prelast(abbr=False) + person.last(abbr=False))
            if i < lim-1 : 
                result +=', '
        if lpers > lim :
            result +=' et al.'
        return result+' '

# pybtex/style/labels/alpha.py
