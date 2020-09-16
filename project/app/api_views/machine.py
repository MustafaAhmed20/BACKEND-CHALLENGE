""" all the views related to CoffeeMachine model"""

from . import api, jsonify, make_response
from . import baseApi, baseStatus

# import the logic
from ..models.machine import *

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
	waterLine = filters.get('waterLine')

	try:
		machines = getCoffeeMachine(id=id, name=name, WaterLine=waterLine)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not machines:
		result['data']['CoffeeMachines'] = []
	elif type(machines) is list:
		result['data']['CoffeeMachines'] = [machine.toDict() for machine in machines]
	else:
		result['data']['CoffeeMachines'] = [machines]

	return make_response(jsonify(result), 200)

@api.route('/add_machine', methods=['POST'])
def addMachineRoute():
	''' add new coffee Machine - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	name = post_data.get('name')
	waterLine = post_data.get('waterLine')
	productType = post_data.get('productType')

	if not all([name, waterLine, productType]):
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not addCoffeeMachine(name=name, WaterLine=waterLine, ProductType=productType):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
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
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)


# 'CoffeeMachineProductType' model
#

@api.route('/get_product_type')
def getProductTypeRoute():
	''' filter the coffee Machines with query parameters'''

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
		result['data']['machine_product_type'] = [queryResult]

	return make_response(jsonify(result), 200)

@api.route('/add_product_type', methods=['POST'])
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
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_product_type', methods=['DELETE'])
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
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)

