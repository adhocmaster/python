from numpy import *
import os
import re
import classifier


def img2vector( filePath ):

	#print ( " parsing file: " + filePath )

	outputV = zeros( 1024 )

	fh = open( filePath )

	for i in range( 32 ):

		line = fh.readline()

		for j in range(32):
			outputV[ 32 * i + j] = int( line[j] )

	return outputV

def getTrainingSet( dirPath ):

	# dirPath = "E:\\projects\\python\\manning\\machinelearninginaction\\Ch02\\trainingDigits"

	print ( " parsing dirPath: " + dirPath )

	labels = []

	trainingFileList = os.listdir( dirPath )

	numFiles = len( trainingFileList )

	print ( "files found " + str( numFiles ) )

	data = zeros ( ( numFiles, 1024 ) )

	for i in range( numFiles ):

		if ( i % 100 ) == 0:
			print ( " percentage trained: {:.2%}".format( i / numFiles ) )

		data[i] = img2vector( dirPath + '/' + trainingFileList[i] )

		labels.append( getLabelFromFileName( trainingFileList[i] ) )


	return data, labels


def getLabelFromFileName( fileName ):

	m = re.match( r'.*\\?(\d)_.*\.txt', fileName )
	if m:
		return m.group( 1 )

	raise ValueError( "could not parse label from filename " + filename )


def matchDigit( testFilePath, data, labels, k ):

 	#testFilePath = "E:\\projects\\python\\manning\\machinelearninginaction\\Ch02\\testDigits\\0_0.txt"

	inputV = img2vector( testFilePath )

	return classifier.getLabelFromVectorKnnClassifier( inputV, data, labels, k )


def testErrorRate( testDirPath, data, labels, k ):

	print ( " parsing testDirPath: " + testDirPath )

	testFileList = os.listdir( testDirPath ) 

	numTest = len ( testFileList )

	print ( "files found " + str( numTest ) )

	wrongCount = 0

	for i in range ( numTest ):

		if ( i % 20 ) == 0:
			print ( " percentage tested: {:.2%}".format( i / numTest ) )
		predictTedDigit = matchDigit( testDirPath + '/' + testFileList[i], data, labels, k )

		if predictTedDigit != getLabelFromFileName( testFileList[i] ):

			wrongCount += 1;

	print ( " total wrong: {0} out of: {1}".format( wrongCount, numTest ) )

	return ( wrongCount * 100.0 ) / numTest

