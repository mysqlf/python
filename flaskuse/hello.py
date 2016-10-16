#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from mycontroller import *
from flask import Flask, url_for, render_template, Markup
from flask import request
from werkzeug import secure_filename
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
    about()


@app.route('/me/<name>')
def me(name=None):
    # 渲染模板,模板文件夹默认templates,应该可以设置,目前不会
    return render_template('me.html', name=name)
    # return 'Me'

with app.test_request_context('/login', method='POST'):
    assert request.path == '/login'
    assert request.method == 'POST'


@app.route('/test')
def testlogin():
    return render_template('login.html')

# 上传文件
# 直接获取文件名


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['img']
        f.save('D:/youget/'+secure_filename(f.filename))
        return '123'
    else:
        return render_template('upload.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    url = 'login.html'
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return render_template('me.html')
            # return log_the_user_in(request.form['username'])
        #     pass
        # return 'YOU can login for post'
        else:
            return 'Tnvalid username/password'
        # return 'YOU can`t login for get
    else:
        return render_template(url)


if __name__ == '__main__':
    app.run()
