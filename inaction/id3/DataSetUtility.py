import operator
from numpy import *

class DataSetUtility:

	@staticmethod
	def getIfOutputLabelsAreTheSame( dataSet ):

		firstLabel = dataSet[0][-1]

		size = len( dataSet )

		for i in range( size ):

			if ( firstLabel != dataSet[i][-1] ):
				return False, None

		return True, firstLabel


	@staticmethod
	def getMajorityOutputLabel( dataSet ):

		labelCounts = {}

		size = len( dataSet )
		
		for i in range( size ):

			label = dataSet[i][-1]

			labelCounts[ label ] = labelCounts.get( label, 0 ) + 1

		sortedLabelCounts = sorted( labelCounts.items(), operator.itemgetter( 1 ), reverse = True )

		return sortedLabelCounts[0][0]
