""" the functionality related to 'CoffeeMachine' model"""

from ..models import db, CoffeeMachine, CoffeeMachineProductType

# CoffeeMachine model
# 
def addCoffeeMachine(name, WaterLine, ProductType):
	""" add new CoffeeMachine.
	perm: name        = the name of the CoffeeMachine product
	perm: WaterLine   = True or False
	perm: ProductType = ProductType name as string
	return 'CoffeeMachine' object if success else None"""

	# first check the ProductType
	productType = CoffeeMachineProductType.query.filter_by(name=ProductType).first()

	# not valid ProductType name
	if not productType:
		return None

	# add new CoffeeMachine
	machine = CoffeeMachine(name=name, WaterLine=WaterLine)

	# add to session
	db.session.add(machine)

	# add the machine to this type table
	productType.CoffeeMachines.append(machine)

	# save
	db.commit()

	# success
	return machine

def getCoffeeMachine(id=None, name=None, WaterLine=None):
	""" return the CoffeeMachine object or None if not exist
		return a list of all CoffeeMachine if no filters passed.
		return one object if filtered by 'id'"""

	# no filters 
	if not any([id, name, WaterLine]):
		return CoffeeMachine.query.all()
	
	# filter by id
	if id:
		return CoffeeMachine.query.get(id)
	
	# other filters
	baseQuery = CoffeeMachine.query

	if name:
		baseQuery = baseQuery.filter_by(name=name)
	if WaterLine:
		baseQuery = baseQuery.filter_by(WaterLine=WaterLine)
	
	# execute the query
	return baseQuery.all()

def deleteCoffeeMachine(id):
	""" delete the CoffeeMachine with passed id
		return True if success else False"""

	object = CoffeeMachine.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True

# CoffeeMachineProductType model
# 
def addCoffeeMachineProductType(name):
	""" add new CoffeeMachineProductType.
	perm: name = the name of the ProductType (must be unique)
	return 'CoffeeMachineProductType' object if success else None"""

	# check if the name already exists
	object = CoffeeMachineProductType.query.filter_by(name=name).first()

	if object:
		# already exists
		return None
	
	object = CoffeeMachineProductType(name=name)

	# add to session
	db.session.add(object)
	
	# save
	db.commit()

	# success
	return object

def getCoffeeMachineProductType(id=None, name=None):
	""" return the 'CoffeeMachineProductType' object or None if not exist
		return a list of all CoffeeMachine if no filters passed.
		return one object if filtered by 'id'"""

	# query all
	if not any([id, name]):
		return CoffeeMachineProductType.query.all()

	if id:
		# one object
		return CoffeeMachineProductType.query.get(id)
	
	if name:
		return CoffeeMachineProductType.query.filter_by(name=name)

def deleteCoffeeMachineProductType(id=None):
	''' delete the 'Coffee Machine Type'
		return True if success else False
		Warning: the will delete connected 'CoffeeMachine' '''
	object = CoffeeMachineProductType.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True