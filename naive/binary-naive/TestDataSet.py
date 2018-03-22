class TestDataSet:

	def __init__( self ):
		
		self.dataSet, self.outputLabels = self.loadDataSet()
		self.vocabularyList = self.generateVocabularyList()

	def loadDataSet( self ):
		tweets = [
			[ 'my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
			[ 'maybe', 'not', 'take', 'him', \
				'to', 'dog', 'park', 'stupid'],
			[ 'my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
			[ 'stop', 'posting', 'stupid', 'worthless', 'garbage' ],
			[ 'mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
			[ 'quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
		]

		outputLabels = [ 0, 1, 0, 1, 0, 1 ] #1 is abusive, 0 is not

		return tweets, outputLabels

	def generateVocabularyList( self ):

		vSet = set()

		for row in self.dataSet:

			vSet = vSet | set( row )

		return list( vSet )

	def getVocabularyList( self ):

		return self.vocabularyList;

	def getFeatueVectorFromInputWords( self, inputWords ):

		emptyVector = [0] * len( self.vocabularyList )

		for i in range( len( self.vocabularyList) ):

			if self.vocabularyList[i] in inputWords:
				emptyVector[i] = 1
			else:
				print( "{0} is not in our input".format( self.vocabularyList[i] ) )

		return emptyVector