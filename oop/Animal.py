from abc import ABCMeta, abstractmethod

class Animal( object ):

	__metaclass__ = ABCMeta

	baseSalePrice = 0

	def __init__( self, breed, soldOn ):

		self.breed = breed
		self.soldOn = soldOn

	def getBreed( self ):
		return self.breed

	def getSoldOn( self ):
		return self.soldOn

	def getSalePrice( self ):
		return baseSalePrice

	def __str__( self ):
		return "[ " + "breed: " + self.breed  + "" \
				 "soldOn: " +  self.soldOn.strftime( '%m/%d/%Y' )  + "" \
				 "salePrice: " + str( self.baseSalePrice )  + "" \
				 " ]"

	@abstractmethod
	def speak( self ):
		pass

