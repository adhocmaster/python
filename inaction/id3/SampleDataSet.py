from numpy import *

def createSampleDataSet():
	dataSet = [
		[ 1, 1, 'yes' ],
		[ 1, 1, 'yes' ],
		[ 1, 0, 'no' ],
		[ 0, 1, 'no' ],
		[ 0, 1, 'maybe' ],
	]

	featureNames = [ 'no surfacing', 'flippers' ]

	return dataSet, featureNames

def createSampleDataSetNdArr():

	dataSet, featureNames = createSampleDataSet()
	return asarray( dataSet ), featureNames

def getLenseDataSet( filePath ):

	fileHandler = open( filePath )

	lenses = [ line.strip().split( '\t' ) for line in  fileHandler.readlines() ]

	labels = [ 'age', 'prescript', 'astigmatic', 'tearRate' ]

	return lenses, labels