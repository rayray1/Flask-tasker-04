# config.py - holds the app's settings and configuration variables

import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)


#database uri - to tell sqlalchemy where to access the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH