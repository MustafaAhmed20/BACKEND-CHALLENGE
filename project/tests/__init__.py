from app import create_app

from app.models import db, defaultData

import unittest
import os

# application instance
app = create_app()
app.app_context().push()

# testing config
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['DEBUG'] = False

# use testing database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI') +\
										 os.getenv('DATABASE_NAME_TESTING')

# raise error if no environment variable
assert os.getenv('SQLALCHEMY_DATABASE_URI') and os.getenv('DATABASE_NAME_TESTING')

class TestConfig(unittest.TestCase):
	""" The base test class. all test Inherits from this class """

	def setUp(self):
		"""
		Create the database if not created!
		
		"""
		# test app
		self.client_app = app.test_client()

		# now create the tables 
		db.create_all()

		# add the default Data
		#defaultData(app=app, db=db)

	def tearDown(self):

		# drop all tables
		db.drop_all()

class TestConfigChallenge(unittest.TestCase):
	""" test the app with the default data described in the challenge doc """

	def setUp(self):
		"""
		Create the database if not created!
		
		"""
		# test app
		self.client_app = app.test_client()

		# now create the tables 
		db.create_all()

		# add the default Data
		defaultData(app=app, db=db)

	def tearDown(self):

		# drop all tables
		db.drop_all()
