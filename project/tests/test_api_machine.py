""" the tests related to views/machine """

from . import TestConfig
import json

# the models
from app.models.machine import *

class TestCoffeeMachineApi(TestConfig):

	def test_add_machine_product_type(self):
		''' try add new machine product and then get it with 'GET' request'''

		data = {'name': 'test'}
		
		# send the post request
		result = self.client_app.post("/api/add_machine_product_type", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new type in the database
		resultQuery = CoffeeMachineProductType.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)

		# try get it throw requests
		#
		
		# get the machine product type
		data = {}

		result=self.client_app.get('/api/get_machine_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['machine_product_type']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


		# get the machine product type with id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_machine_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['machine_product_type'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		 # get the machine product type with name filter 
		data = {'name':'test'}

		result = self.client_app.get('/api/get_machine_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['machine_product_type']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the new type
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_machine_product_type', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)
	
	def test_add_machine(self):
		''' try add new coffee machine  and then get it with 'GET' request'''

		# first add product type
		data = {'name':'test'}
		result = self.client_app.post("/api/add_machine_product_type", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# now add the coffee machine
		data = {'name':'test', 'water_line':True, 'product_type':'test'}
		result = self.client_app.post("/api/add_machine", data=json.dumps(data), content_type='application/json')
	
		data = json.loads(result.data.decode())

		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type,  'application/json')
		self.assertEqual(result.status_code, 201)

		# check the new coffee machine in the database
		resultQuery = CoffeeMachine.query.all()
		self.assertTrue(resultQuery, 'no data found')
		self.assertEqual(len(resultQuery), 1)



		# try get it throw requests
        #
        
        # get the machine product type
		data = {}

		result=self.client_app.get('/api/get_machine', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_machines']), 1)
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)


        # get the machine product type with id filter not exist
		data = {'id':5}

		result=self.client_app.get('/api/get_machine', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertFalse(data['data']['coffee_machines'], 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

         # get the machine product type with name filter 
		data = {'name':'test'}

		result=self.client_app.get('/api/get_machine', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_machines']), 1, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

		# now delete the new coffee machine
		data = {'id':resultQuery[0].id}
		result = self.client_app.delete('/api/delete_machine', data=json.dumps(data), content_type='application/json')
		
		data = json.loads(result.data.decode())
		
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

