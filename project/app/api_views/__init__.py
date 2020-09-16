"""This module will contain the api 'Blueprint' and its views."""

from flask import Blueprint, jsonify, request, make_response

# the Blueprint instance
api = Blueprint('api', __name__)

# this is the general api structure
baseApi = {'status':None, 'message':None, 'data':{}}
# the available status messages
baseStatus = {'failure':'failure', 'success':'success'}

# import the views so the top level app can load it
from .pod import *
from .machine import *