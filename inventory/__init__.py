#!/usr/bin/python3
"""This module contains initailization for the inventory package"""
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from inventory.models.engine.db_storage import DBStorage
"""from flask_login import LoginManager"""


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bcrypt = Bcrypt(app)
storage = DBStorage()
storage.reload()
"""login_manager = LoginManager(app)"""

from inventory import user_routes
