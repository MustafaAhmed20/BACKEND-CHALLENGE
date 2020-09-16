from flask_sqlalchemy import SQLAlchemy

# the database instance
db =  SQLAlchemy()

# import all the models 
from .machine import *
from .pod import *


def defaultData(app, db):
	""" the default data described in the challenge"""
	
	# you need to push context to add the data
	app.app_context().push()

	# CoffeeMachineProductType model
	#
	large = CoffeeMachineProductType(name='COFFEE_MACHINE_LARGE')
	small = CoffeeMachineProductType(name='COFFEE_MACHINE_SMALL')
	espresso = CoffeeMachineProductType(name='ESPRESSO_MACHINE')

	db.session.add_all([large, small, espresso])
	db.session.commit()


	# CoffeeMachine model
	#
	c1= CoffeeMachine(name='CM001-base model', WaterLine=False, ProductType=small.id)
	c2= CoffeeMachine(name='CM002-premium model', WaterLine=False, ProductType=small.id)
	c3= CoffeeMachine(name='CM003-deluxe mode', WaterLine=True, ProductType=small.id)

	db.session.add_all([c1, c2, c3])
	db.session.commit()

	c4= CoffeeMachine(name='CM101-base model', WaterLine=False, ProductType=large.id)
	c5= CoffeeMachine(name='CM102-premium model', WaterLine=True, ProductType=large.id)
	c6= CoffeeMachine(name='CM103-deluxe mode', WaterLine=True, ProductType=large.id)

	db.session.add_all([c4, c5, c6])
	db.session.commit()

	c7= CoffeeMachine(name='EM001-base model', WaterLine=False, ProductType=espresso.id)
	c8= CoffeeMachine(name='EM002-premium model', WaterLine=False, ProductType=espresso.id)
	c9= CoffeeMachine(name='EM003-deluxe mode', WaterLine=True, ProductType=espresso.id)

	db.session.add_all([c7, c8, c9])
	db.session.commit()

	# ....
	# CoffeePod dependencies
	size1 = PodPackSize(size=12)
	size2 = PodPackSize(size=36)
	size3 = PodPackSize(size=60)
	size4 = PodPackSize(size=84)

	db.session.add_all([size1,size2, size3, size4])
	db.session.commit()

	flavor1 = CoffeeFlavor(name='COFFEE_FLAVOR_VANILLA')
	flavor2 = CoffeeFlavor(name='COFFEE_FLAVOR_CARAMEL')
	flavor3 = CoffeeFlavor(name='COFFEE_FLAVOR_PSL')
	flavor4 = CoffeeFlavor(name='COFFEE_FLAVOR_MOCHA')
	flavor5 = CoffeeFlavor(name='COFFEE_FLAVOR_HAZELNUT')

	db.session.add_all([flavor1, flavor2, flavor3, flavor4, flavor5])
	db.session.commit()

	type1 = PodProductType(name='COFFEE_POD_LARGE')
	type2 = PodProductType(name='COFFEE_POD_SMALL')
	type3 = PodProductType(name='ESPRESSO_POD')

	db.session.add_all([type1, type2, type3])
	db.session.commit()

	db.session.add_all([
	# the pods
	CoffeePod(name='CP001', productType=type2.id, coffeeFlavor=flavor1.id, podPackSize=size1.id),
	CoffeePod(name='CP003', productType=type2.id, coffeeFlavor=flavor1.id, podPackSize=size2.id),

	CoffeePod(name='CP011', productType=type2.id, coffeeFlavor=flavor2.id, podPackSize=size1.id),
	CoffeePod(name='CP013', productType=type2.id, coffeeFlavor=flavor2.id, podPackSize=size2.id),

	CoffeePod(name='CP021', productType=type2.id, coffeeFlavor=flavor3.id, podPackSize=size1.id),
	CoffeePod(name='CP023', productType=type2.id, coffeeFlavor=flavor3.id, podPackSize=size2.id),

	CoffeePod(name='CP031', productType=type2.id, coffeeFlavor=flavor4.id, podPackSize=size1.id),
	CoffeePod(name='CP033', productType=type2.id, coffeeFlavor=flavor4.id, podPackSize=size2.id),

	CoffeePod(name='CP041', productType=type2.id, coffeeFlavor=flavor5.id, podPackSize=size1.id),
	CoffeePod(name='CP043', productType=type2.id, coffeeFlavor=flavor5.id, podPackSize=size2.id),

	# large type
	CoffeePod(name='CP101', productType=type1.id, coffeeFlavor=flavor1.id, podPackSize=size1.id),
	CoffeePod(name='CP103', productType=type1.id, coffeeFlavor=flavor1.id, podPackSize=size2.id),

	CoffeePod(name='CP111', productType=type1.id, coffeeFlavor=flavor2.id, podPackSize=size1.id),
	CoffeePod(name='CP113', productType=type1.id, coffeeFlavor=flavor2.id, podPackSize=size2.id),

	CoffeePod(name='CP121', productType=type1.id, coffeeFlavor=flavor3.id, podPackSize=size1.id),
	CoffeePod(name='CP123', productType=type1.id, coffeeFlavor=flavor3.id, podPackSize=size2.id),

	CoffeePod(name='CP131', productType=type1.id, coffeeFlavor=flavor4.id, podPackSize=size1.id),
	CoffeePod(name='CP133', productType=type1.id, coffeeFlavor=flavor4.id, podPackSize=size2.id),

	CoffeePod(name='CP141', productType=type1.id, coffeeFlavor=flavor5.id, podPackSize=size1.id),
	CoffeePod(name='CP143', productType=type1.id, coffeeFlavor=flavor5.id, podPackSize=size2.id),

	# espresso type
	CoffeePod(name='EP003', productType=type3.id, coffeeFlavor=flavor1.id, podPackSize=size2.id),
	CoffeePod(name='EP005', productType=type3.id, coffeeFlavor=flavor1.id, podPackSize=size3.id),
	CoffeePod(name='EP007', productType=type3.id, coffeeFlavor=flavor1.id, podPackSize=size4.id),

	CoffeePod(name='EP013', productType=type3.id, coffeeFlavor=flavor2.id, podPackSize=size2.id),
	CoffeePod(name='EP015', productType=type3.id, coffeeFlavor=flavor2.id, podPackSize=size3.id),
	CoffeePod(name='EP017', productType=type3.id, coffeeFlavor=flavor2.id, podPackSize=size4.id),

	])



	
	# save
	db.session.commit()

