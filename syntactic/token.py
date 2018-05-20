class Token(object):
	"""docstring for Token"""
	def __init__(self, classe, lexema, linha, coluna):
		self.classe = classe
		self.lexema = lexema
		self.linha  = linha
		self.coluna = coluna

	def getLexema(self):
		return self.lexema
		
	def getClass(self):
		return self.classe

	def toString(self):
		return "< " + str(self.classe) +  ", " + "\""  + str(self.lexema) + "\""
		

