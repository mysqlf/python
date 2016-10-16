#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, redirect, url_for
from mycontroller import *
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    # abort(401)
    return this_is_never_executed()
if __name__ == '__main__':
    app.run()
