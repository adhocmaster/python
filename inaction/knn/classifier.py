from numpy import *
import operator

# every axis in data must have the same number of numbers as the input vector
def getLabelFromVectorKnnClassifier( inputV, data, labels, k ):

	inputTile = tile( inputV, (data.shape[0], 1) );

	difTile = data - inputTile;

	difSqTile = difTile ** 2

	difSqTileSum = difSqTile.sum( 1 ) # row sum

	distanceV = difSqTileSum ** 0.5

	distanceSortedIndex = distanceV.argsort()

	topClassesCount = getKTopNeighbourClassesWithCount( labels, distanceSortedIndex, k )

	return getMostMatchedClass( topClassesCount )


def getKTopNeighbourClassesWithCount( labels, distanceSortedIndex, k ):

	topClassesCount = {}

	for i in range( k ):
		voteLabel = labels[ distanceSortedIndex[i] ]
		topClassesCount[ voteLabel ] = topClassesCount.get( voteLabel, 0 ) + 1

	return topClassesCount

def getMostMatchedClass( classesWithCount ):

	sortedClasses = sorted( classesWithCount.items(), key = operator.itemgetter(1), reverse = True )
	return sortedClasses[0][0]

	
