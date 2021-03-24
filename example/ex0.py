from matplotlib import pyplot

import pandas

#
# Public methods
#

def run_ex0 (documents, params) :
	books = documents['Book ID']
	types = documents['CodePreliminary']

	if params.should_plot :
		pyplot.figure('Book ID')
		books.value_counts().plot.barh()
		pyplot.gca().invert_yaxis()
		pyplot.show()

		pyplot.figure('CodePreliminary')
		types.value_counts().plot.barh()
		pyplot.subplots_adjust(left = 0.35)
		pyplot.gca().invert_yaxis()
		pyplot.show()
