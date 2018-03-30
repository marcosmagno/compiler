class TabelaSimbolo(object):
	"""docstring for TabelaSimbolo"""
	def __init__(self):

		self.tabela_simbolo = {}
		self.word = ["KW", 'program', 0 , 0]
		self.put_tabela_simbolo(self.word,'1' )

		self.word = ["KW", 'if', 0 , 0]
		self.put_tabela_simbolo(self.word,'2' )

		self.word = ["KW", 'else', 0 , 0]
		self.put_tabela_simbolo(self.word,'3' )		

		self.word = ["KW", 'while', 0 , 0]
		self.put_tabela_simbolo(self.word,'4' )

		self.word = ["KW", 'write', 0 , 0]
		self.put_tabela_simbolo(self.word,'5' )

		self.word = ["KW", 'read', 0 , 0]
		self.put_tabela_simbolo(self.word,'6' )
		
		self.word = ["KW", 'num', 0 , 0]
		self.put_tabela_simbolo(self.word,'7' )

		self.word = ["KW", 'char', 0 , 0]
		self.put_tabela_simbolo(self.word,'8' )		

		self.word = ["KW", 'not', 0 , 0]
		self.put_tabela_simbolo(self.word,'9' )

		self.word = ["KW", 'or', 0 , 0]
		self.put_tabela_simbolo(self.word,'10' )

		self.word = ["KW", 'and', 0 , 0]
		self.put_tabela_simbolo(self.word,'11' )				
	
	#@classmethod
	def put_tabela_simbolo(self, w,i):
		self.tabela_simbolo[i] = w

	#@classmethod
	def get_tabela_simbolo(self, i):
		return self.tabela_simbolo[i]

'''
def main():
	t = TabelaSimbolo()
	print t.get_tabela_simbolo()

if __name__ == '__main__':
	main()
'''