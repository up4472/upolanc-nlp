from source.core.core_params    import Params
from example.constants          import dataset
from example.constants          import compset
from example.ex0                import run_ex0
from example.ex1                import run_ex1
from example.ex2                import run_ex2

import matplotlib
import tensorflow
import wordcloud
import openpyxl
import sklearn
import pandas
import numpy
import nltk
import xlrd

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
	print(f'- sklearn     : {sklearn.__version__}')
	print(f'- numpy       : {numpy.__version__}')
	print(f'- tensorflow  : {tensorflow.__version__}')
	print(f'- pandas      : {pandas.__version__}')
	print(f'- nltk        : {nltk.__version__}')
	print(f'- matplotlib  : {matplotlib.__version__}')
	print(f'- xlrd        : {xlrd.__version__}')
	print(f'- openpyxl    : {openpyxl.__version__}')
	print(f'- wordcloud   : {wordcloud.__version__}')
	print()

#
# Main method
#

if __name__ == "__main__" :
	params = Params()

	params.should_shuffle   = True
	params.should_stem      = True
	params.should_plot      = True
	params.should_save      = True
	params.should_print     = True

	if params.should_print :
		__versions()

	run_ex0(dataset[0], params)
	run_ex0(dataset[1], params)
	run_ex1(compset, params)
	run_ex2(compset, params)
