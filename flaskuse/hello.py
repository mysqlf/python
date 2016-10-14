#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/hello/<username>/<int:age>')
def welcome(username, age):
    return '%s ,Welcome to flask %s' % (username, age)


@app.route('/hello/<int:age>')
def showage(age):
    return 'you age %s' % age


@app.route('/about')
def about():
    return 'About Us'


@app.route('/me/')
def me():
    return render_template('me.html')  # 渲染模板,模板文件夹默认templates,应该可以设置,目前不会
    # return 'Me'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'YOU can login for post'
    else:
        return 'YOU can`t login for get'
if __name__ == '__main__':
    app.run()
