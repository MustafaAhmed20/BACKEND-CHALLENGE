""" the functionality related to 'CoffeePod' model"""
from ..models import db, CoffeePod, PodProductType, CoffeeFlavor, PodPackSize

# CoffeePod model
# 
def addCoffeePod(name, productType, coffeeFlavor, podPackSize):
	""" add new CoffeeMachine.
	perm: name        = the name of the CoffeePod product
	perm: coffeeFlavor= the name of the coffeeFlavor product
	perm: podPackSize = Pack Size of this product
	return 'CoffeePod' object if success else None"""

	# first check the dependencies
	productType = PodProductType.query.filter_by(name=productType).first()
	
	coffeeFlavor = CoffeeFlavor.query.filter_by(name=coffeeFlavor).first()
	
	podPackSize = PodPackSize.query.filter_by(size=podPackSize).first()

	# not valid dependencies
	if not all([productType, coffeeFlavor, podPackSize]):
		return None

	# add new CoffeePod
	pod = CoffeePod(name=name)

	# add to session
	db.session.add(pod)

	# add the pod to the dependencies
	productType.coffeePods.append(pod)
	coffeeFlavor.coffeePods.append(pod)
	podPackSize.coffeePods.append(pod)

	# save
	db.session.commit()

	# success
	return pod

def getCoffeePod(id=None, name=None):
	""" return the CoffeePod object or None if not exist
		return a list of all CoffeePod if no filters passed.
		return one object if filtered by 'id'"""

	# no filters 
	if not any([id, name]):
		return CoffeePod.query.all()
	
	# filter by id
	if id:
		return CoffeePod.query.get(id)
	
	# filter by name
	return CoffeePod.query.filter_by(name=name).all()

def deleteCoffeePod(id):
	""" delete the CoffeePod with passed id
		return True if success else False"""

	object = CoffeePod.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True

# PodProductType model
# 
def addPodProductType(name):
	""" add new PodProductType.
	perm: name = the name of the ProductType (must be unique)
	return 'PodProductType' object if success else None"""

	# check if the name already exists
	object = PodProductType.query.filter_by(name=name).first()

	if object:
		# already exists
		return None
	
	object = PodProductType(name=name)

	# add to session
	db.session.add(object)
	
	# save
	db.session.commit()

	# success
	return object

def getPodProductType(id=None, name=None):
	""" return the 'PodProductType' object or None if not exist
		return a list of all PodProductType if no filters passed.
		return one object if filtered by 'id'"""

	# query all
	if not any([id, name]):
		return PodProductType.query.all()

	if id:
		# one object
		return PodProductType.query.get(id)
	
	if name:
		return PodProductType.query.filter_by(name=name).all()

def deletePodProductType(id=None):
	''' delete the 'Pod Product Type'
		return True if success else False
		Warning: the will delete connected 'CoffeePod' '''
	object = PodProductType.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True

# CoffeeFlavor model
# 
def addCoffeeFlavor(name):
	""" add new CoffeeFlavor.
	perm: name = the name of the CoffeeFlavor (must be unique)
	return 'CoffeeFlavor' object if success else None"""

	# check if the name already exists
	object = CoffeeFlavor.query.filter_by(name=name).first()

	if object:
		# already exists
		return None
	
	object = CoffeeFlavor(name=name)

	# add to session
	db.session.add(object)
	
	# save
	db.session.commit()

	# success
	return object

def getCoffeeFlavor(id=None, name=None):
	""" return the 'CoffeeFlavor' object or None if not exist
		return a list of all CoffeeFlavor if no filters passed.
		return one object if filtered by 'id'"""

	# query all
	if not any([id, name]):
		return CoffeeFlavor.query.all()

	if id:
		# one object
		return CoffeeFlavor.query.get(id)
	
	if name:
		return CoffeeFlavor.query.filter_by(name=name).all()

def deleteCoffeeFlavor(id=None):
	''' delete the 'CoffeeFlavor'
		return True if success else False
		Warning: the will delete connected 'CoffeePod' '''
	object = CoffeeFlavor.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True

# PodPackSize model
# 
def addPodPackSize(size):
	""" add new PodPackSize.
	perm: size = the size of the pack (must be unique)
	return 'PodPackSize' object if success else None"""

	# check if the size already exists
	object = PodPackSize.query.filter_by(size=size).first()

	if object:
		# already exists
		return None
	
	object = PodPackSize(size=size)

	# add to session
	db.session.add(object)
	
	# save
	db.session.commit()

	# success
	return object

def getPodPackSize(id=None, size=None):
	""" return the 'PodPackSize' object or None if not exist
		return a list of all PodPackSize if no filters passed.
		return one object if filtered by 'id' or size"""

	# query all
	if not any([id, size]):
		return PodPackSize.query.all()

	if id:
		# one object
		return PodPackSize.query.get(id)
	
	if size:
		return PodPackSize.query.filter_by(size=size).first()

def deletePodPackSize(id=None):
	''' delete the 'PodPackSize'
		return True if success else False
		Warning: the will delete connected 'CoffeePod' '''
	object = PodPackSize.query.get(id)

	if not object:
		return False
	
	# delete the object
	db.session.delete(object)
	db.session.commit()	

	# success
	return True

