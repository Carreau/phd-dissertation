" set dictionary+=./vimwords
imap <C-S> 1z=
nmap <C-S> 1z=
nmap <C-D> [s
imap <C-D> [s

"Ctrl+C will autocorrect the last badly spell words 
imap <C-C> <esc>mk[s1z=`ki
nmap <C-C> <esc>mk[s1z=`k

set linebreak

set complete+=kspell
set completeopt+=longest
set spellfile=phd.en.utf-8.add
