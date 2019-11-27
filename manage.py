# coding: utf-8
# !/usr/bin/env python
# Author: ID3055

import os
from flask_script import Manager
from backend import create_app
from flask_cors import CORS

app = create_app(config_name=os.getenv("FLASK_CONFIG") or 'default')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
