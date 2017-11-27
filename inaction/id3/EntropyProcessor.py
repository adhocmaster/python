import math

class EntropyProcessor:

	#  labels = [ l, l, l, ... ]
	@staticmethod
	def getEntropyFromVector( labels ):

		labelFreq = {}

		numElements = len ( labels )

		for i in range( numElements ):

			curL = labels[i]

			labelFreq[ curL ] = labelFreq.get( curL, 0 ) + 1

		entropy = 0.0

		for key in labelFreq.keys():

			probabilityL = float ( labelFreq[ key ] ) / numElements
			entropy -= probabilityL * math.log( probabilityL, 2 )

		return entropy


	@staticmethod
	def getEntropyFromDataSet( dataSet ):
		
		return EntropyProcessor.getEntropyFromVector( [ r[-1] for r in dataSet ] ) #this actually works for both


