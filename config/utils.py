import os
import sys
import logging
import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 读取配置文件
config = yaml.safe_load(open("{}/config.yaml".format(os.path.dirname(os.path.abspath(__file__))), "r"))
# 日志配置
def get_logger(name):
    if not os.path.exists("{}/../logs/".format(os.path.dirname(os.path.abspath(__file__)))):
        os.mkdir("{}/../logs/".format(os.path.dirname(os.path.abspath(__file__))))
    log_file = "{}/../logs/app.log".format(os.path.dirname(os.path.abspath(__file__)))
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

