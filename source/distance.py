import numpy

#
# Public methods
#

def levenshtein (x, y, should_print = False) :
	xlen = 1 + len(x)
	ylen = 1 + len(y)

	distance = numpy.zeros((xlen, ylen), dtype = int)

	for i in range(xlen) :
		distance[i][0] = i

	for i in range(ylen) :
		distance[0][i] = i

	acost = 1   # Insertion
	bcost = 1   # Deletion
	ccost = 2   # Substitution

	for xi in range(1, xlen) :
		for yi in range(1, ylen) :
			xchar = x[xi - 1]
			ychar = y[yi - 1]

			if xchar == ychar :
				distance[xi][yi] = distance[xi - 1][yi - 1]
			else :
				a = acost + distance[xi + 0][yi - 1]
				b = bcost + distance[xi - 1][yi + 0]
				c = ccost + distance[xi - 1][yi - 1]

				distance[xi][yi] = min(a, b, c)

	if should_print :
		__print(distance)

	return distance[xlen - 1][ylen - 1]

def lcs (x, y, should_print = False) :
	xlen = 1 + len(x)
	ylen = 1 + len(y)

	distance = numpy.zeros((xlen, ylen), dtype = int)

	for xi in range(1, xlen) :
		for yi in range(1, ylen) :
			xchar = x[xi - 1]
			ychar = y[yi - 1]

			if xchar == ychar :
				distance[xi][yi] = distance[xi - 1][yi - 1] + 1
			else :
				a = distance[xi - 1][yi + 0]
				b = distance[xi + 0][yi - 1]

				distance[xi][yi] = max(a, b)
	if should_print :
		__print(distance)

	return distance[xlen - 1][ylen - 1]

#
# Private methods
#

def __print (distance) :
	xlen = distance.shape[0]
	ylen = distance.shape[1]

	for xi in range(xlen) :
		for yi in range(ylen) :
			print('{:2d}'.format(distance[xi][yi]), end = ' ')
		print()
	print()
