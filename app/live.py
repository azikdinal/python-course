from livereload import Server

# Create a server instance
server = Server()

# Watch the current directory for changes
server.watch('/home/a/python-course/app/templates/', delay=0.1)

# Serve the current directory
server.serve(root='/home/a/python-course/app/templates/')

