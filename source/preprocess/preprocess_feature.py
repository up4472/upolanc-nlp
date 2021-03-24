from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.feature_extraction.text    import CountVectorizer

import pandas

#
# Public methods
#

def tfidf (documents) :
	extractor = TfidfVectorizer()

	vectors     = extractor.fit_transform(documents)
	features    = extractor.get_feature_names()
	dense       = vectors.todense().tolist()

	return pandas.DataFrame(dense, columns = features)

def countvec (documents) :
	extractor = CountVectorizer()

	vectors     = extractor.fit_transform(documents)
	features    = extractor.get_feature_names()
	dense       = vectors.todense().tolist()

	return pandas.DataFrame(dense, columns = features)
