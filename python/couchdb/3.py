from couchdb.client import Server

server = Server('http://localhost:5984')
try:
	db = server.create('animals')
except:
	db = server['animals']

doc_id, doc_rev = db.save({'type': 'Sparrow', 'name': 'Jack'})
print doc_id, doc_rev
