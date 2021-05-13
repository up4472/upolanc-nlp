from source.preprocess.preprocess_feature   import handcrafted
from source.preprocess.preprocess_feature   import tfidf
from source.preprocess.preprocess_feature   import countvec
from source.preprocess.preprocess_tokenize  import tokenize

#
# Params class
#

class ClassifierParams :

	def __init__ (self, params) :
		self.should_shuffle = params.should_shuffle
		self.should_print   = params.should_print
		self.should_stem    = params.should_stem
		self.should_plot    = params.should_plot
		self.should_save    = params.should_save

		self.x = 'Message'
		self.y = 'Book ID'

		self.nfolds     = 10
		self.extractor  = 'tfidf'

	def features (self, data) :
		if self.extractor == 'tfidf' or self.extractor == 'countvec':
			data, _ = tokenize(data, self)

		if self.extractor == 'tfidf' :
			return tfidf(data)
		elif self.extractor == 'countvec' :
			return countvec(data)
		elif self.extractor == 'handcrafted' :
			return handcrafted(data)
		elif self.extractor == 'none' :
			return data
		else :
			print(f'Option <{self.extractor}> does not match any. TF-IDF will be used.')
			return tfidf(data)
