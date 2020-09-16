""" tests the USE CASES described in the doc"""

from . import TestConfigChallenge
import json

class TestUSECASES(TestConfigChallenge):

	def test_large_machines(self):
		"""All large machines"""
		largeName = 'COFFEE_MACHINE_LARGE'

		# get the large machines
		#
		
		data = {'name':largeName}
		result=self.client_app.get('/api/get_machine_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		# get 3 results
		
		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['machine_product_type'][0]['CoffeeMachines']), 3, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

	def test_large_pods(self):
		"""All large pods"""
		largeName = 'COFFEE_POD_LARGE'

		# get the large machines
		#
		
		data = {'name':largeName}
		result=self.client_app.get('/api/get_pod_product_type', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		# get 10 results
		
		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['pod_product_type'][0]['coffeePods']), 10, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

	def test_espresso_pods(self):
		""" All espresso vanilla pods"""

		espressoName = 'ESPRESSO_POD'
		flavor = 'COFFEE_FLAVOR_VANILLA'

		# get the large machines
		#
		
		data = {'product_type':espressoName, 'coffee_flavor':flavor}
		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		# get 3 results
		
		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_pods']), 3, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

	def test_espresso_machines(self):
		"""All espresso machines"""
		
		productType = 'ESPRESSO_MACHINE'

		data = {'product_type':productType}
		result=self.client_app.get('/api/get_machine', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_machines']), 3, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

	def test_small_pods(self):
		"""All small pods"""

		smallPods = 'COFFEE_POD_SMALL'
		
		data = {'product_type':smallPods}
		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_pods']), 10, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

	def test_pods_7_pack(self):
		"""All pods sold in 7 dozen packs"""

		packSize = 84

		data = {'pod_pack_size':packSize}
		result=self.client_app.get('/api/get_pod', query_string=data, content_type='application/json')
		data = json.loads(result.data.decode())

		self.assertTrue(data, 'no data')
		self.assertEqual(len(data['data']['coffee_pods']), 2, 'query failed')
		self.assertEqual(data['message'],  None)
		self.assertEqual(data['status'], 'success')
		self.assertEqual(result.content_type, 'application/json')
		self.assertEqual(result.status_code, 200)

