""" all coffee pods related db-models """

# the database instance
from . import db

class CoffeePod(db.Model):
	""" 'Coffee Pod' Model representation """

	__name__ = 'CoffeePod'
	__tablename__ = 'coffee_pod'

	id = db.Column(db.Integer, primary_key=True)

	# the name of the Coffee Pod product
	name = db.Column(db.String(50), nullable=False, unique=True)

	# the type of this 'Coffee Pod' - access with backref = 'type'
	productType = db.Column('product_type', db.Integer, db.ForeignKey('pod_product_type.id'), nullable=False)

	# the coffee flavor of this pod - access with backref = 'flavor'
	coffeeFlavor = db.Column('coffee_flavor', db.Integer, db.ForeignKey('coffee_flavor.id'), nullable=False)

	# the pack size - access with backref = 'size'
	podPackSize = db.Column('pod_pack_size', db.Integer, db.ForeignKey('pod_pack_size.id'), nullable=False)

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'name':self.name, 'productType':self.type.name,
		'coffeeFlavor':self.flavor.name, 'podPackSize':self.size.size}

class PodProductType(db.Model):
	""" the types of the Coffee Pods (LARGE, SMALL, ect)"""

	__name__ = 'PodProductType'
	__tablename__ = 'pod_product_type'

	id = db.Column(db.Integer, primary_key=True)

	# the name of the 'Coffee Pod' type
	name = db.Column(db.String(30), nullable=False, unique=True)

	# the Coffee Pods with this type
	coffeePods = db.relationship('CoffeePod', backref='type', lazy='dynamic', cascade = "all, delete, delete-orphan")

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'name':self.name, 'coffeePods':self.coffeePods}

class CoffeeFlavor(db.Model):
	""" the types of the Coffee flavors (FLAVOR_VANILLA, FLAVOR_CARAMEL, ect)"""

	__name__ = 'CoffeeFlavor'
	__tablename__ = 'coffee_flavor'

	id = db.Column(db.Integer, primary_key=True)

	# the name of the 'Coffee Flavor' 
	name = db.Column(db.String(30), nullable=False, unique=True)

	# the Coffee Pods with this Flavor
	coffeePods = db.relationship('CoffeePod', backref='flavor', lazy='dynamic', cascade = "all, delete, delete-orphan")

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'name':self.name, 'coffeePods':self.coffeePods}

class PodPackSize(db.Model):
	""" the different sizes of pods"""

	__name__ = 'PodPackSize'
	__tablename__ = 'pod_pack_size'

	id = db.Column(db.Integer, primary_key=True)

	# the size of the pack (12, 24, 36, ect)
	size = db.Column(db.Integer, nullable=False, unique=True)

	# the Coffee Pods with this size
	coffeePods = db.relationship('CoffeePod', backref='size', lazy='dynamic', cascade = "all, delete, delete-orphan")

	def toDict(self):
		""" return dict representation of the object """
		return {'id':self.id, 'size':self.size, 'coffeePods':self.coffeePods}
