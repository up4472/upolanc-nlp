from source.preprocess.preprocess_frequency import frequency
from matplotlib                             import pyplot

import pandas

#
# Public methods
#

def run_ex0 (documents, params) :
	books0 = documents[0]['Book ID']
	types0 = documents[0]['CodePreliminary']
	stuid0 = documents[0]['Pseudonym']

	books1 = documents[1]['Book ID']
	types1 = documents[1]['CodePreliminary']
	stuid1 = documents[1]['Pseudonym']

	unique0 = types0.unique()
	unique1 = types1.unique()

	counts0 = types0.value_counts()
	counts1 = types1.value_counts()

	for i in unique0 :
		if i not in unique1 :
			counts1 = counts1.append(pandas.Series([0], index = [str(i)]))

	if params.should_plot :
		pyplot.figure('Book ID')
		books0.value_counts().plot(position = 0.0, kind = 'barh', color = 'g', width = 0.2)
		books1.value_counts().plot(position = 1.0, kind = 'barh', color = 'b', width = 0.2)
		pyplot.gca().invert_yaxis()
		pyplot.legend(['Dataset 1', 'Dataset 2'], loc = 4)
		pyplot.show()

		pyplot.figure('CodePreliminary')
		counts0.plot(position = 0.0, kind = 'barh', color = 'g', width = 0.2)
		counts1.plot(position = 1.0, kind = 'barh', color = 'b', width = 0.2)
		pyplot.subplots_adjust(left = 0.35)
		pyplot.gca().invert_yaxis()
		pyplot.legend(['Dataset 1', 'Dataset 2'], loc = 4)
		pyplot.show()

		pyplot.figure('Pseudonym')
		stuid0.value_counts().nlargest(15).plot(position = 0.0, kind = 'barh', color = 'g', width = 0.2)
		stuid1.value_counts().nlargest(15).plot(position = 1.0, kind = 'barh', color = 'b', width = 0.2)
		pyplot.gca().invert_yaxis()
		pyplot.legend(['Dataset 1', 'Dataset 2'], loc = 4)
		pyplot.show()
