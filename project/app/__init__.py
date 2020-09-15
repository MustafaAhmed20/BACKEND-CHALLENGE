from flask import Flask, make_response
from dotenv import load_dotenv

def create_app():
	""" create the app instance """
	
	# load the variables from the '.env' file!
	load_dotenv()

	from . import models, api_views
	app = Flask(__name__)

	# Configurations
	app.config.from_object('config')
	
	models.db.init_app(app)

	# register the blueprints
	#app.register_blueprint(api_views.api, url_prefix='/api')
	
	return app
