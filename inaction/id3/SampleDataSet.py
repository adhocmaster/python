from numpy import *

def createSampleDataSet():
	dataSet = [
		[ 1, 1, 'yes' ],
		[ 1, 1, 'yes' ],
		[ 1, 0, 'no' ],
		[ 0, 1, 'no' ],
		[ 0, 1, 'no' ],
	]

	featureNames = [ 'no surfacing', 'flippers' ]

	return dataSet, featureNames

def createSampleDataSetNdArr():

	dataSet, featureNames = createSampleDataSet()
	return asarray( dataSet ), featureNames