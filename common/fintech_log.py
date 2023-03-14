#coding=utf-8

import logging
import logging.handlers
import os
import time


class Logs(object):
    def __init__(self):
        self.logger = logging.getLogger("")
        # 创建文件目录
        logs_dir = 'logs'
        if not os.path.exists(logs_dir) or not os.path.isdir(logs_dir):
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = f'{timestamp}.log'
        logfilepath = os.path.join(logs_dir, logfilename)
        FileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                           maxBytes=1024 * 1024 * 50,
                                                           backupCount=5,
                                                           encoding='utf-8')
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - %(levelname)s: %(message)s')

        FileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(FileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)


if __name__ == "__main__":
    log = Logs()
#     log.info("---记录开始---")
#     log.info("---记录结束---")
