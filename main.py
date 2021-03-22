from examples.utility   import dataset
from examples.utility   import bookset
from examples.ex1       import run_ex1

import matplotlib
import sklearn
import tensorflow
import pandas
import numpy
import nltk

#
# Configuration
#

pandas.set_option('display.width', 200)

nltk.download('averaged_perceptron_tagger', quiet = True)
nltk.download('maxent_ne_chunker', quiet = True)
nltk.download('stopwords', quiet = True)
nltk.download('words', quiet = True)
nltk.download('punkt', quiet = True)

#
# Version information
#

def __versions () :
	print(f'- sklearn     : {sklearn.__version__}')
	print(f'- numpy       : {numpy.__version__}')
	print(f'- tensorflow  : {tensorflow.__version__}')
	print(f'- pandas      : {pandas.__version__}')
	print(f'- nltk        : {nltk.__version__}')
	print(f'- matplotlib  : {matplotlib.__version__}')

#
# Main method
#

if __name__ == "__main__" :
	# Run only bookset
	#run_ex1(bookset)

	# Run only dataset
	#run_ex1([' '.join(item['Message']) for item in dataset])

	# Run bookset and dataset
	run_ex1(bookset + [' '.join(item['Message']) for item in dataset])
