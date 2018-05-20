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
		self.word = Token(Tag_type.KW_PROGRAM, 'program', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW_ELSE, 'else', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW_IF, 'if', 0, 0)
		self.put_symbol_table(self.word)


		self.word = Token(Tag_type.KW_WHILE, 'while', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW_WRITE, 'write', 0, 0)
		self.put_symbol_table(self.word)		


		self.word = Token(Tag_type.KW_READ, 'read', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW_NUM, 'num', 0, 0)
		self.put_symbol_table(self.word)

		self.word = Token(Tag_type.KW_CHAR, 'char', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW_NOT, 'not', 0, 0)
		self.put_symbol_table(self.word)				

		self.word = Token(Tag_type.KW_OR, 'or', 0, 0)
		self.put_symbol_table(self.word)	

		self.word = Token(Tag_type.KW_AND, 'and', 0, 0)
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
