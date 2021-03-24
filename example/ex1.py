from source.preprocess.preprocess_tokenize  import tokenize
from source.preprocess.preprocess_frequency import frequency
from source.preprocess.preprocess_feature   import tfidf

from matplotlib import pyplot

import pandas

#
# Public methods
#

def run_ex1 (documents, params) :
	corpus, _   = tokenize(documents, params)
	vector      = tfidf(corpus)

	if len(documents) == 2 :
		titles = ['XLSX Data', 'XLSX Discussion']
	elif len(documents) == 3 :
		titles = ['ID260 and ID261', 'ID264 and ID265', 'ID266 and ID267']
	else :
		titles = ['ID260 and ID261', 'ID264 and ID265', 'ID266 and ID267', 'XLSX Data', 'XLSX Discussion']

	if params.should_print :
		words = []

		for index in range(len(vector)) :
			df = vector.transpose()
			df = df.nlargest(15, index)
			df = df.transpose()

			words.append(df.columns.values)

			with pandas.option_context('display.max_rows', None, 'display.max_columns', None) :
				print(titles[index] + ' : ')
				print(df)
				print()

		words = pandas.DataFrame(words)

		words.columns   = range(1, 16)
		words.index     = titles

		with pandas.option_context('display.max_rows', None, 'display.max_columns', None) :
			print('Top 15 words for each document : ')
			print(words)
			print()

	if params.should_plot :
		f1 = frequency(documents, 1, params)
		f2 = frequency(documents, 2, params)

		for index in range(len(f1)) :
			pyplot.figure(titles[index] + ' - Unigrams', (8, 6))
			pyplot.subplots_adjust(bottom = 0.25)

			f1[index].plot(15)

		for index in range(len(f2)) :
			pyplot.figure(titles[index] + ' - Bigrams', (8, 6))
			pyplot.subplots_adjust(bottom = 0.35)

			f2[index].plot(15)
