from livereload import Server, shell

server = Server()

# run a shell command
server.watch('static/*.stylus', 'make static')

# run a function
#server.watch('foo.txt', alert)

# output stdout into a file
server.watch('_build/html/*.html')#, shell('lessc style.less', output='style.css'))
server.watch('*.rst', shell('make html'))
server.watch('parts/*.rst', shell('make html'))
server.watch('figs/*', shell('make html'))

server.serve()
