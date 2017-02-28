#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
from petrel import storm
from petrel.emitter import BasicBolt


class WordCountBolt(BasicBolt):

    def __init__(self):
        super(WordCountBolt, self).__init__(script=__file__)
        self.count = defaultdict(int)

    @classmethod
    def declareOutputFields(cls):
        return ['word', 'count']

    def process(self, tup):
        word = tup.values[0]
        self._count[word] += 1
        storm.emit([word, self._count[word]])


def run():
    WordCountBolt().run()
