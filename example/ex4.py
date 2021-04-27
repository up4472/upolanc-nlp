from source.classifier.classifier_params    import ClassifierParams
from source.classifier.classifier_model     import ClassifierModel

import pandas

def __runclassifier (documents, params, model) :
	model   = ClassifierModel(model, documents)
	result  = model.cross_valid(params)

	if params.should_print :
		print(f'Running {model.name} classifier: ')

		with pandas.option_context('display.max_rows', None, 'display.max_columns', None) :
			print(result)

#
# Public methods
#

def run_ex4 (documents, params, model = 'VC') :
	params              = ClassifierParams(params)
	params.y            = 'CodePreliminary'
	#params.y            = 'Topic'
	#params.y            = 'Book ID'
	#params.y            = 'Bookclub'
	params.extractor    = 'tfidf'
	#params.extractor    = 'countvec'

	if model == 'ALL' :
		for name in ['RF', 'NB', 'LR', 'KNN', 'VC'] :
			__runclassifier(documents, params, name)
	else :
		__runclassifier(documents, params, model)
