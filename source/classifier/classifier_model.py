from source.classifier.classifier_util      import createRF
from source.classifier.classifier_util      import createNB
from source.classifier.classifier_util      import createLR
from source.classifier.classifier_util      import createKNN
from source.classifier.classifier_util      import createVC
from source.model.model_bert                import Bert

from sklearn.model_selection    import KFold
from sklearn.metrics            import accuracy_score
from sklearn.metrics            import f1_score

import pandas
import numpy

#
# Model class
#

class ClassifierModel :

	def __init__ (self, name, data, params) :
		self.name = name
		self.data = data

		if self.name == 'RF' :
			self.model = createRF()
		elif self.name == 'NB' :
			self.model = createNB()
		elif self.name == 'LR' :
			self.model = createLR()
		elif self.name == 'KNN' :
			self.model = createKNN()
		elif self.name == 'VC' :
			self.model = createVC()
		elif self.name == 'BERT' :
			n = self.data[[params.y]]
			n = data.loc[:, params.y].astype('category')
			n = len(set(n))
			print(n)

			self.model = Bert(params, n)
		else :
			self.model = createRF()

	def cross_valid (self, params) :
		f1train     = numpy.zeros(params.nfolds, dtype = numpy.float32)
		f1test      = numpy.zeros(params.nfolds, dtype = numpy.float32)
		acctrain    = numpy.zeros(params.nfolds, dtype = numpy.float32)
		acctest     = numpy.zeros(params.nfolds, dtype = numpy.float32)

		index = 0

		data = self.data[[params.x, params.y]]
		data = data.dropna()

		x = data.loc[:, params.x]
		y = data.loc[:, params.y].astype('category')

		x = params.features(x)

		for xi, yi in KFold(n_splits = params.nfolds, shuffle = params.should_shuffle, random_state = 0).split(x) :
			x0 = x.iloc[xi]
			y0 = y.iloc[xi]
			x1 = x.iloc[yi]
			y1 = y.iloc[yi]

			self.model.fit(x0, y0)

			p0 = self.model.predict(x0)
			p1 = self.model.predict(x1)

			f1train[index]  = f1_score(y0, p0, average = 'weighted', zero_division = 0)
			f1test[index]   = f1_score(y1, p1, average = 'weighted', zero_division = 0)

			acctrain[index] = accuracy_score(y0, p0, normalize = True)
			acctest[index]  = accuracy_score(y1, p1, normalize = True)

			index = index + 1

		result = {
			'F1 Score'  : [
				'{0:.2f} \u00B1 {1:.2f}'.format(numpy.mean(f1train), numpy.std(f1train)),
				'{0:.2f} \u00B1 {1:.2f}'.format(numpy.mean(f1test), numpy.std(f1test)),
			],
			'Accuracy'  : [
				'{0:.2f} \u00B1 {1:.2f}'.format(numpy.mean(acctrain), numpy.std(acctrain)),
				'{0:.2f} \u00B1 {1:.2f}'.format(numpy.mean(acctest), numpy.std(acctest)),
			]
		}

		result = pandas.DataFrame(result)

		result.columns   = ['F1 Score', 'Accuracy']
		result.index     = ['Train', 'Test']

		return result
