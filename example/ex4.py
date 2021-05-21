from source.classifier.classifier_params    import ClassifierParams
from source.classifier.classifier_model     import ClassifierModel

import pandas
import re

#
# Public methods
#

def run_ex4 (documents, params, model = None, extractor = None, target = None) :
	if extractor is None : extractor = ['tfidf', 'countvec', 'handcrafted', 'none']
	if model is None : model = ['RF', 'NB', 'KNN', 'LR', 'MV', 'BERT']
	if target is None : target = ['CodePreliminary', 'Topic', 'Book ID']

	params = ClassifierParams(params)

	if type(target) != list or type(extractor) != list or type(model) != list :
		print('The values <model>, <extractor> and <target> must all be of class <list>.')
		raise ValueError

	for index in range(len(documents)) :
		document = documents[index]

		for yi in target :
			result = []

			for ei in extractor :
				params.y = yi
				params.extractor = ei

				for name in model :
					if name == 'BERT' and ei != 'none' :
						continue
					if name != 'BERT' and ei == 'none' :
						continue

					if params.should_print :
						print(f'Running model <{name}> with <{ei}> on <{yi}> ....')

					classifier = ClassifierModel(name, document, params)
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
