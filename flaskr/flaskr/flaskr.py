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
e
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    '''connects to specified database)'''

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

#I'm gonna have to read the source code for this thing. No idea what's going on.
