import csv
from numpy import *

class CancerDataProcessor:

	@staticmethod
	def getFeatureNames():

		return [

			'Mean radius', 'Mean texture', 'Mean perimeter', 'Mean area', 'Mean smoothness', 
			'Mean compactness', 'Mean concavity', 'Mean concave points', 'Mean symmetry', 'Mean fractal dimension',

			'SE radius', 'SE texture', 'SE perimeter', 'SE area', 'SE smoothness', 
			'SE compactness', 'SE concavity', 'SE concave points', 'SE symmetry', 'SE fractal dimension',

			'Worst radius', 'Worst texture', 'Worst perimeter', 'Worst area', 'Worst smoothness', 
			'Worst compactness', 'Worst concavity', 'Worst concave points', 'Worst symmetry', 'Worst fractal dimension'

		]

	@staticmethod
	def getDataFromCSVFile( filePath ):

		#E:\projects\python\inaction\id3\cancerData\wdbc.data
		with open( filePath, 'r' ) as fileHandler:
			reader = csv.reader( fileHandler )
			rawData = list( reader )

			structuredData = []
			for r in rawData:
				sR = [ float( i ) for i in r[ 2 : ] ]
				sR.append( r[ 1 ] )
				structuredData.append( sR )

		return structuredData

	@staticmethod
	def segmentData( structuredData ):

		r = len( structuredData )
		c = len( structuredData[0] )

		numData = zeros( ( r, c - 1 ) )
		i = 0;
		for r in structuredData:
			numData[i] = r[0:-1]
			i += 1

		return numData

	@staticmethod
	def replaceWithSegmentClassification( structuredData, classifiedSegData ):

		rowNum = len( structuredData )
		labelIndex = len( structuredData[0] ) - 1

		for i in range( rowNum ):
			structuredData[i] = classifiedSegData[i].tolist() + [ structuredData[i][ labelIndex ] ]

		return structuredData

	"""
	k =  number of steps to create in data

	for each row we get range, then devide the range by k. And feature is classified from 0 to k-1
	"""
	@staticmethod
	def segmentClassification( segmentData, k = 5 ):

		cols = segmentData.shape[1]
		featureSteps = zeros( cols )

		for i in range( cols ):

			rangeOfF = max( segmentData[ :, i ] ) - min( segmentData[ :, i ] )
			step = rangeOfF / k
			print ( "range: {0}, step: {1}".format( rangeOfF, step ) )
			segmentData[ :, i ] = around( segmentData[ :, i ] / step );
			featureSteps[i] = step 

		return segmentData, featureSteps

	@staticmethod
	def classifyFeatureVal( featureSteps, value, fIndex ):
		return around( value / featureSteps[ fIndex ] )
	@staticmethod
	def classifyFeatureVals( featureSteps, values ):
		return around( values / featureSteps )