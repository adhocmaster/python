from TreeNode import *
from DataSetUtility import *
from ID3FeatureProcessor import *

import pickle
import os

import matplotlib.pyplot as plt

class TreeMaker:

	decisionNode = dict( boxstyle = "sawtooth", fc = "0.6" )
	leafNode = dict( boxstyle = "circle", fc = "0.8" )
	rootNode = dict( boxstyle = "roundtooth", fc="cyan")
	featureValStyle = dict( boxstyle = "round", fc="black")
	arrow_args = dict( arrowstyle = "<-" )

	@staticmethod
	def plotNode( nodeTxt, centerPt, parentPt, nodeType ):
		TreeMaker.plotByDFS.axes.annotate( nodeTxt, xy = parentPt, xycoords='axes fraction', 
											xytext=centerPt, textcoords='axes fraction', 
											va="center", ha="center", 
											bbox=nodeType, arrowprops= TreeMaker.arrow_args )

	@staticmethod
	def createNode( featureName, featureVals ):

		return TreeNode( featureName, featureVals )

	"""
	dataSet must a split that corresponds to only the parent node
	featureNames: reduced featureNames which are not yet processed
	depth: 0 if tree can grow to maximum level. root is considered to have level 1
	curLevel: must always be 0

	return: isLeaf, Node

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

	"""
	plots a tree in the rectangle (0,0) and (1,1)
	"""

	@staticmethod
	def plotTree( root ):
		fig = plt.figure( 1, facecolor = 'white' )
		fig.clf()

		TreeMaker.plotByDFS.axes = plt.subplot( 111, frameon = False )

		TreeMaker.plotByDFS.depth = TreeMaker.getTreeDepth( root )

		TreeMaker.plotByDFS.span = TreeMaker.getTreeSpan( root )

		TreeMaker.plotByDFS.yDistance = - 1.0 / ( TreeMaker.plotByDFS.depth  + 1 )
		TreeMaker.plotByDFS.xDistance = 1.0 / ( TreeMaker.plotByDFS.span + 1 )

		print( "span: {0}, depth: {1}, xDistance: {2}, yDistance: {3}".format( TreeMaker.plotByDFS.span, TreeMaker.plotByDFS.depth, TreeMaker.plotByDFS.xDistance, TreeMaker.plotByDFS.yDistance ) )

		TreeMaker.plotByDFS( root, ( 0.0, 1.0 ), ( 0.0, 1.0 ), ( 1.0, 1.0 ) )

		plt.show()


	@staticmethod
	def getTreeDepth( node ):

		if type( node ) is not TreeNode:
			return 1;

		max = 0;

		for fVal in node.fValueMap.keys():
			fValDepth = TreeMaker.getTreeDepth( node.fValueMap[ fVal ] )

			if ( max < fValDepth ):
				max = fValDepth

		return max + 1


	@staticmethod
	def getTreeSpan( node ):

		count = 0

		for fVal in node.fValueMap.keys():
			if type( node.fValueMap[ fVal ] ) is TreeNode:
				count += TreeMaker.getTreeSpan( node.fValueMap[ fVal ] )
			else:
				count += 1

		return count


	"""
	plots a id3tree
	node the root node
	parentNodePt = root node
	minL = lowest coordinate in the space ( 0, 0 )
	maxR = highest corrdinate in the space ( 1, 1 )
	annotate = false 
	"""
	@staticmethod
	def plotByDFS( node, parentNodePt, minL, maxR, annotate = False ):

		# plot children and add annotations


		print( "entering node {0}", node.fName )
		print( "minL: {0}".format( minL ) )
		print( "maxR: {0}".format( maxR ) )

		currentLeftPos = ( minL[0], minL[1] + TreeMaker.plotByDFS.yDistance )

		noOfChildren = len( node.fValueMap )

		parentX = minL[0] + noOfChildren * TreeMaker.plotByDFS.xDistance / 2 

		parentPt = ( parentX, minL[1] )

		for fVal in node.fValueMap.keys():

			print( "previousLeftPost: {0}".format( currentLeftPos ) )
			#TreeMaker.plotFeatureValText( parentPt, currentLeftPos, fVal )	

			if type( node.fValueMap[ fVal ] ) is TreeNode:

				leftX, rightX, immediateX = TreeMaker.plotByDFS( node.fValueMap[ fVal ], parentPt, currentLeftPos, maxR, True )

				#currentLeftPos = ( ( leftX + rightX ) / 2 , currentLeftPos[1] )
				#currentLeftPos = ( leftX + TreeMaker.plotByDFS.xDistance, currentLeftPos[1] )
				currentLeftPos = ( leftX , currentLeftPos[1] )

				nodeTxt = fVal

			else:
				nodeTxt = node.fValueMap[ fVal ]

				centerPt = TreeMaker.getTextCenterCoords( currentLeftPos )

				TreeMaker.plotNode( nodeTxt, centerPt, parentPt, TreeMaker.leafNode )

				TreeMaker.plotFeatureValText( centerPt, parentPt, fVal )	

				currentLeftPos = ( currentLeftPos[0] + TreeMaker.plotByDFS.xDistance, currentLeftPos[1] )


			

		print( "currentLeftPost after printing children: {0}".format( currentLeftPos ) )
		#print this node

		if annotate == True:

			TreeMaker.plotFeatureValText( parentPt, parentNodePt, fVal )	
			TreeMaker.plotNode( node.fName, parentPt, parentNodePt, TreeMaker.decisionNode )

		else:
			TreeMaker.plotByDFS.axes.text( parentPt[0] - TreeMaker.plotByDFS.xDistance / 2, parentPt[1], node.fName, bbox = TreeMaker.rootNode )


		print( "leaving node {0}", node.fName )

		return currentLeftPos[0], maxR[0], parentPt[0]

		# save leftmost and rightmost childred coords
		# put node in middle
		# return right most and node coord

	@staticmethod
	def plotFeatureValText( parentPt, currentLeftPos, fVal ):

		midX = ( parentPt[0] + currentLeftPos[0] ) / 2
		midY = ( parentPt[1] + currentLeftPos[1] ) / 2

		TreeMaker.plotByDFS.axes.text( midX, midY, fVal, ha = 'center', color = 'white', bbox = TreeMaker.featureValStyle )


	@staticmethod
	def plotByBFS( node, afterCoord ):
		pass


	@staticmethod
	def getTextCenterCoords( curL ):

		x = ( TreeMaker.plotByDFS.xDistance / 2 ) + curL[0]

		return ( x, curL[1] )

	@staticmethod
	def storeTree( root, filePath ):
		fh = open( filePath, 'wb' )
		pickle.dump( root, fh )

		fh.close()

	@staticmethod
	def getTreeFromFile( filePath ):

		fh = open( filePath, 'rb' )
		root = pickle.load( fh )
		fh.close()

		return root 









