#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import logging
import logging.config

LOG_FILENAME='logging.conf'
logging.config.fileConfig(LOG_FILENAME)
logger=logging.getLogger('simple_log_example')
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
