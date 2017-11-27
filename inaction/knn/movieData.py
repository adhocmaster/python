from numpy import *
import operator

def createDataSet():
	group = array( [

			[ 1.0, 1.1 ],
			[ 1.0, 1.0 ],
			[ 0, 0 ],
			[ 0, 0.1]

		] )

	labels = [ 'A', 'A', 'B', 'B' ]

	return group, labels

def classify( inX, dataSet, labels, k ):

	sqDistances = getSqDistances( inX, dataSet )

	orderedNearestIndices = getOrderByNearness( sqDistances )

	classCount = getClassNearestKCount( labels, orderedNearestIndices, k )

	#print( classCount )

	sortedClassCount = getSortedClassCount( classCount );

	return sortedClassCount[0][0]


def getSqDistances( inX, dataSet ):

	nRows = dataSet.shape[0]

	spannedX = tile( inX, ( nRows, 1) )

	diffXY = spannedX - dataSet

	sqDiffXY = diffXY ** 2

	sqDistances = sqDiffXY.sum( axis = 1 )

	return sqDistances


def getOrderByNearness( sqDistances ):

	return sqDistances.argsort()

def	getClassNearestKCount( labels, orderedNearestIndices, k ):

	classCount = {}

	for i in range( k ):
		ithNearestLabel = labels[ orderedNearestIndices[i] ]
		classCount[ ithNearestLabel ] = classCount.get( ithNearestLabel, 0 ) + 1

	return classCount

def getSortedClassCount( classCount ):

	return sorted( classCount.items(), key = operator.itemgetter(1), reverse = True )


