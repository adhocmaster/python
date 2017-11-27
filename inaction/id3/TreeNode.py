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

		return self.fValueMap[ fValueLabel ]


	def printNode( self ):
		print( "Node Name: " + self.fName )

		for key in fValueMap.keys():

			print( "feature label: " + str( key ) )

			v = fValueMap[key]

			if type( v ) is TreeNode:
				v.printNode()
			else:
				print( "output level: " + str( v ) )

