#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def testDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No enteries here so far'.encode('utf-8') in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)  # , follow_redirects=True

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in'.encode('utf-8') in rv.data
        rv = self.logout()
        assert 'You were loggrd out'.encode('utf-8') in rv.data
        rv = self.login('adminx', 'default')
        assert 'Username error'.encode('utf-8') in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Password error'.encode('utf-8') in rv.data

    def test_messages(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(title='<hello>', text='<strong>HTML</strong>allowed here'), follow_redirects=True)  # follow_redirects=True
        assert 'No enteries here so far'.encode('utf-8') not in rv.data
        assert '&lt;hello &gt'.encode('utf-8') in rv.data
        assert '<strong>HTML</strong>allowed here'.encode('utf-8') in rv.data
if __name__ == '__main__':
    unittest.main()
