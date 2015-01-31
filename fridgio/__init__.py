from flask import Flask, g
from flask.ext.couchdb import CouchDBManager
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.config["COUCHDB_SERVER"] = "http://localhost:5984"
app.config["COUCHDB_DATABASE"] = "fridgio"
manager = CouchDBManager()
manager.setup(app)

couch = LocalProxy(lambda: g.couch)

from fridgio import views
