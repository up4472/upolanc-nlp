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
# Apply some fixes
#

def __applyfixes (data) :
	data['CodePreliminary'] = data['CodePreliminary'].replace('Non-verbal'                          , 'Emoticon/Non-verbal')
	data['CodePreliminary'] = data['CodePreliminary'].replace('General Comment (Narrative?)'        , 'General Comment')
	data['CodePreliminary'] = data['CodePreliminary'].replace('General Discussion'                  , 'General Comment')
	data['CodePreliminary'] = data['CodePreliminary'].replace('Assignment Instructions Question'    , 'Assignment Instructions')
	data['CodePreliminary'] = data['CodePreliminary'].replace('Content Discussion/Outside Material' , 'Content Discussion')
	data['CodePreliminary'] = data['CodePreliminary'].replace('Observation'                         , 'General Comment')
	data['CodePreliminary'] = data['CodePreliminary'].replace('Instuction Question'                 , 'Instruction Question')
	data['CodePreliminary'] = data['CodePreliminary'].replace('Outside Material'                    , 'External Material')

	data['CodePreliminary'] = [item.strip().lower() for item in data['CodePreliminary']]

#
# Loading files
#

__b0 = loadtxt(__file261)
__b1 = loadtxt(__file264)
__b2 = loadtxt(__file266)
__d0 = loadxlsx(__dataset, 'data')
__d1 = loadxlsx(__dataset, 'discussion')

__applyfixes(__d0)
__applyfixes(__d1)

#
# Public contstants
#

bookset = [
	__b0,
	__b1,
	__b2
]

dataset = [
	__d0,
	__d1
]

compset = [
	__b0,
	__b1,
	__b2,
	' '.join(__d0['Message']),
	' '.join(__d1['Message'])
]
