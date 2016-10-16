#!/usr/bin/env python
# -*- coding: utf-8 -*-
# session 使用
from flask import Flask, render_template, session, escape, redirect, url_for, request
import os
import time
app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Login in as %s' % escape(session['username'])
    else:
        return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        app.logger.debug(
            '%s login as %s' % (request.form['username'], time.localtime(time.time())))
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
# 产生秘钥
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run()
    app.run()
