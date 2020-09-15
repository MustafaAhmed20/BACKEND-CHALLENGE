""" the tests related to 'CoffeeMachine' model and logic"""

from . import TestConfig

# the logic
from app.logic.machine import *

# the models
from app.models.machine import *

class TestCoffeeMachine(TestConfig):

	def test_addCoffeeMachine(self):
		""" add new CoffeeMachine """

		# first add new product type
		productType = addCoffeeMachineProductType(name='test')
		self.assertTrue(productType, 'add new type failed')

		# check the new type in the database
		newType = CoffeeMachineProductType.query.filter_by(name='test').first()
		self.assertTrue(newType, 'no new type returned')


		# add new Machine
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')

		self.assertTrue(Machine, 'add new Machine failed')

		# check the new Machine in the database
		newType = CoffeeMachine.query.filter_by(name='test').first()
		self.assertTrue(newType, 'no new type returned')

	def test_getCoffeeMachine(self):
		""" add new CoffeeMachine and filter it with the getters"""

		# first add new product type

		productType = addCoffeeMachineProductType(name='test')

		self.assertTrue(productType, 'add new type failed')

		# add new Machine
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')

		self.assertTrue(Machine, 'add new Machine failed')

		## try get the type with the filter
		##
		allTypes = getCoffeeMachineProductType()

		self.assertTrue(allTypes, 'no types returned')
		self.assertEqual(len(allTypes), 1, 'not the right number of types')

		# filter the types with id
		returnedType = getCoffeeMachineProductType(id=productType.id)
		self.assertTrue(returnedType, 'no type returned')

		# filter the types with name
		returnedType = getCoffeeMachineProductType(name=productType.name)
		self.assertTrue(returnedType, 'no type returned')

		
		## filter the Machine
		##
		allMachines = getCoffeeMachine()

		self.assertTrue(allMachines, 'no Machines returned')
		self.assertEqual(len(allMachines), 1, 'not the right number of Machines')

		# filter the Machine with id
		returnedMachine = getCoffeeMachine(id=Machine.id)
		self.assertTrue(returnedMachine, 'no Machine returned')

		# filter the Machine with name
		returnedMachine = getCoffeeMachine(name=Machine.name)
		self.assertTrue(returnedMachine, 'no Machine returned')

	def test_failaddCoffeeMachine(self):
		""" try add a CoffeeMachine with already exist name"""

		# first add new product type
		productType = addCoffeeMachineProductType(name='test')
		self.assertTrue(productType, 'add new type failed')

		# try add new type with same name
		productType = addCoffeeMachineProductType(name='test')
		self.assertFalse(productType, 'add new type with same name')

		# add new Machine
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')
		self.assertTrue(Machine, 'add new Machine failed')

		# try add new Machine with same name
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')
		self.assertFalse(Machine, 'add new Machine with same name')

	def test_deleteCoffeeMachine(self):
		''' add new CoffeeMachine then delete it'''

		# first add new product type
		productType = addCoffeeMachineProductType(name='test')
		self.assertTrue(productType, 'add new type failed')

		# add new Machine
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')
		self.assertTrue(Machine, 'add new Machine failed')

		# check the new Machine in the database
		newType = CoffeeMachine.query.filter_by(name='test').first()
		self.assertTrue(newType, 'no new type returned')

		# now delete the Machine
		result = deleteCoffeeMachine(id=Machine.id)
		self.assertTrue(result, 'delete the Machine failed')

		# check the Machine in the database
		deletedMachine = CoffeeMachine.query.filter_by(name='test').first()
		self.assertFalse(deletedMachine, 'delete not succeed')
	
	def test_deleteCoffeeMachineProductType(self):
		''' add new productType then delete it with its Machines'''

		# first add new product type
		productType = addCoffeeMachineProductType(name='test')
		self.assertTrue(productType, 'add new type failed')

		# add new Machine
		Machine = addCoffeeMachine(name='test', WaterLine=True, ProductType='test')
		self.assertTrue(Machine, 'add new Machine failed')

		# delete the productType
		result = deleteCoffeeMachineProductType(id=productType.id)
		self.assertTrue(result, 'delete the Machine failed')

		# check the deleted type in the database
		deletedType = CoffeeMachineProductType.query.filter_by(name='test').first()
		self.assertFalse(deletedType, 'delete the type failed')

		# check the related Machine (must be deleted)
		deletedMachine = CoffeeMachine.query.filter_by(name='test').first()
		self.assertFalse(deletedMachine, 'delete the Machine failed')

