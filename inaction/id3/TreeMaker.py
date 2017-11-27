from TreeNode import *
from DataSetUtility import *
from ID3FeatureProcessor import *

class TreeMaker:

	@staticmethod
	def createNode( featureName, featureVals ):

		return TreeNode( featureName, featureVals )

	"""
	dataSet must a split that corresponds to only the parent node
	featureNames: reduced featureNames which are not yet processed
	depth: 0 if tree can grow to maximum level. root is considered to have level 1
	curLevel: must always be 0

	"""
	@staticmethod
	def createTree( dataSet, featureNames, reducedFeatureNames, depth = 0, curLevel = 0 ):

		isLeaf, outputLabel = TreeMaker.getIfItsALeaf( dataSet, featureNames, depth, curLevel )

		print( "isLeaf: " + str( isLeaf ) + " outputLabel: " + str( outputLabel ) )

		if True == isLeaf:
			return isLeaf, outputLabel

		#I am a new node


		bestFeatureName, bestFeatureIndex = ID3FeatureProcessor.getBestFeature( dataSet, featureNames, reducedFeatureNames )

		print ( "best feature: " + bestFeatureName + " index: " + str( bestFeatureIndex ) )

		featureVals = ID3FeatureProcessor.getFeatureUniqueVals( dataSet, bestFeatureIndex )

		meNode = TreeMaker.createNode( bestFeatureName, featureVals )

		featureSplitData = ID3FeatureProcessor.getSplitedDataSetsForFeature( dataSet, bestFeatureIndex )

		featureNamesWithoutMe = list( featureNames ) # keep oroginal list untouched
		featureNamesWithoutMe.remove( bestFeatureName )

		if depth != 0:
			curLevel += 1


		for fVal in featureSplitData.keys():

			isLeaf, outputLabelOrTree = TreeMaker.createTree( featureSplitData[ fVal ], featureNames, featureNamesWithoutMe, depth, curLevel )


			meNode.addValue( fVal, outputLabelOrTree )

		return False, meNode

	"""
	leaf conditions:
		1. single output label
		2. no feature left
		3. currentLevel crosses depth
	"""
	@staticmethod
	def getIfItsALeaf( dataSet, featureNames, depth, curLevel ):

		isLeaf, outputLabel = DataSetUtility.getIfOutputLabelsAreTheSame( dataSet ) 

		if True == isLeaf:
			print( "outputLabels are the same: " + str( outputLabel ) )
			return isLeaf, outputLabel

		if len( featureNames ) == 0  or curLevel > depth:
			print( "featureNames empty: " + str( featureNames ) + " or curLevel crossed depth: " + str( outputLabel ) )

			return True, DataSetUtility.getMajorityOutputLabel( dataSet )

		return False, None





