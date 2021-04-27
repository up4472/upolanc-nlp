from source.preprocess.preprocess_frequency import frequency
from matplotlib                             import pyplot

import pandas

#
# Public methods
#

def run_ex0 (documents, params) :
	books = documents['Book ID']
	types = documents['CodePreliminary']
	stuid = documents['Pseudonym']

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

		pyplot.figure('Pseudonym')
		stuid.value_counts().nlargest(15).plot.barh()
		pyplot.gca().invert_yaxis()
		pyplot.show()
