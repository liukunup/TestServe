# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2024/3/16 00:31
# description: XXX

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ 开发环境 """
    # 环境标识
    DEBUG = True
    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'local-database.sqlite')


class TestingConfig(Config):
    """ 测试环境 """
    # 环境标识
    TESTING = True
    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'local-database.sqlite')


class StagingConfig(Config):
    """ 预发环境 """
    # 环境标识
    STAGING = True
    # 数据库
    host = os.environ.get('DATABASE_HOST') or '127.0.0.1'
    port = os.environ.get('DATABASE_PORT') or '3306'
    username = os.environ.get('DATABASE_USERNAME') or 'root'
    password = os.environ.get('DATABASE_PASSWORD') or 'hard to guess'
    #
    from urllib import parse
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'mysql+pymysql://{host}:{port}@{parse.quote(username)}:{parse.quote(password)}/db?charset=utf8'


class ProductionConfig(StagingConfig):
    """ 生产环境 """

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class DockerConfig(ProductionConfig):
    """ 在Docker环境执行 """
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    """ 在Linux环境执行 """
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.INFO)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}
