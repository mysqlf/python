#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from line_spout import LineSpout
from split_words import SplitWordsBolt
from count_words import CountWordsBolt
from log_results import LogResultsBolt


def create(builder):
    builder.setSpout("spout", LineSpout(), 1)
    builder.setBolt("split", SplitWordsBolt(), 1).shuffleGrouping("spout")
    builder.setBolt("count", CountWordsBolt(),
                    1).fieldsGrouping("split", ["word"])
    builder.setBolt("result", LogResultsBolt(),
                    1).fieldsGrouping("split")
