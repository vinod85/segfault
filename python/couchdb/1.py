from couchdb.client import Server

server = Server('http://localhost:5984')
try:
	db = server.create('animals')
except:
	db = server['animals']

for name in server:
	print name
