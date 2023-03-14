#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : Code 
@File    : demo3.py
@IDE     : PyCharm 
@Author  : xuan
@Date    : 2023-03-14 23:28 
"""
import os
from datetime import datetime
import loguru


class Logger:
    def __init__(self):
        self.logger_add()

    def get_project_path(self, project_path=None):
        if project_path is None:
            # 当前项目文件的，绝对真实路径
            # 路径，一个点代表当前目录，两个点代表当前目录的上级目录
            project_path = os.path.realpath('..')
        # 返回当前项目路径
        return project_path

    def get_log_path(self):
        # 项目目录
        project_path = self.get_project_path()
        # 项目日志目录
        project_log_dir = os.path.join(project_path, 'Logs')
        # 日志文件名
        now = datetime.now()
        project_log_filename = f'{datetime.now().strftime("%Y-%m-%d-%H")}.log'
        # 日志文件路径
        project_log_path = os.path.join(project_log_dir, project_log_filename)
        # 返回日志路径
        return project_log_path

    def logger_add(self):
        loguru.logger.add(
            # 水槽，分流器，可以用来输入路径
            sink=self.get_log_path(),
            # 日志创建周期
            # rotation='00:00',
            # 保存
            rotation="10 MB",
            retention='1 year',
            # 文件的压缩格式
            compression='zip',
            # 编码格式
            encoding="utf-8",
            # 具有使日志记录调用非阻塞的优点
            enqueue=True
        )

    @property
    def get_logger(self):
        return loguru.logger


'''
# 实例化日志类
'''
logger = Logger().get_logger

if __name__ == '__main__':
    logger.debug('调试代码')
    logger.info('输出信息')
    logger.success('输出成功')
    logger.warning('错误警告')
    logger.error('代码错误')
    logger.critical('崩溃输出')

    """
    在其他.py文件中，只需要直接导入已经实例化的logger类即可
    例如导入访视如下：
    from project.logger import logger
    然后直接使用logger即可
    """
