from source.io.io_loader    import loadxlsx
from source.io.io_loader    import loadtxt

from os.path    import abspath
from os.path    import dirname

#
# Define filepaths
#

__root  = dirname(dirname(abspath(__file__)))

__dataset   = __root + '\\resources\\dataset.xlsx'
__cookbook  = __root + '\\resources\\cookbook.docx'
__criteria  = __root + '\\resources\\criteria.docx'
__file261   = __root + '\\resources\\ID260 and ID261.txt'
__file264   = __root + '\\resources\\ID264 and ID265.txt'
__file266   = __root + '\\resources\\ID266 and ID267.txt'

#
# Public contstants
#

bookset = [
	loadtxt(__file261),
	loadtxt(__file264),
	loadtxt(__file266)
]

dataset = [
	loadxlsx(__dataset, 'data'),
	loadxlsx(__dataset, 'discussion')
]

compset = [
	bookset[0],
	bookset[1],
	bookset[2],
	' '.join(dataset[0]['Message']),
	' '.join(dataset[1]['Message'])
]
