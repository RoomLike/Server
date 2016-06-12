#!/usr/bin/python

import bottle
import bottle.ext.sqlite
from bottle import SimpleTemplate

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='/home/tinyiota/development/RoomLike/Server/Server/db/test.db')
app.install(plugin)

@app.route('/show/:name')
def show(name, db):
	
        row = db.execute('SELECT * FROM Users WHERE UserName = ?', [name]).fetchone()
        if row:
		return row['UserName']
        return HTTPError(404, 'Page not found')

app.run(host = 'localhost', port = 8080, debug = True)
