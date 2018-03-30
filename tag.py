class Tag(object):
	"""docstring for Tag"""
	def __init__(self):

		# Operadores
		self.OP_EQ = 'OP_EQ'
		self.OP_NE = 'OP_NE'
		self.OP_GT = 'OP_GT'
		self.OP_LT = 'OP_LT'
		self.OP_GE = 'OP_GE'
		self.OP_LE = 'OP_LE'
		self.OP_AD = 'OP_AD'
		self.OP_MIN = 'OP_MIN'
		self.OP_MUL = 'OP_MUL'
		self.OP_DIV = 'OP_DIV'
		self.OP_ASS = "OP_ASS"


    @classmethod
    def get_op(self):
        return self.OP_EQ

'''
    	# Simbolos
    	self.SMB_OBC = 'SMB_OBC'
    	self.SMB_CBC = 'SMB_CBC'
    	self.SMB_OPA = 'SMB_OPA'
    	self.SMB_CPA = 'SMB_CPA'
    	self.SMB_COM = 'SMB_COM'
    	self.SMB_SEM = 'SMB_SEM'

    	# ID
    	self.ID = 'ID'

    	# Constantes
    	self.CON_NUM = 'CON_NUM'
    	self.CON_CHAR = 'CON_CHAR'
    	

    	# Literal
    	self.LITERAL = 'LITERAL'

    	# Palavrs Recervadas
    	self.KW = 'KW'
'''