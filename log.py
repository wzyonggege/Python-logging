# coding:utf-8
import logging

# log setting
LOG_FILE = 'test.log'
ERROR_LOG_FILE = 'test_error.log'

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(filename=LOG_FILE, filemode='a+',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    )

logger = logging.getLogger(__name__)

# print in console
console_handler = logging.StreamHandler()
console_handler.formatter = formatter
logger.addHandler(console_handler)

# error file
file_handler = logging.FileHandler(ERROR_LOG_FILE)
file_handler.level = logging.ERROR
file_handler.formatter = formatter
logger.addHandler(file_handler)

logger.info('this is info')
logger.warn('this is warn')
logger.error('this is error')
