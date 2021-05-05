from source.classifier.classifier_params    import ClassifierParams
from source.classifier.classifier_model     import ClassifierModel

import pandas
import re

#
# Public methods
#

def run_ex4_all (dataset, params) :
	run_ex4(dataset, params,
	        model = ['RF', 'NB', 'KNN', 'LR', 'MV'],
	        extractor = ['tfidf', 'countvec', 'handcrafted'],
	        y = ['CodePreliminary', 'Topic', 'Book ID']
	)

def run_ex4 (documents, params, model = None, extractor = None, y = None) :
	if extractor is None : extractor = ['tfidf']
	if model is None : model = ['RF', 'NB', 'LR', 'KNN', 'VC']
	if y is None : y = ['CodePreliminary']

	params = ClassifierParams(params)

	if type(y) != list or type(extractor) != list or type(model) != list :
		print('The values <model>, <extractor> and <y> must all be of class <list>.')
		raise ValueError

	for index in range(len(documents)) :
		document = documents[index]

		for yi in y :
			result = []

			for ei in extractor :
				params.y = yi
				params.extractor = ei

				for name in model :
					classifier = ClassifierModel(name, document)
					results = classifier.cross_valid(params).values.tolist()

					result.append([name, params.extractor, results[1][0], results[1][1]])

			result = pandas.DataFrame(result, columns = ['Model', 'Extractor', 'F1 Score', 'Accuracy'])
			result = result.sort_values(['Accuracy', 'F1 Score', 'Extractor', 'Model'], ascending = False)

			if params.should_print :
				print()
				print(f'Classifier results on dataset <{index}> and target <{params.y}> : ')
				print()

				with pandas.option_context('display.max_rows', None, 'display.max_columns', None) :
					print(result)

			if params.should_save :
				filename = f'{index}-{params.y}'
				filename = filename.lower()
				filename = filename.replace(' ', '')

				result.to_csv(f'results\\{filename}.csv', header = True, index = True, sep = '\t', mode = 'w')
