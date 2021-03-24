from source.preprocess.preprocess_tokenize  import tokenize
from source.preprocess.preprocess_feature   import tfidf

from sklearn.cluster    import KMeans
from wordcloud          import WordCloud
from matplotlib         import pyplot

#
# Public methods
#

def run_ex2 (documents, params) :
	corpus, _   = tokenize(documents, params)
	vector      = tfidf(corpus)

	k = len(documents)

	model = KMeans(n_clusters = k, init = 'k-means++', max_iter = 200, n_init = 10)
	model.fit(vector)

	if k == 2 :
		titles = ['XLSX Data', 'XLSX Discussion']
	elif k == 3 :
		titles = ['ID260 and ID261', 'ID264 and ID265', 'ID266 and ID267']
	else :
		titles = ['ID260 and ID261', 'ID264 and ID265', 'ID266 and ID267', 'XLSX Data', 'XLSX Discussion']

	for i in range(0, k) :
		wc = WordCloud(
			max_font_size = 50,
			max_words = 100,
			background_color = 'white'
		).generate(corpus[i])

		if params.should_plot :
			pyplot.figure(titles[i])
			pyplot.imshow(wc, interpolation = 'bilinear')
			pyplot.axis('off')
			pyplot.show()
