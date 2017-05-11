#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 设置cookie
from flask import Flask, request, render_template
from flask import make_response
app = Flask(__name__)


@app.route('/index')
def index():
    username = request.cookies.get('username')
    return username


@app.route('/')
def start():
    resp = make_response(render_template('me.html'))
    resp.set_cookie('username', 'ZL')
    return resp


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run()
