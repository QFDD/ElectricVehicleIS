from flask import current_app, g
import sqlite3
import click

DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#数据库结束
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    