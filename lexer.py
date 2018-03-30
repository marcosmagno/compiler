import time
import sys
from tabela_simbolo import TabelaSimbolo
from token import Token
from tag import Tag_Type
from random import *
class Lexer(object):
	"""docstring for Lexer"""
	def __init__(self, input_file):
		self.__TS = TabelaSimbolo()
		self.__END_OF_FILE = -1
		self.__lookahead = 0
		self.n_linha = 1
		self.n_column = 0
		self._caracter = ''
		self.__estado = 1
		self.__list_lexema = []
		self.__ponteiro = 0
		self.lexema = []

		try:
			self.__file = open(input_file,'r')
		except IOError as e:
			print "Erro to open file."


	def pointer_file(self):
		self.__file.seek(self.__file.tell() - 1)

	def nex_token(self):

		while True:

			self.n_column = self.n_column + 1 

			# Ler arquivo
			try:
				self.c = self.__file.read(1)
				if not self.c:
					return Token(Tag_Type.EOF, "EOF", self.n_linha, self.n_column)				

			except IOError as e:
				raise e		
	
			if self.__estado == 1: # CASE 1
				if not self.c:					
					return Token(Tag_Type.EOF, "EOF", self.n_linha, self.n_column)				
				
				elif self.c == "\n":
					self.n_linha = self.n_linha + 1
					self.n_column = 0
					pass

				elif self.c == '\t':
					pass

				elif self.c == " ":
					pass

				elif self.c == "<":
					self.__estado = 2

				elif self.c == "=":
					 self.__estado = 5

				elif self.c == ">":
					self.__estado = 8

				elif self.c == "!":
					self.__estado = 11

				elif self.c == "-": 
					self.__estado = 1 # estado 13
					return Token(Tag_Type.OP_MIN, "-", self.n_linha, self.n_column)

				elif self.c == "+":
					self.__estado = 1 # estado 14
					return Token(Tag_Type.OP_AD, "+", self.n_linha, self.n_column)

				elif self.c == "*":
					if self.c == "/":
						self.__estado = 17 # estado 17
					else:
						return Token(Tag_Type.OP_MUL, "*", self.n_linha, self.n_column)

				elif self.c == "/":
					self.__estado = 16 # estado 16
					


				elif self.c.isalpha():					
					self.__list_lexema.append(self.c)					
					self.__estado = 14

				elif self.c == ";":
					pass

			elif self.__estado == 2: # CASE 2
				if self.c == "=":
					self.__estado = 1
					return Token(Tag_Type.OP_LE, "<=", self.n_linha, self.n_column)
				else:
					self.__estado = 1
					self.pointer_file()
					return Token(Tag_Type.OP_LT, "<", self.n_linha, self.n_column)


			elif self.__estado == 5: # CASE 5
				if self.c == "=": # estado 6
				   self.__estado = 1
				   return Token(Tag_Type.OP_EQ, "==", self.n_linha, self.n_column)					
				else:
					self.__estado = 1 # estado 7
					self.pointer_file()
					return Token(Tag_Type.OP_ASS, "=", self.n_linha, self.n_column)					

			
			elif self.__estado == 8: # CASE 8
				if self.c == "=":
					self.__estado = 1 # estado 9
					return Token(Tag_Type.OP_ASS, "=", self.n_linha, self.n_column)	
				else:
					self.__estado = 1 # estado 10
					self.pointer_file()
					return Token(Tag_Type.OP_GT, "=", self.n_linha, self.n_column)					

			elif self.__estado == 11: # CASE 11
				if self.c == "=":
					self.__estado = 1 # estado 12
					return Token(Tag_Type.OP_NE, "!=", self.n_linha, self.n_column)
				else:
					self.__estado = 1 # estado 13
					self.pointer_file()
					print "Token Incompleto" #implemntar mensagem de error
					return None

			elif self.__estado == 16: # CASE 16
				if self.c == "/":
					self.__estado = 21
					pass
				elif self.c == "*":
					self.__estado = 17


				else:
					self.__estado = 1
					self.pointer_file()
					return Token(Tag_Type.OP_DIV, "/", self.n_linha, self.n_column)

			elif self.__estado == 21:
				if self.c == "\n":
					self.__estado = 1

			elif self.__estado == 17:
				if self.c == "*":
					if self.c == "/":
						self.__estado = 1



  			elif self.__estado == 14: # Case 2

  				if self.c.isalpha() or self.c.isdigit(): 
  					self.__list_lexema.append(self.c)


  				else:
  					self.__estado = 1 # Retorna para o comeco

  					self.lexema = self.__list_lexema
  					self.__list_lexema = []
  					

  					token =  self.__TS.get_token(''.join(map(str, self.lexema))) # converte lista em string
  					self.pointer_file()
  					if token == None: 
  						# se nao encontrar na tabela de simbolo, insere.
  						token = Token(Tag_Type.ID, ''.join(map(str, self.lexema)), self.n_linha, self.n_column)
	  					self.__TS.put_tabela_simbolo(token, randint(21,100))
	  					return token # retorna o novo token
  					
  					return token


def main():
	lexer = Lexer('HelloJavinha.jvn')
	while True:
		token = lexer.nex_token()
		if token == None:
			return
		if token.getLexema() == "EOF":
			return
		else:
			print >>sys.stderr, "Token: " + " '"+ str(token.toString()) +"' " + " Linha: " + str(lexer.n_linha) + " Coluna: " + str(lexer.n_column)


if __name__ == '__main__':
	main()

