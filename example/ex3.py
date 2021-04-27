from source.preprocess.preprocess_tokenize  import tokenize
from source.preprocess.preprocess_feature   import tfidf

from sklearn.cluster    import KMeans
from collections        import Counter
from wordcloud          import WordCloud
from matplotlib         import pyplot

import numpy

#
# Private methods
#

def __autolabe (ax, rects) :
	for rect in rects :
		h = rect.get_height()

		ax.annotate('{}'.format(h),
			xy  = (rect.get_x() + rect.get_width() / 2, h),
			ha  = 'center',
			va  = 'bottom'
		)

#
# Public methods
#

def run_ex3 (documents, params) :
	corpus, bow     = tokenize(documents, params)
	vector          = tfidf(corpus)

	freq = []

	for index in range(3) :
		for word in bow[index] :
			freq.append(word)

	print(freq)

	freq = Counter(freq)
	freq = freq.most_common(15)

	words = []
	id261 = []
	id264 = []
	id266 = []
	data = []

	for (key, val) in freq :
		words.append(key)
		id261.append(vector[key][0])
		id264.append(vector[key][1])
		id266.append(vector[key][2])
		data.append(vector[key][3])

	words.reverse()
	id261.reverse()
	id264.reverse()
	id266.reverse()
	data.reverse()

	x = numpy.arange(len(words))
	w = 0.2

	fig, ax = pyplot.subplots()

	ax.barh(x - 3 * w / 2, id261, w, label = 'ID260 and ID261')
	ax.barh(x - 1 * w / 2, id264, w, label = 'ID264 and ID265')
	ax.barh(x + 1 * w / 2, id266, w, label = 'ID266 and ID267')
	ax.barh(x + 3 * w / 2, data , w, label = 'XLXS Data')

	ax.set_xlabel('')
	ax.set_title('')
	ax.set_yticks(x)
	ax.set_yticklabels(words)
	ax.legend()

	fig.tight_layout()
	pyplot.show()

	print(id261)
