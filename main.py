from source.core.core_params    import Params
from example.constants          import dataset
from example.constants          import compset
from example.ex0                import run_ex0
from example.ex1                import run_ex1
from example.ex2                import run_ex2
from example.ex3                import run_ex3
from example.ex4                import run_ex4

import transformers
import matplotlib
import tensorflow
import wordcloud
import openpyxl
import warnings
import argparse
import sklearn
import pandas
import scipy
import numpy
import nltk
import xlrd

#
# Ignore warnings
#

def warn (*args, **kvargs) :
	pass

warnings.warn = warn

#
# Configuration
#

pandas.set_option('display.width', 200)

nltk.download('averaged_perceptron_tagger'  , quiet = True)
nltk.download('maxent_ne_chunker'           , quiet = True)
nltk.download('stopwords'                   , quiet = True)
nltk.download('words'                       , quiet = True)
nltk.download('punkt'                       , quiet = True)

#
# Version information
#

def __versions () :
	print('The following versions are being used :')
	print(f'- sklearn      : {sklearn.__version__}')
	print(f'- numpy        : {numpy.__version__}')
	print(f'- tensorflow   : {tensorflow.__version__}')
	print(f'- pandas       : {pandas.__version__}')
	print(f'- nltk         : {nltk.__version__}')
	print(f'- matplotlib   : {matplotlib.__version__}')
	print(f'- xlrd         : {xlrd.__version__}')
	print(f'- openpyxl     : {openpyxl.__version__}')
	print(f'- wordcloud    : {wordcloud.__version__}')
	print(f'- scipy        : {scipy.__version__}')
	print(f'- transformers : {transformers.__version__}')
	print(f'- argparse     : {argparse.__version__}')
	print()

#
# Main method
#

if __name__ == "__main__" :
	print()

	parser = argparse.ArgumentParser(description = 'Argument parser')

	parser.add_argument('-m', '--model', default = None, type = str, nargs = '+',
	                    choices = ['LR', 'RF', 'NB', 'KNN', 'MV', 'BERT'],
	                    help = 'the model to be used (only used for --demo 4)'
	)
	parser.add_argument('-e', '--extractor', default = None, type = str, nargs = '+',
	                    choices = ['tfidf', 'countvec', 'handcrafted', 'none'],
	                    help = 'the extractor to be used (only used for --demo 4)'
	)
	parser.add_argument('-t', '--target', default = None, type = str, nargs = '+',
	                    choices = ['CodePreliminary', 'Topic', 'Book ID'],
	                    help = 'the classification target to be used (only used for --demo 4)'
	)
	parser.add_argument('-d', '--demo', default = 4, type = int,
	                    choices = [0, 1, 2, 3, 4],
	                    help = 'the demo number, where (0) is target distribution, (1) is uni-grams and bi-grams, ' +
	                           '(2) is wordclouds, (3) is top words distribution, and (4) is text classification.'
	)
	parser.add_argument('-v', '--verbose', default = 0, type = int,
						choices = [0, 1],
						help = 'the verbose flag'
	)
	parser.add_argument('-s', '--save', default = 0, type = int,
	                    choices = [0, 1],
						help = 'the save flag'
	)

	args = parser.parse_args()

	params = Params()

	params.should_shuffle   = True
	params.should_stem      = True
	params.should_plot      = True
	params.should_save      = args.save == 1
	params.should_print     = args.verbose == 1

	if params.should_print :
		__versions()

	if args.demo == 0 :
		run_ex0(dataset, params)
	elif args.demo == 1 :
		run_ex1(compset, params)
	elif args.demo == 2:
		run_ex2(compset, params)
	elif args.demo == 3:
		run_ex3(compset, params)
	elif args.demo == 4:
		run_ex4(dataset, params,
			model = args.model,
			extractor = args.extractor,
			target = args.target
		)
