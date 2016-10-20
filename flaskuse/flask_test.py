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
        assert 'No enteries here so far 'in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'Your were logged in ' in rv.data
        rv = self.logout()
        assert 'Your were loggrd out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Username error' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Password error' in rv.data
if __name__ == '__main__':
    unittest.main()
