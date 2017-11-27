from numpy import *
import matplotlib
import matplotlib.pyplot as plt

import movieData

def getLinesFromFile( filePath ):
	return open( filePath ).readlines()

def getData( filePath ):

	#"E:\projects\python\manning\machinelearninginaction\Ch02\datingTestSet.txt"


	likeness = getLikeness();

	lines = getLinesFromFile( filePath );

	numLines = len( lines )

	returnMat = zeros( (numLines, 3) )

	labels = []

	labelVals = []

	index = 0

	for line in lines:

		row = line.strip().split( '\t' )

		returnMat[ index, : ] = row[ 0 : 3 ]

		labels.append( row[ -1 ] )

		labelVals.append( int ( likeness.get( row[-1], 0 ) ) )

		index += 1

	return returnMat, labels, labelVals

def getLikeness():
	return  { 'largeDoses' : 1, 'smallDoses' : 2, 'didntLike' : 3 }


def drawPlot( data, labelVals ):
	fig = plt.figure()
	ax = fig.add_subplot( 111 )
	ax.scatter( data[ :, 1 ], data[ :, 2], 15.0 * array( labelVals ), 15.0 * array( labelVals ) )
	plt.show()

def normalize2DAndMinAndRange( data ):

	minVec = data.min(0)
	maxVec = data.max(0)

	rangeVec = maxVec - minVec

	noOfAxes = data.shape[0]

	minData = tile( minVec, ( noOfAxes, 1 ) )
	rangeData = tile( rangeVec, ( noOfAxes, 1 ) )

	return ( data - minData ) / rangeData


def classify( inX, data, labels, k ):
	return movieData.classify( inX, data, labels, k )

def checkPerformance( data, labels, k, testData, testLabels ):

	numRecords = testData.shape[0]

	numIncorrect = 0.0;

	for i in range( numRecords ):

		testLabel = classify( testData[i], data, labels, k )
		if testLabel != testLabels[i]:
			numIncorrect += 1.0
			print ("classifier got " + str(testLabel) + " but actualData " + str(testLabels[i]))
		else:
			print ("data correct")

	#print( numIncorrect )
	return ( numIncorrect * 100 ) / numRecords

