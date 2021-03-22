from sklearn.feature_extraction.text    import TfidfVectorizer
from pandas                             import DataFrame

#
# Public methods
#

def tfidf (documents) :
	extractor = TfidfVectorizer()

	vectors     = extractor.fit_transform(documents)
	features    = extractor.get_feature_names()
	dense       = vectors.todense().tolist()

	return DataFrame(dense, columns = features)
