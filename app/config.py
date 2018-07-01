# -*- coding: UTF-8 -*-
import os



#记录增量更新数量
RECORD_UPDATE_LIMIT = 20


class Config():

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/build?charset=utf8'
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    pass

class DevelopmentConfig(Config):
    """开发环境配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/build?charset=utf8'


class TestConfig(Config):
    """测试环境配置
    """

    #可以通过修改SQLALCHEMY_DATABASE_URI来控制访问不同数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lzx:123@192.168.66.188/blog?charset=utf8'


class ProductionConfig(Config):
    """生产环境
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lzx:123@192.168.66.188/blog'

# 设置配置映射
config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}