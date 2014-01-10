#!/usr/bin/env python

from livereload import Server, shell

server = Server()

# run a shell command
server.watch('*.rst', 'make html')


server.serve()

