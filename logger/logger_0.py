# -*- coding: utf-8 -*-
#!python3

import logging

''' Source from 
        Python 中的 Log 利器：使用 logging 模組來整理 print 訊息
        https://zhung.com.tw/article/python中的log利器-使用logging模組來整理print訊息/

    https://docs.python.org/3/library/logging.html

    This is a simple example of using the logging module in Python.    

'''

# TODO 123

logging.basicConfig(level=logging.INFO)

# list all handlers associated with the root logger
for _i, handler in enumerate(logging.root.handlers[:]):
    print(_i, ':', str(handler))
    # logging.root.removeHandler(handler)   # Remove the handler

logging.info('Hi!')
# in stdout: 'INFO:root:Hi'

# create a log file handler
file_handler = logging.FileHandler('log.txt')
# get the root logger and bind the handler
logger = logging.getLogger()
logger.addHandler(file_handler)

for _i, handler in enumerate(logging.root.handlers[:]):
    print(_i, ':', str(handler))

#logging.info('(log to handler) Hi!')
print(logger.getEffectiveLevel())
#logger.setLevel(logging.DEBUG)
logger.info('(log to handler) Hi!')


