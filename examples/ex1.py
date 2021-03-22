from source.preprocess  import tokenize
from source.preprocess  import frequency
from source.extractors  import tfidf

import pandas

#
# Private constants
#

__should_stem     = True
__should_plot     = True
__should_print    = True
__should_save     = False

__nlargest  = 15
__unigrams  = 1
__bigrams   = 2

#
# Public methods
#

def run_ex1 (documents) :
	corpus, bow = tokenize(documents, __should_stem)
	corpus      = tfidf(corpus)

	leader = []

	for index in range(len(corpus)) :
		leader.append(corpus.transpose().nlargest(__nlargest, index).transpose())

	if __should_print :
		for item in leader :
			with pandas.option_context('display.max_rows', None, 'display.max_columns', None) :
				print(item)
				print()

	_ = frequency(documents, __unigrams, __should_stem, __should_plot)
	_ = frequency(documents, __bigrams, __should_stem, __should_plot)

	return corpus
