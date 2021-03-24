from nltk.stem      import SnowballStemmer
from nltk.corpus    import stopwords

import string
import numpy
import nltk
import re

#
# Public methods
#

def tokenize (documents, params) :
	stemmer = SnowballStemmer('english')

	bow = numpy.empty(len(documents), dtype = numpy.object)
	nne = []

	for index in range(len(documents)) :
		document = ''.join([word for word in documents[index] if word not in string.punctuation])

		token = nltk.word_tokenize(document)
		token = nltk.pos_tag(token)
		chunk = nltk.ne_chunk(token)

		for i in chunk :
			if hasattr(i, 'label') :
				nne.append(' '.join([x[0].lower() for x in i]))

		document = re.sub(r'\b\d+\b'        , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\W'             , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\s+[a-zA-Z]\s+]', ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\[a-zA-Z]\s+'   , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'\s+'            , ' ', document, flags = re.IGNORECASE)
		document = re.sub(r'^b\s+'          , ' ', document, flags = re.IGNORECASE)

		document = document.lower()
		document = document.split()

		document = [word for word in document if not word in stopwords.words('english')]

		if params.should_stem :
			document = [word if word in nne else stemmer.stem(word) for word in document]

		bow[index] = document

	return [' '.join(document) for document in bow], bow
