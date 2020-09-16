""" all coffee machine related db-models """

# the database instance
from . import db

class CoffeeMachine(db.Model):
	""" 'Coffee Machine' Model representation """

	__name__ = 'CoffeeMachine'
	__tablename__ = 'coffee_machine'

	id = db.Column(db.Integer, primary_key=True)

	# the name of the Coffee Machine product
	name = db.Column(db.String(50), nullable=False, unique=True)

	# the type of this 'Coffee Machine' - access with backref = 'type'
	ProductType = db.Column('product_type', db.Integer, db.ForeignKey('coffee_machine_product_type.id'), nullable=False)

	# has Water Line or not ?
	WaterLine = db.Column('water_line', db.Boolean, nullable=False)

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'name':self.name, 'WaterLine':self.WaterLine, 'ProductType':self.type.name}

class CoffeeMachineProductType(db.Model):
	""" the types of the coffee machines (LARGE, SMALL, ect)"""

	__name__ = 'CoffeeMachine'
	__tablename__ = 'coffee_machine_product_type'

	id = db.Column(db.Integer, primary_key=True)

	# the name of the 'Coffee Machine' type
	name = db.Column(db.String(30), nullable=False, unique=True)

	# the Coffee Machines with this type
	CoffeeMachines = db.relationship('CoffeeMachine', backref='type', lazy='dynamic', cascade = "all, delete, delete-orphan")

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'name':self.name, 'CoffeeMachines':[i.name for i in self.CoffeeMachines]}
