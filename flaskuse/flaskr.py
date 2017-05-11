#!/usr/bin/env python
# -*- coding: utf-8 -*-
# all inport
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort
from flask import render_template, flash
# from contextlib import contextmanager
# from flask import appcontext_pushed
# from flask import json, jsonify
app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('sc.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# def get_user():
#     user = getattr(g, 'user', None)
#     if user is None:
#         user = fetch_current_user_from_database()
#         g.user = user
#     return user


# @contextmanager
# def user_set(app, user):
#     def handler(sender, **kwargs):
#         g.user = user
#     with appcontext_pushed.connected_to(handler, app):
#         yield


# @app.route('/users/me')
# def user_me():
#     return jsonify(username=g.user.username)

# with user_set(app, user_me):
#     with add.test_client() as c:
#         resp = c.get('/users/me')
#         data = json.loads(resp.data)
#         self.assert_equal(data['username'], my_user.username)


@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) values(?,?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Username error'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Password error'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.before_request
def before_request():
    g.db = connect_db()
if __name__ == "__main__":
    app.run()
    # # To allow aptana to receive errors, set use_debugger=False
    # app = create_app(config="config.yaml")

    # if app.debug:
    #     use_debugger = True
    # try:
    #     # Disable Flask's debugger if external debugger is requested
    #     use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
    # except:
    #     pass
    # app.run(use_debugger=use_debugger, debug=app.debug,
    #         use_reloader=use_debugger, host='0.0.0.0')
