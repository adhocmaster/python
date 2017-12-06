from pprint import *

class TreeNode( object ):

	""" valuelabels needs to be a list of strings """
	def __init__( self, name, valuelabels ):

		self.fName = name
		self.fValueMap = {}

		self.initValueMaps( valuelabels )


	def initValueMaps( self, valuelabels ):

		for i in range( len( valuelabels ) ):
			self.fValueMap[ valuelabels[i] ] = None


	def addValue( self, fValueLabel, value ):

		self.fValueMap[ fValueLabel ] = value


	def getValue( self, fValueLabel ):

		return self.fValueMap.get( fValueLabel, "invalidLabel" ) 


	def printNode( self ):
		print( "feature Name: " + self.fName )

		for key in self.fValueMap.keys():

			print( "********** label: " + self.fName + " - " + str( key ) + " **********" )

			v = self.fValueMap[key]

			if type( v ) is TreeNode:
				v.printNode()
			else:
				print( "output level: " + str( v ) )

			print( "********** /label: " + self.fName + " - " + str( key ) + " **********" )

	def __str__ ( self ):
		data = "[ fName: " + pprint( self.fName, 1 ) + " Tree: \n" + pprint( self.fValueMap, 2 ) + " ]"
		return data 


