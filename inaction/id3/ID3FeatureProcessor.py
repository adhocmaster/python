from numpy import *
from EntropyProcessor import *

""" works both with NDArray and lists """
class ID3FeatureProcessor():

	"""
	returns a dictionary with featureVal as keys and list of records/vectors as values.

	"""
	@staticmethod 
	def getSplitedDataSetsForFeature( dataSet, featureCol ):

		fUniqueVals = ID3FeatureProcessor.getFeatureUniqueVals( dataSet, featureCol )

		splittedDictionary = {}

		if type( dataSet ) is list:
			numRecords = len( dataSet )
		else:
			numRecords = dataSet.shape[0]

		for i in range( numRecords ):

			ID3FeatureProcessor.addToSplittedDictionary( splittedDictionary, dataSet[i], featureCol )

		return splittedDictionary


	@staticmethod 
	def getFeatureUniqueVals( dataSet, featureCol ):

		#return set( dataSet[ :, featureCol ] ) doesn't work with lists

		return [  r[ featureCol] for r in dataSet ] # works for both lists and ndarray

	@staticmethod 
	def addToSplittedDictionary( splittedDictionary, vector, featureCol ):

		fVal = vector[featureCol]

		listVec = splittedDictionary.get( fVal, [] )

		listVec.append( vector )

		splittedDictionary[ fVal ] = listVec

	@staticmethod
	def getFeatureEntropy( dataSet, featureCol ):

		if  type( dataSet ) is list:
			dataSize = len( dataSet )
		else: 
			dataSize = dataSet.shape[0]

		featureSplitData = ID3FeatureProcessor.getSplitedDataSetsForFeature( dataSet, featureCol )

		entropy = 0.0;

		for key in featureSplitData.keys():

			fVEntropy = EntropyProcessor.getEntropyFromDataSet( featureSplitData[key] )
			fVProbability = float( len( featureSplitData[key] ) ) / dataSize

			#print ( "featureCol: " + str( featureCol ) + " fVEntropy " + str( fVEntropy ) + " fVProbability " + str( fVProbability ) )
			entropy += fVProbability * fVEntropy;

		#print ( "Entropy of feature col " + str( featureCol ) + " is " + str( entropy ) )

		return entropy

	@staticmethod
	def getBestFeature( dataSet, featureNames, reducedFeatureNames ):

		totalEntropy = EntropyProcessor.getEntropyFromDataSet( dataSet )

		bestInformationGain = 0.0

		featureCols = len( dataSet[0] ) - 1

		tempGain = 0.0
		bestFeatureCol = -1

		for i in range( len( reducedFeatureNames ) ):

			fName = reducedFeatureNames[i]

			actualIndex = featureNames.index( fName )

			iEntropy = ID3FeatureProcessor.getFeatureEntropy( dataSet, actualIndex )

			tempGain = totalEntropy - iEntropy

			print ( "featureCol: " + str( actualIndex ) + "entropy: " + str( iEntropy ) + " tempGain: " + str( tempGain ) )

			if ( tempGain > bestInformationGain ):

				bestInformationGain = tempGain
				bestFeatureCol = actualIndex

		return featureNames[bestFeatureCol], bestFeatureCol



		