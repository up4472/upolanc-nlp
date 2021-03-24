from source.preprocess.preprocess_tokenize  import tokenize

from nltk.probability   import FreqDist
from nltk.util          import ngrams

#
# Public methods
#

def frequency (documents, n, params) :
	corpus, bow = tokenize(documents, params)

	data = []

	for document in bow :
		freq = ngrams(document, n)
		freq = FreqDist(freq)

		data.append(freq)

	return data
