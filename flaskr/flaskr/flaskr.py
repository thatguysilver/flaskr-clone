import os 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) #instantiates application
app.config.from_object(__name__) #Load config from this, flaskr.py

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin', 
    PASSWORD = 'default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    '''connects to specified database)'''

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    '''initializes the db from the cli'''

    init_db()
    print('Initialized database')

def get_db():
    '''Opens a new database connection if there isn't already one.'''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):

    '''closes database again after request is satisfied'''

    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
#I'm gonna have to read the source code for this thing. No idea what's going on.
