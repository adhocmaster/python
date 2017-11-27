from Animal import Animal

class Dog( Animal ):

	baseSalePrice = 100

	def speak( self ):
		return "Bark"

	def getSalePrice( self ):
		return self.baseSalePrice - 1;

	def setSalePrice( self, newVal ):
		self.baseSalePrice = newVal;
