import click
from flask import current_app, g
from flask.cli import with_appcontext
import mysql.connector as mysql
from mysql.connector import errorcode


# The g name stands for “global”, but that is referring to the data being global within a context. 
# The data on g is lost after the context ends, and it is not an appropriate place to store data between requests. 
def get_db():
    if 'db' not in g:
        g.db = mysql.connect(host='127.0.0.1', user='root', password='',
                             database='cs348')
    return g.db

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
