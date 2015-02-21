#db_create.py - sets up and creates the database
# ORM - Translates and maps SQL commands and ur db schema into python objects

from views import db
from models import Task
from datetime import date

# create the database and the db table - initialize the database schema
db.create_all()


#insert data - use the Task object from models.py to specify schema
# db.session.add(Task("Finish Work assignment", date(2014, 4, 13), 10, 1))
# db.session.add(Task("Meet the directors", date(2014, 7, 13), 10, 1))

# commit the changes
db.session.commit()