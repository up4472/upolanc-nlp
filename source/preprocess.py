from nltk.stem          import PorterStemmer
from nltk.probability   import FreqDist
from nltk.corpus        import stopwords
from nltk.util          import ngrams
from matplotlib         import pyplot

import string
import numpy
import nltk
import re

#
# Public methods
# https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
#

# FIXME : named entities need to be removed from stemming, and add support for multiword entities (e.q. New York)
def tokenize (documents, should_stem = True) :
	stemmer = PorterStemmer()

	bow = numpy.empty(len(documents), dtype = object)

	for index in range(len(documents)) :
		# Get document
		document = str(documents[index])

		# Remove punctuation
		document = ''.join([word for word in document if word not in string.punctuation])

		# Remove all non word digits
		document = re.sub(r'\b\d+\b', '', document)

		# Fink all named entities
		ne = []

		token = nltk.word_tokenize(document)
		token = nltk.pos_tag(token)
		chunk = nltk.ne_chunk(token)

		for i in chunk :
			if hasattr(i, 'label') :
				ne.append(' '.join([x[0].lower() for x in i]))

		# Remove all the special characters
		document = re.sub(r'\W', ' ', document)

		# Remove all single characters
		document = re.sub(r'\s+[a-zA-Z]\s+]', ' ', document)

		# Remove single characters from the start
		document = re.sub(r'\[a-zA-Z]\s+', ' ', document)

		# Substituting multiple spaces with single space
		document = re.sub(r'\s+', ' ', document, flags = re.I)

		# Removing prefixed 'b'
		document = re.sub(r'^b\s+', '', document)

		# Converting to lowercase
		document = document.lower()

		# Tokenize the document
		document = document.split()

		# Remove stop words
		document = [word for word in document if not word in stopwords.words('english')]

		# Stematization
		if should_stem :
			document = [word if word in ne else stemmer.stem(word) for word in document]

		# Add the document to the data list
		bow[index] = document

	return [' '.join(document) for document in bow], bow

def frequency (documents, n = 1, should_stem = True, should_plot = False) :
	corpus, bow = tokenize(documents, should_stem)

	data = []

	for document in bow :
		freq = FreqDist(ngrams(document, n))

		if should_plot :
			__plot(freq, n = 15)

		data.append(freq)

	return data

#
# Private methods
#

def __plot (freq, n = 15) :
	pyplot.figure(figsize = (12, 8))
	pyplot.subplots_adjust(bottom = 0.30)

	freq.plot(n)
