# Data Transformation and Normalization

## Transformer
	
Trainers expects feature columns with "numbered" feature labels. So, transformers convert human readable data to trainer readable data. It also converts classes to "numbered" labels for faster calculations.

## Normalizer

In case of continuous data, normalizers classify labels in ranges. Ranges are given numbers which are feature labels. Output labels / classes are also numbered in this way. So, for example if we have temperature data we can create ranges like this

0 if temperature < -10
1 if temperature <  0
2 if temperature <  10
3 if temperature <  20
4 if temperature <  30
5 if temperature >=  30

__As this is a binary naive system, our normalizer will only give:__

0 if temperature <  20
1 if temperature >= 20


# Trainers

## 1 DataSetTrainer

This trainer expects the dataset in list of lists (record). Sample data set would be:

	[
		[ 'my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
		[ 'maybe', 'not', 'take', 'him', \
			'to', 'dog', 'park', 'stupid'],
		[ 'my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
		[ 'stop', 'posting', 'stupid', 'worthless', 'garbage' ],
		[ 'mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
		[ 'quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
	]
And classes (output labels) as a list where nth value is the class of nth record.

## FileDataSetTrainer

This works exactly like DataSetTrainer, but the data is loaded from a file. Sample file is given for reference

### APITrainer

This works through an API call where you pass a single record and its class. The main goal of this is coming by performance for huge data. So it's not possible to recalculate class labels and feature labels each time new data comes over. It only recalculates probabilities and does not save trained dataset for optimization purposes. Preconditions:

1. class labels must be given in initialization. No new data can have a class label which is not already present.
2. feature labels must be given in initialization.

__So, it works in two steps__
1. Train with a DataSetTrainer or FileDataSetTrainer to get the nascent classifier which have the complete set of all the labels.
2. Attach the classifier to APITrainer which recalculates probabilities.