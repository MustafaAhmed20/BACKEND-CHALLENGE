from flask_sqlalchemy import SQLAlchemy

# the database instance
db =  SQLAlchemy()

# import all the models 
from .machine import *
from .pod import *