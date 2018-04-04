from token import Token
from tag import Tag_Type
from random import *
import sys
class TabelaSimbolo(object):
	"""docstring for TabelaSimbolo"""
	def __init__(self):

		self.tabela_simbolo = {}
		#self.word = ["KW", 'program', 0 , 0]
		self.word = Token(Tag_Type.KW, 'program', 0, 0)
#		print self.word.getLexema()
	
		self.put_tabela_simbolo(self.word, randint(0,20) )

		self.word = Token(Tag_Type.KW, 'else', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )

		self.word = Token(Tag_Type.KW, 'if', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )



		self.word = Token(Tag_Type.KW, 'while', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )

		self.word = Token(Tag_Type.KW, 'write', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )		


		self.word = Token(Tag_Type.KW, 'read', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )	

		self.word = Token(Tag_Type.KW, 'num', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )

		self.word = Token(Tag_Type.KW, 'char', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )	

		self.word = Token(Tag_Type.KW, 'not', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )				

		self.word = Token(Tag_Type.KW, 'or', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )	

		self.word = Token(Tag_Type.KW, 'and', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )	

		self.word = Token(Tag_Type.KW, 'class', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )

		self.word = Token(Tag_Type.KW, 'public', 0, 0)
		self.put_tabela_simbolo(self.word, randint(0,20) )	



	def put_tabela_simbolo(self, w,i):
		self.tabela_simbolo[i] = w



	def get_token(self, lexema):

		for k, token in self.tabela_simbolo.iteritems():
			if token.getLexema() == lexema:
				return token

		return None	

	def toString(self,value):
		return str(value[0]) + "," + " '" + str(value[1]) + "'"

	def get_ts(self):
		for k,v in self.tabela_simbolo.iteritems():
			print >>sys.stderr, k,v.toString()
'''
def main():
	t = TabelaSimbolo()
	print t.get_token("program")

if __name__ == '__main__':
	main()
'''