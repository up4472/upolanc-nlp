import scipy
from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.feature_extraction.text    import CountVectorizer
from nltk.corpus                        import stopwords

import pandas
import string
import nltk
import re

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

def handcrafted (documents) :
	dense = []

	stop_words = stopwords.words('english')

	inte_words = [
		'which', 'what', 'whose', 'who', 'whom',
		'where', 'whither', 'whence', 'when', 'how',
		'why', 'whether', 'whatsoever'
	]

	for document in documents :
		document = document.lower()

		sentences = nltk.sent_tokenize(document)
		words = re.findall(r'\w+', document)
		lengths = list(map(lambda x : len(x), words))

		chars = sum(lengths)                                                        # number of non-whitespace characters
		uniqe = len(set(words))                                                     # number of unique words
		count = len(words)                                                          # number of words
		sents = len(sentences)                                                      # number of sentences

		digit = len(list(filter(lambda c : c in string.punctuation, document)))     # number of digits
		sword = 0                                                                   # number of stop words
		iword = 0                                                                   # number of interrogative words

		maxlen = max(lengths) if lengths != [] else 0                               # maximum length of words
		minlen = min(lengths) if lengths != [] else 0                               # minimum length of words

		punc0 = len(list(filter(lambda c : c == '!', document)))                    # number of !
		punc1 = len(list(filter(lambda c : c == '?', document)))                    # number of ?
		punc2 = len(list(filter(lambda c : c == ',', document)))                    # number of ,
		punc3 = len(list(filter(lambda c : c == '.', document)))                    # number of .
		punc4 = len(list(filter(lambda c : c == '-', document)))                    # number of -
		punc5 = len(list(filter(lambda c : c == ')', document)))                    # number of )
		punc6 = len(list(filter(lambda c : c == '(', document)))                    # number of (
		punc7 = len(list(filter(lambda c : c == ':', document)))                    # number of :

		caps = len(re.findall(r'[A-Z]', document))                                  # number of capital letters
		wild = len(re.findall(r'^w+', document))                                    # number of non asci characters

		document = re.sub(r'\b\d+\b'        , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\W'             , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\s+[a-zA-Z]\s+]', ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\[a-zA-Z]\s+'   , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\s+'            , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'^b\s+'          , ' ', document, flags = re.IGNORECASE)

		for word in document.split() :
			if word in stop_words :
				sword = sword + 1
			if word in inte_words :
				iword = iword + 1

		row = [
			sents, count, chars, uniqe, digit,
			sword, iword, maxlen, minlen,
			punc0, punc1, punc2, punc3,
			punc4, punc5, punc6, punc7,
			caps, wild
		]

		dense.append(row)

	return pandas.DataFrame(dense)
