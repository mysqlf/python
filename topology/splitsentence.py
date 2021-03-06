#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from petrel import storm
from petrel.emitter import BasicBolt


class SplitSentenceBolt(BasicBolt):

    def __init__(self):
        super(SplitSentenceBolt, self).__init__(script=__file__)

    @classmethod
    def declareOutputFields(self):
        return ['word']

    def process(self, tup):
        words = tup.values[0].split("")
        for word in words:
            storm.emit([word])


def run():
    SplitSentenceBolt().run()
