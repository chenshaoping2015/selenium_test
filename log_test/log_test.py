import logging
import os

root_dir = os.path.abspath(os.path.dirname(os.getcwd()))+ '/Log/'
print(root_dir)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename= root_dir + '/test.log/',
    filemode='w'
)
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')