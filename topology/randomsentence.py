#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random

from petrel import storm
from petrel.emitter import Spout


class RandomSentenceSpout(Spout):

    def __init__(self):
        super(RandomSentenceSpout, self).__init__(script=__file__)

    @classmethod
    def declareOutputFields(cls):
        return ['sentence']
    sentence = [
        "the cow jumped over the moon",
        "an apple a day keep the doctor away",
    ]

    def nextTuple(self):
        time.sleep(1)
        sentence = self.sentence[
            random.randint(0, len(self.sentence) - 1)]
        storm.emit([sentence])


def run():
    RandomSentenceSpout().run()
