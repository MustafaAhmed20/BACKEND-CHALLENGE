""" the tests related to 'CoffeePod' model and logic"""

from . import TestConfig

# the logic
from app.logic.pod import *

# the models
from app.models.pod import *

class TestCoffeePod(TestConfig):

	def test_addPodProductType(self):
		''' add new 'PodProductType' then get it with filters then delete it'''
		
		# add new ProductType
		ProductType = addPodProductType(name='test')
		self.assertTrue(ProductType, 'add ProductType failed')

		# check in the database
		result = PodProductType.query.filter_by(name='test').first()
		self.assertTrue(result, 'add ProductType failed')

		# try get it with the getters
		#

		# all the ProductTypes
		result = getPodProductType()
		self.assertTrue(result, 'Get ProductType failed')
		self.assertEqual(len(result), 1, 'wrong length of ProductTypes')

		# filter with id
		result = getPodProductType(id=ProductType.id)
		self.assertTrue(result, 'Get ProductType failed by id')

		# filter with name
		result = getPodProductType(name=ProductType.name)
		self.assertTrue(result, 'Get ProductType failed by name')

		# try delete it 
		result = deletePodProductType(id=ProductType.id)
		self.assertTrue(result, 'delete ProductType failed')

		# check in the database
		result = PodProductType.query.filter_by(name='test').first()
		self.assertFalse(result, 'not deleted')
	
	def test_addCoffeeFlavor(self):
		''' add new 'CoffeeFlavor' then get it with filters then delete it'''
		
		# add new CoffeeFlavor
		Flavor = addCoffeeFlavor(name='test')
		self.assertTrue(Flavor, 'add Flavor failed')

		# check in the database
		result = CoffeeFlavor.query.filter_by(name='test').first()
		self.assertTrue(result, 'add Flavor failed')

		# try get it with the getters
		#

		# all the Coffee Flavor
		result = getCoffeeFlavor()
		self.assertTrue(result, 'Get Flavor failed')
		self.assertEqual(len(result), 1, 'wrong length of CoffeeFlavors')

		# filter with id
		result = getCoffeeFlavor(id=Flavor.id)
		self.assertTrue(result, 'Get Flavor failed by id')

		# filter with name
		result = getCoffeeFlavor(name=Flavor.name)
		self.assertTrue(result, 'Get Flavor failed by name')

		# try delete it 
		result = deleteCoffeeFlavor(id=Flavor.id)
		self.assertTrue(result, 'delete Flavor failed')

		# check in the database
		result = CoffeeFlavor.query.filter_by(name='test').first()
		self.assertFalse(result, 'not deleted')

	def test_addPodPackSize(self):
		''' add new 'PodPackSize' then get it with filters then delete it'''
		
		# add new PodPackSize
		size = addPodPackSize(size=18)
		self.assertTrue(size, 'add size failed')

		# check in the database
		result = PodPackSize.query.filter_by(size=18).first()
		self.assertTrue(result, 'add size failed')

		# try get it with the getters
		#

		# all the Coffee Flavor
		result = getPodPackSize()
		self.assertTrue(result, 'Get size failed')
		self.assertEqual(len(result), 1, 'wrong length of PodPackSize')

		# filter with id
		result = getPodPackSize(id=size.id)
		self.assertTrue(result, 'Get size failed by id')

		# filter with size
		result = getPodPackSize(size=size.size)
		self.assertTrue(result, 'Get size failed by name')

		# try delete it 
		result = deletePodPackSize(id=size.id)
		self.assertTrue(result, 'delete size failed')

		# check in the database
		result = PodPackSize.query.filter_by(size=18).first()
		self.assertFalse(result, 'not deleted')
	
class TestCoffeePod2(TestConfig):
	
	def test_addCoffeePod(self):
		''' add new CoffeePod then get it with the filters and lastly delete it'''

		# first add the dependencies
		#

		# add new ProductType
		ProductType = addPodProductType(name='test')
		self.assertTrue(ProductType, 'add ProductType failed')

		# add new CoffeeFlavor
		Flavor = addCoffeeFlavor(name='test')
		self.assertTrue(Flavor, 'add Flavor failed')

		# add new PodPackSize
		size = addPodPackSize(size=18)
		self.assertTrue(size, 'add size failed')

		# now add the CoffeePod
		object = addCoffeePod(name='test', productType='test', coffeeFlavor='test', podPackSize=18)
		self.assertTrue(object, 'add CoffeePod failed')

		# check the database
		result = CoffeePod.query.filter_by(name='test').first()
		self.assertTrue(result, 'add CoffeePod failed')

		# now use getters
		#

		# all the Coffee pod
		result = getCoffeePod()
		self.assertTrue(result, 'Get Coffee pod failed')
		self.assertEqual(len(result), 1, 'wrong length of Coffee pods')

		# filter with id
		result = getCoffeePod(id=object.id)
		self.assertTrue(result, 'Get Coffee pod failed by id')

		# filter with name
		result = getCoffeePod(name=object.name)
		self.assertTrue(result, 'Get Coffee pod failed by name')

		# try delete it 
		result = deleteCoffeePod(id=object.id)
		self.assertTrue(result, 'delete Coffee pod failed')

		# check in the database
		result = CoffeePod.query.filter_by(name='test').first()
		self.assertFalse(result, 'not deleted')

	def test_deletedata1(self):
		''' test the 'delete functionality' (delete one of the dependencies must delete the )'''

		# first add the dependencies
		#

		# add new ProductType
		ProductType = addPodProductType(name='test')
		self.assertTrue(ProductType, 'add ProductType failed')

		# add new CoffeeFlavor
		Flavor = addCoffeeFlavor(name='test')
		self.assertTrue(Flavor, 'add Flavor failed')

		# add new PodPackSize
		size = addPodPackSize(size=18)
		self.assertTrue(size, 'add size failed')

		# now add the CoffeePod
		object = addCoffeePod(name='test', productType='test', coffeeFlavor='test', podPackSize=18)
		self.assertTrue(object, 'add CoffeePod failed')

		# delete the ProductType
		result = deletePodProductType(id=ProductType.id)
		self.assertTrue(result, 'delete ProductType failed')

		# check the if CoffeePod was deleted
		result = CoffeePod.query.all()
		self.assertFalse(result, 'delete CoffeePod failed')
	
	def test_deletedata2(self):
		''' test the 'delete functionality' (delete one of the dependencies must delete the )'''

		# first add the dependencies
		#

		# add new ProductType
		ProductType = addPodProductType(name='test')
		self.assertTrue(ProductType, 'add ProductType failed')

		# add new CoffeeFlavor
		Flavor = addCoffeeFlavor(name='test')
		self.assertTrue(Flavor, 'add Flavor failed')

		# add new PodPackSize
		size = addPodPackSize(size=18)
		self.assertTrue(size, 'add size failed')

		# now add the CoffeePod
		object = addCoffeePod(name='test', productType='test', coffeeFlavor='test', podPackSize=18)
		self.assertTrue(object, 'add CoffeePod failed')

		# delete the CoffeeFlavor
		result = deleteCoffeeFlavor(id=Flavor.id)
		self.assertTrue(result, 'delete Flavor failed')

		# check the if CoffeePod was deleted
		result = CoffeePod.query.all()
		self.assertFalse(result, 'delete CoffeePod failed')

	def test_deletedata3(self):
		''' test the 'delete functionality' (delete one of the dependencies must delete the )'''

		# first add the dependencies
		#

		# add new ProductType
		ProductType = addPodProductType(name='test')
		self.assertTrue(ProductType, 'add ProductType failed')

		# add new CoffeeFlavor
		Flavor = addCoffeeFlavor(name='test')
		self.assertTrue(Flavor, 'add Flavor failed')

		# add new PodPackSize
		size = addPodPackSize(size=18)
		self.assertTrue(size, 'add size failed')

		# now add the CoffeePod
		object = addCoffeePod(name='test', productType='test', coffeeFlavor='test', podPackSize=18)
		self.assertTrue(object, 'add CoffeePod failed')

		# delete the PodPackSize
		result = deletePodPackSize(id=size.id)
		self.assertTrue(result, 'delete size failed')

		# check the if CoffeePod was deleted
		result = CoffeePod.query.all()
		self.assertFalse(result, 'delete CoffeePod failed')
