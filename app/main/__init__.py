from flask import Blueprint

# 实例化蓝本对象，必须指定name蓝本名字，import_name蓝本所在包或模块
main = Blueprint(name='main', import_name=__name__)