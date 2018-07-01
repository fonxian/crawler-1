# -*- coding: UTF-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
global db
db = SQLAlchemy()


def create_app(config_name):
    # __name__ 决定应用根目录
    app = Flask(__name__)
    # 初始化app配置
    app.config.from_object(config[config_name])
    # 扩展应用初始化
    bootstrap.init_app(app)
    db.init_app(app)

    # 初始化蓝本
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
