from token import Token
from tag import Tag_type
from random import *
import sys
import time
class TabelaSimbolo(object):
	"""docstring for TabelaSimbolo"""
	def __init__(self):
		self.count = 0

		self.identifier = 0

		self.tabela_simbolo = {}
		#self.word = ["KW", 'program', 0 , 0]
		self.word = Token(Tag_type.KW, 'program', 0, 0)
#		print self.word.getLexema()
	
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW, 'else', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW, 'if', 0, 0)
		self.put_symbol_table(self.word)


		self.word = Token(Tag_type.KW, 'while', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW, 'write', 0, 0)
		self.put_symbol_table(self.word)		


		self.word = Token(Tag_type.KW, 'read', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW, 'num', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW, 'char', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW, 'not', 0, 0)
		self.put_symbol_table(self.word)				

		self.word = Token(Tag_type.KW, 'or', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW, 'and', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW, 'class', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW, 'public', 0, 0)
		self.put_symbol_table(self.word)	



	def put_symbol_table(self, w):
		self.count = self.count + 1
	
		self.set_identifier()
		i = self.get_identifier()
		self.tabela_simbolo[i] = w		


	def set_identifier(self):
		self.identifier = self.identifier + 1

	def get_identifier(self):
		return self.identifier

	def get_token(self, lexema):
		for k, token in self.tabela_simbolo.iteritems():			
			if token.getLexema() == lexema:
				return token
		return None	



	def get_ts(self):
		
		for k,v in self.tabela_simbolo.iteritems():
			print k,v.getClasse(), v.getLexema()
