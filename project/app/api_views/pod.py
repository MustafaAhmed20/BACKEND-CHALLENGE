""" all the views related to CoffeeMachine model"""

from . import api, jsonify, make_response
from . import baseApi, baseStatus

# import the logic
from ..models.pod import *

# 'CoffeePod' model
#

@api.route('/get_pod')
def getPodRoute():
	''' filter the coffee pods with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	name = filters.get('name')
	

	try:
		pods = getCoffeePod(id=id, name=name)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not machines:
		result['data']['coffee_pods'] = []
	elif type(machines) is list:
		result['data']['coffee_pods'] = [p.toDict() for p in pods]
	else:
		result['data']['coffee_pods'] = [pods]

	return make_response(jsonify(result), 200)

@api.route('/add_pod', methods=['POST'])
def addPodRoute():
	''' add new coffee pod - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	name = post_data.get('name')
	coffeeFlavor = post_data.get('coffee_flavor')
	productType = post_data.get('product_type')
	podPackSize = post_data.get('pack_size')

	if not all([name, coffeeFlavor, productType, podPackSize]):
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not addCoffeePod(name=name, coffeeFlavor=coffeeFlavor, productType=productType, podPackSize=podPackSize):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_pod', methods=['DELETE'])
def deleteMachineRoute():
	''' delete the coffee Pod - accept data as json'''

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
	if not deleteCoffeePod(id):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)


# 'PodProductType' model
#

@api.route('/get_pod_product_type')
def getPodProductTypeRoute():
	''' filter the pod types with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	name = filters.get('name')

	try:
		queryResult = getPodProductType(id=id, name=name)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not queryResult:
		result['data']['pod_product_type'] = []
	elif type(queryResult) is list:
		result['data']['pod_product_type'] = [type.toDict() for type in queryResult]
	else:
		result['data']['pod_product_type'] = [queryResult]

	return make_response(jsonify(result), 200)

@api.route('/add_pod_product_type', methods=['POST'])
def addPodProductTypeRoute():
	''' add new Pod ProductType - accept data as json'''

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
	if not addPodProductType(name=name):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_pod_product_type', methods=['DELETE'])
def deletePodProductTypeRoute():
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
	if not deletePodProductType(id):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)

# 'CoffeeFlavor' model
#

@api.route('/get_pod_coffee_flavor')
def getPodCoffeeFlavorRoute():
	''' filter the pod CoffeeFlavors with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	name = filters.get('name')

	try:
		queryResult = getCoffeeFlavor(id=id, name=name)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not queryResult:
		result['data']['pod_product_type'] = []
	elif type(queryResult) is list:
		result['data']['pod_product_type'] = [type.toDict() for type in queryResult]
	else:
		result['data']['pod_product_type'] = [queryResult]

	return make_response(jsonify(result), 200)

@api.route('/add_pod_coffee_flavor', methods=['POST'])
def addPodCoffeeFlavorRoute():
	''' add new Pod CoffeeFlavor - accept data as json'''

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
	if not addCoffeeFlavor(name=name):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_pod_coffee_flavor', methods=['DELETE'])
def deletePodCoffeeFlavorRoute():
	''' delete the pod CoffeeFlavor - accept data as json'''

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
	if not deleteCoffeeFlavor(id):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)

# 'PodPackSize' model
#

@api.route('/get_pod_pack_size')
def getPodPodPackSizeRoute():
	''' filter the PodPackSize with query parameters'''

	# the result json structure
	result = copy.deepcopy(baseApi)
	
	filters = request.args

	# get with filters
	#
	
	id = filters.get('id')
	size = filters.get('size')

	try:
		queryResult = getPodPackSize(id=id, size=size)
	except Exception as e:
		result['status'] = baseStatus['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = baseStatus['success']
	if not queryResult:
		result['data']['pod_pack_size'] = []
	elif type(queryResult) is list:
		result['data']['pod_pack_size'] = [type.toDict() for type in queryResult]
	else:
		result['data']['pod_pack_size'] = [queryResult]

	return make_response(jsonify(result), 200)

@api.route('/add_pod_pack_size', methods=['POST'])
def addPodPodPackSizeRoute():
	''' add new PodPackSize - accept data as json'''

	# the result json structure
	result = copy.deepcopy(baseApi)

	# get the json post data
	post_data = request.get_json()

	size = post_data.get('size')

	if not size:
		# fail
		result['status'] = baseStatus['failure']
		result['message'] = 'required data not submitted'
		return make_response(jsonify(result), 400)

	# add the data
	if not addPodPackSize(size=size):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 201)

@api.route('/delete_pod_pack_size', methods=['DELETE'])
def deletePodPodPackSizeRoute():
	''' delete the PodPackSize - accept data as json'''

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
	if not deletePodPackSize(id):
		result['status'] = status['failure']
		result['message'] = 'Some error occurred. Please try again'
		return make_response(jsonify(result), 401)

	# success
	result['status'] = status['success']
	return make_response(jsonify(result), 200)

