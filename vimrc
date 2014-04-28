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

function! SearchMultiLine(bang, ...)
  if a:0 > 0
    let sep = (a:bang) ? '\_W\+' : '\_s\+'
    let @/ = join(a:000, sep)
  endif
endfunction
command! -bang -nargs=* -complete=tag S call SearchMultiLine(<bang>0, <f-args>)|normal! /<C-R>/<CR>

set ignorecase
