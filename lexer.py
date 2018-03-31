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
		self.n_column = 1
		self._caracter = ''
		self.__estado = 1
		self.__list_lexema = []
		self.__ponteiro = 0
		self.lexema = []
		self.__list_digit = []
		self.digit = []
		self.__list_const_char = []
		try:
			self.__file = open(input_file,'r')
		except IOError as e:
			print "Erro to open file."

	def pointer_file(self):
		self.__file.seek(self.__file.tell() - 1)

	def mode_panic(self):
		self.__file.seek(self.__file.tell() - 1)

	def nex_token(self):

		self.count_literal = 0
		while True:

			self.n_column = self.n_column + 1 

			# Ler arquivo
			try:
				self.c = self.__file.read(1)				
				if not self.c:
					return Token(Tag_Type.EOF, "EOF", self.n_linha, self.n_column)				

			except IOError as e:
				raise e		
			#print self.c, self.n_column
			#time.sleep(0.5)
			if self.__estado == 1: # CASE 1
				if not self.c:					
					return Token(Tag_Type.EOF, "EOF", self.n_linha, self.n_column)				
				
				elif self.c == "\n":
					self.n_linha = self.n_linha + 1
					self.n_column = 1
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

				elif self.c == "{":
					self.__estado = 1 # estado 25
					return Token(Tag_Type.SMB_OBC, "{", self.n_linha, self.n_column)					
				
				elif self.c == "}":
					self.__estado = 1 # estado 26
					return Token(Tag_Type.SMB_CBC, "}", self.n_linha, self.n_column)					
				
				elif self.c == "(":
					self.__estado = 1 # estado 27
					return Token(Tag_Type.SMB_OPA, "(", self.n_linha, self.n_column)	

				elif self.c == ")":
					self.__estado = 1 # estado 28
					return Token(Tag_Type.SMB_CPA, ")", self.n_linha, self.n_column)					
				
				elif self.c == ",":
					self.__estado = 1 # estado 29
					return Token(Tag_Type.SMB_COM, ",", self.n_linha, self.n_column)					

				elif self.c == ";":
					self.__estado = 1 # estado 30
					return Token(Tag_Type.SMB_SEM, ";", self.n_linha, self.n_column)					
			

				elif self.c.isdigit():
					self.__list_digit.append(self.c)
					self.__estado = 31

				elif self.c.isalpha():					
					self.__list_lexema.append(self.c)					
					self.__estado = 35

				elif self.c == "'":
					self.__estado = 40

	

			elif self.__estado == 2: # CASE 2
				if self.c == "=":
					self.__estado = 1
					return Token(Tag_Type.OP_LE, "<=", self.n_linha, self.n_column)
				else:
					self.__estado = 1
					self.pointer_file()
					self.n_column = self.n_column - 1

					return Token(Tag_Type.OP_LT, "<", self.n_linha, self.n_column)


			elif self.__estado == 5: # CASE 5
				if self.c == "=": # estado 6
				   self.__estado = 1
				   return Token(Tag_Type.OP_EQ, "==", self.n_linha, self.n_column)					
				else:
					self.__estado = 1 # estado 7
					self.pointer_file()
					self.n_column = self.n_column - 1
					return Token(Tag_Type.OP_ASS, "=", self.n_linha, self.n_column)					

			
			elif self.__estado == 8: # CASE 8
				if self.c == "=":
					self.__estado = 1 # estado 9
					return Token(Tag_Type.OP_ASS, "=", self.n_linha, self.n_column)	
				else:
					self.__estado = 1 # estado 10
					self.pointer_file()
					self.n_column = self.n_column - 1
					return Token(Tag_Type.OP_GT, "=", self.n_linha, self.n_column)					

			elif self.__estado == 11: # CASE 11
				if self.c == "=":
					self.__estado = 1 # estado 12
					return Token(Tag_Type.OP_NE, "!=", self.n_linha, self.n_column)
				else:
					self.__estado = 1 # estado 13
					#self.pointer_file()
					self.n_column = self.n_column - 1
					print >>sys.stderr, "   ", "File ", self.__file.name, " \n\n\tLinha:", self.n_linha , " Coluna: ", self.n_column, "\n\t invalid", "\n\n\t expected ="
					self.mode_panic()

  			elif self.__estado == 31: # CASE 31
  				if self.c.isdigit():
  					self.__list_digit.append(self.c)
  				else:
  					if self.c == ".":
  						self.__list_digit.append(self.c)
  						self.__estado = 32 # estado 32
  					else:
	  					self.__estado = 1
	  					self.digit = self.__list_digit
	  					self.__list_digit = []
	  					self.pointer_file()
	  					self.n_column = self.n_column - 1
	  					return Token(Tag_Type.INTEGER, ''.join(map(str, self.digit)), self.n_linha, self.n_column)

  			elif self.__estado == 32:  # CASE 31
  				if self.c.isdigit():
  					self.__list_digit.append(self.c)
  					
  				else:
  					self.__estado = 1	# estado 34
  					self.pointer_file()
  					self.n_column = self.n_column - 1
  					return Token(Tag_Type.DOUBLE, ''.join(map(str, self.__list_digit)), self.n_linha, self.n_column)
  			

  			elif self.__estado == 35: # Case 35
  				if self.c.isalpha() or self.c.isdigit(): 
  					self.__list_lexema.append(self.c)

  				else:
  					self.__estado = 1 # # estado 36
  					self.lexema = self.__list_lexema
  					self.__list_lexema = []
  					

  					token =  self.__TS.get_token(''.join(map(str, self.lexema))) # Pesquisa na Tabela de Simbolo
  					self.pointer_file()
  					self.n_column = self.n_column - 1
  					if token == None: 
  						# se nao encontrar na tabela de simbolo, insere.
  						token = Token(Tag_Type.ID, ''.join(map(str, self.lexema)), self.n_linha, self.n_column)
	  					self.__TS.put_tabela_simbolo(token, randint(21,100)) # Cadastra na Tabela de Simbolo
	  					return token # retorna o novo token  					
  					return token

  			elif self.__estado == 40:
  				if self.c.isdigit() or self.c.isalpha() and self.c != "'":
  					self.__list_const_char.append(self.c)  					
  				else:
  					if self.c == "'":
  						self.__estado = 1
  						if len(self.__list_const_char) > 1:
  							print "Erro para formar a Constante Char"
  							return None
  						else:
  							return Token(Tag_Type.CON_CHAR, ''.join(map(str, self.__list_const_char)), self.n_linha, self.n_column)
  					
	  					
	  			#time.sleep(1)




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

