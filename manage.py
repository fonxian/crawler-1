# -*- coding: UTF-8 -*-

import os
from . import *
from flask_script import *
from build_spider import  *
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':

    manager.run()
    a()
