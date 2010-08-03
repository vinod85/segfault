from couchdb.client import Server

server = Server('http://localhost:5984')
try:
	db = server.create('animals')
except:
	db = server['animals']

print db.name

server.delete(db.name)
