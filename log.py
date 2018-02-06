import logging
import os

# 检查是否有log文件夹 没有则创建
if not os.path.exists('log/'):
    os.mkdir('log')

# log setting
LOG_FILE = os.path.join('log', 'test.log')
ERROR_LOG_FILE =  os.path.join('log', 'test_error.log')

# 获取logger实例
logger = logging.getLogger(__name__)

# 指定logger输出格式
formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')

# 文件日志
file_handler = logging.FileHandler(LOG_FILE)
file_handler.formatter = formatter
logger.addHandler(file_handler)

# 添加控制台logger
console_handler = logging.StreamHandler()
console_handler.formatter = formatter
logger.addHandler(console_handler)

# 添加Error级别日志写入
error_file_handler = logging.FileHandler(ERROR_LOG_FILE)
error_file_handler.level = logging.ERROR
error_file_handler.formatter = formatter
logger.addHandler(error_file_handler)

# 设置输出级别
logger.setLevel(logging.INFO)

logger.info('this is info')
logger.warning('this is warn')
logger.error('this is error')
