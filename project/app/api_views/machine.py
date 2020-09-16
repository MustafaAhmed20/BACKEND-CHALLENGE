""" all the views related to CoffeeMachine model"""

from . import api, jsonify, make_response, request
from . import baseApi, baseStatus
import copy

# import the logic
from ..logic.machine import *

# 'CoffeeMachine' model
#

@api.route('/get_machine')
def getMachineRoute():
	''' filter the coffee Machines with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	name = filters.get('name')
	waterLine = filters.get('water_line')
	productType = filters.get('product_type')

	try:
		machines = getCoffeeMachine(id=id, name=name, WaterLine=waterLine, productType=productType)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not machines:
		result['data']['coffee_machines'] = []
	elif type(machines) is list:
		result['data']['coffee_machines'] = [machine.toDict() for machine in machines]
	else:
		result['data']['coffee_machines'] = [machines.toDict()]

	return make_response(jsonify(result), 200)

@api.route('/add_machine', methods=['POST'])
def addMachineRoute():
	''' add new coffee Machine - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	name = post_data.get('name')
	waterLine = post_data.get('water_line')
	productType = post_data.get('product_type')

	if not all([name, waterLine, productType]):
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not addCoffeeMachine(name=name, WaterLine=waterLine, ProductType=productType):
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_machine', methods=['DELETE'])
def deleteMachineRoute():
	''' delete the coffee Machine - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	id = post_data.get('id')

	if not id:
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not deleteCoffeeMachine(id):
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	return make_response(jsonify(result), 200)


# 'CoffeeMachineProductType' model
#

@api.route('/get_machine_product_type')
def getProductTypeRoute():
	''' filter the coffee Machines types with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	name = filters.get('name')

	try:
		queryResult = getCoffeeMachineProductType(id=id, name=name)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not queryResult:
		result['data']['machine_product_type'] = []
	elif type(queryResult) is list:
		result['data']['machine_product_type'] = [type.toDict() for type in queryResult]
	else:
		result['data']['machine_product_type'] = [queryResult.toDict()]

	return make_response(jsonify(result), 200)

@api.route('/add_machine_product_type', methods=['POST'])
def addProductTypeRoute():
	''' add new ProductType - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	name = post_data.get('name')

	if not name:
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not addCoffeeMachineProductType(name=name):
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_machine_product_type', methods=['DELETE'])
def deleteProductTypeRoute():
	''' delete the ProductType - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	id = post_data.get('id')

	if not id:
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not deleteCoffeeMachineProductType(id):
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	return make_response(jsonify(result), 200)

