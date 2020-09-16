""" the tests related to views/pod """

from . import TestConfig
import json

# the models
from app.models.pod import *

class TestCoffeePodApi(TestConfig):
	""" tests the coffee pods dependencies operations"""

	def test_add_pod_pack_size(self):
		''' try add new pack size and then get it with 'GET' request'''

		data = {'size': 18}
		
		# send the post request
		result = self.client_app.post("/api/add_pod_pack_size", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new PodPackSize in the database
		resultQuery = PodPackSize.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)

		# try get it throw requests
		#
		
		# get the PodPackSize
		data = {}

		result=self.client_app.get('/api/get_pod_pack_size', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_pack_size']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


		# get the PodPackSize id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_pod_pack_size', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['pod_pack_size'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		 # get the PodPackSize size filter 
		data = {'size':18}

		result = self.client_app.get('/api/get_pod_pack_size', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_pack_size']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the PodPackSize
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_pod_pack_size', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# check the new PodPackSize in the database
		resultQuery = PodPackSize.query.all()
		self.assertFalse(resultQuery, 'no data found')

	def test_add_pod_coffee_flavor(self):
		''' try add new coffee flacor and then get it with 'GET' request'''

		data = {'name': 'test'}
		
		# send the post request
		result = self.client_app.post("/api/add_pod_coffee_flavor", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new type in the database
		resultQuery = CoffeeFlavor.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)

		# try get it throw requests
		#
		
		# get the coffee flavor
		data = {}

		result=self.client_app.get('/api/get_pod_coffee_flavor', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_product_type']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


		# get the coffee flavor with id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_pod_coffee_flavor', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['pod_product_type'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		 # get the coffee flavor with name filter 
		data = {'name':'test'}

		result = self.client_app.get('/api/get_pod_coffee_flavor', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_product_type']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the coffee flavor
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_pod_coffee_flavor', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# check the coffee flavor in the database
		resultQuery = CoffeeFlavor.query.all()
		self.assertFalse(resultQuery, 'no data found')
	
	def test_add_pod_product_type(self):
		''' try add new PodProductType and then get it with 'GET' request'''

		data = {'name': 'test'}
		
		# send the post request
		result = self.client_app.post("/api/add_pod_product_type", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new type in the database
		resultQuery = PodProductType.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)

		# try get it throw requests
		#
		
		# get the coffee flavor
		data = {}

		result=self.client_app.get('/api/get_pod_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_product_type']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


		# get the coffee flavor with id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_pod_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['pod_product_type'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		 # get the coffee flavor with name filter 
		data = {'name':'test'}

		result = self.client_app.get('/api/get_pod_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_product_type']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the coffee flavor
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_pod_product_type', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# check the coffee flavor in the database
		resultQuery = PodProductType.query.all()
		self.assertFalse(resultQuery, 'no data found')

class TestCoffeePodApi2(TestConfig):
	""" tests the coffee pods operations"""

	def test_add_pod(self):
		''' try add new coffee pod  and then get it with 'GET' request'''

		# first add the dependencies
		
		data = {'size': 18}
		# send the post request
		result = self.client_app.post("/api/add_pod_pack_size", data=json.dumps(data), content_type='application/json')
		
		data = {'name': 'test'}
		# send the post request
		result = self.client_app.post("/api/add_pod_coffee_flavor", data=json.dumps(data), content_type='application/json')

		data = {'name': 'test'}	
		# send the post request
		result = self.client_app.post("/api/add_pod_product_type", data=json.dumps(data), content_type='application/json')


		# now add the coffee pod
		#

		data = {'name':'test', 'coffee_flavor':'test', 'product_type':'test', 'pack_size':18}
		result = self.client_app.post("/api/add_pod", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new coffee pod in the database
		resultQuery = CoffeePod.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)



		# try get it throw requests
        #
        
        # get the coffee pod
		data = {}

		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_pods']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


        # get the coffee pods with id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['coffee_pods'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

         # get the coffee pods with name filter 
		data = {'name':'test'}

		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_pods']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the new coffee pod
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_pod', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# check the new type in the database
		resultQuery = CoffeePod.query.all()
		self.assertFalse(resultQuery, 'no data found')

