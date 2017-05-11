#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import redis

def connredis():
	r=redis.Redis(host="localhost",port=6379,db=0)
	return r
	