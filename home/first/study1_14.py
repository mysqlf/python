#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(21), User(22)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
sort_notcompare()


# 使用attrgetter方法代替lambda
from operator import attrgetter


def sort_notcompare_():
    users = [User(23), User(21), User(22)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
sort_notcompare_()
