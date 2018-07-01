# -*- coding: UTF-8 -*-

import os
from flask_script import *
from app import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':

    manager.run()

