from sklearn.linear_model       import LogisticRegression
from sklearn.naive_bayes        import MultinomialNB
from sklearn.neighbors          import KNeighborsClassifier
from sklearn.ensemble           import RandomForestClassifier
from sklearn.ensemble           import VotingClassifier

#
# Public methods
#

def createRF () :
	return RandomForestClassifier(
		n_estimators        = 150,
		min_samples_leaf    = 3,
		min_samples_split   = 10,
		random_state        = 0,
		n_jobs              = None
	)

def createNB () :
	return MultinomialNB(
		alpha       = 1.0,
		fit_prior   = True
	)

def createLR () :
	return LogisticRegression(
		max_iter    = 1000,
		n_jobs      = None
	)

def createKNN () :
	return KNeighborsClassifier(
		n_neighbors = 10,
		n_jobs      = None
	)

def createVC () :
	lr = createLR()
	rf = createRF()
	nb = createNB()

	return VotingClassifier(
		estimators  = [('LR', lr), ('RF', rf), ('NB', nb)],
		voting      = 'hard'
	)
