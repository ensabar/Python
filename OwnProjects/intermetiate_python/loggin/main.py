#import logging
#logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/Y %H:%M:%S')
#import helper
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is an warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

#logger = logging.getLogger(__name__)
# 
##create handler
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('loggin/file.log')
#
## level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)
#
#formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)
#
#logger.addHandler(stream_h)
#logger.addHandler(file_h)
#
#logger.warning('this is a warning')
#logger.error('this is an error')


#########################################################################
# Second example using .conf file
#import logging
#import logging.config
#
#logging.config.fileConfig('loggin/logging.conf')
#
#logger = logging.getLogger('simpleExample')
#logger.debug('this is a debug message')

#########################################################################
# Third example formatting error catching
#import logging
#import traceback
##try:
##    a = [1, 2, 3]
##    val = a[4]
##except IndexError as e:
##    logging.error(e, exc_info=True)
#
#try:
#    a = [1, 2, 3]
#    val = a[4]
#except:
#    logging.error('The error is %s', traceback.format_exc())

#########################################################################
# Rotation file handler

#import logging
#from logging.handlers import RotatingFileHandler
#
## create logger
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
#
##roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
#
#handler = RotatingFileHandler('loggin/app.log', maxBytes=2000, backupCount=5)
#logger.addHandler(handler)
#
#for _ in range(10000):
#    logger.info('Hello world')

#########################################################################
# Rotation file handler with time duration

import logging
import time
from logging.handlers import TimedRotatingFileHandler

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.

# s, m, h, d
handler = TimedRotatingFileHandler('loggin/timed_test.log',when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello world')
    time.sleep(5)

