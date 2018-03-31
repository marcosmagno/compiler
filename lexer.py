import time
import sys
from tabela_simbolo import TabelaSimbolo
from token import Token
from tag import Tag_Type
from random import *
class Lexer(object):
	"""
		This class implements the lexical analyzer.
	"""

	def __init__(self, input_file):
		self.__TS = TabelaSimbolo()
		self.row = 1
		self.column = 1
		self.__state = 1 #
		self.__list_lexema = []
		self.lexema = []
		self.__list_digit = []
		self.digit = []
		self.__list_const_char = []

		# open the file
		try:
			self.__file = open(input_file,'r')
		except IOError as e:
			print "Erro to open file."

	def file_pointer(self):
		"""
			this method handles the pointer in the file

			seek() : Starts reading from the parameter that is passed
			tell() : Get an integer representing the position of the pointer 
			tell() - 1: returns a position on the pointer
		"""

		try:
			self.__file.seek(self.__file.tell() - 1)
		except Exception as e:
			raise e		

	def panic_mode(self):
		"""
			This methodo handles the panic mode
			tell() - 1: returns a position on the pointer
		"""
		try:
			self.__file.seek(self.__file.tell() - 1)
		except Exception as e:
			raise e
		

	def nex_token(self):
		''' 
		This method handles the input file
		Scroll through each character of the file
		Returns a token when found
			
		'''
		self.count_literal = 0
		while True:

			self.column = self.column + 1 

			# Read File
			try:
				self.c = self.__file.read(1)				
				if not self.c:
					return Token(Tag_Type.EOF, "EOF", self.row, self.column)				

			except IOError as e:
				raise e		

			if self.__state == 1: # CASE 1
				if not self.c:					
					return Token(Tag_Type.EOF, "EOF", self.row, self.column)				
				
				elif self.c == "\n":
					self.row = self.row + 1
					self.column = 1
					pass

				elif self.c == '\t':
					pass

				elif self.c == " ":					 
					pass

				elif self.c == "<":
					self.__state = 2

				elif self.c == "=":
					 self.__state = 5

				elif self.c == ">":
					self.__state = 8

				elif self.c == "!":
					self.__state = 11

				elif self.c == "-": 
					self.__state = 1 # estado 13
					return Token(Tag_Type.OP_MIN, "-", self.row, self.column)

				elif self.c == "+":
					self.__state = 1 # estado 14
					return Token(Tag_Type.OP_AD, "+", self.row, self.column)

				elif self.c == "{":
					self.__state = 1 # estado 25
					return Token(Tag_Type.SMB_OBC, "{", self.row, self.column)					
				
				elif self.c == "}":
					self.__state = 1 # estado 26
					return Token(Tag_Type.SMB_CBC, "}", self.row, self.column)					
				
				elif self.c == "(":
					self.__state = 1 # estado 27
					return Token(Tag_Type.SMB_OPA, "(", self.row, self.column)	

				elif self.c == ")":
					self.__state = 1 # estado 28
					return Token(Tag_Type.SMB_CPA, ")", self.row, self.column)					
				
				elif self.c == ",":
					self.__state = 1 # estado 29
					return Token(Tag_Type.SMB_COM, ",", self.row, self.column)					

				elif self.c == ";":
					self.__state = 1 # estado 30
					return Token(Tag_Type.SMB_SEM, ";", self.row, self.column)					
			

				elif self.c.isdigit():
					self.__list_digit.append(self.c)
					self.__state = 31

				elif self.c.isalpha():					
					self.__list_lexema.append(self.c)					
					self.__state = 35

				elif self.c == "'":
					self.__state = 40

	

			elif self.__state == 2: # CASE 2
				if self.c == "=":
					self.__state = 1
					return Token(Tag_Type.OP_LE, "<=", self.row, self.column)
				else:
					self.__state = 1
					self.file_pointer()
					self.column = self.column - 1

					return Token(Tag_Type.OP_LT, "<", self.row, self.column)


			elif self.__state == 5: # CASE 5
				if self.c == "=": # estado 6
				   self.__state = 1
				   return Token(Tag_Type.OP_EQ, "==", self.row, self.column)					
				else:
					self.__state = 1 # estado 7
					self.file_pointer()
					self.column = self.column - 1
					return Token(Tag_Type.OP_ASS, "=", self.row, self.column)					

			
			elif self.__state == 8: # CASE 8
				if self.c == "=":
					self.__state = 1 # estado 9
					return Token(Tag_Type.OP_ASS, "=", self.row, self.column)	
				else:
					self.__state = 1 # estado 10
					self.file_pointer()
					self.column = self.column - 1
					return Token(Tag_Type.OP_GT, "=", self.row, self.column)					

			elif self.__state == 11: # CASE 11
				if self.c == "=":
					self.__state = 1 # estado 12
					return Token(Tag_Type.OP_NE, "!=", self.row, self.column)
				else:
					self.__state = 1 # estado 13
					#self.file_pointer()
					self.column = self.column - 1
					print >>sys.stderr, "   ", "File ", self.__file.name, " \n\n\tLinha:", self.row , " Coluna: ", self.column, "\n\t invalid", "\n\n\t expected ="
					self.panic_mode()

  			elif self.__state == 31: # CASE 31
  				if self.c.isdigit():
  					self.__list_digit.append(self.c)
  				else:
  					if self.c == ".":
  						self.__list_digit.append(self.c)
  						self.__state = 32 # estado 32
  					else:
	  					self.__state = 1
	  					self.digit = self.__list_digit
	  					self.__list_digit = []
	  					self.file_pointer()
	  					self.column = self.column - 1
	  					return Token(Tag_Type.INTEGER, ''.join(map(str, self.digit)), self.row, self.column)

  			elif self.__state == 32:  # CASE 31
  				if self.c.isdigit():
  					self.__list_digit.append(self.c)
  					
  				else:
  					self.__state = 1	# estado 34
  					self.file_pointer()
  					self.column = self.column - 1
  					return Token(Tag_Type.DOUBLE, ''.join(map(str, self.__list_digit)), self.row, self.column)
  			

  			elif self.__state == 35: # Case 35
  				if self.c.isalpha() or self.c.isdigit(): 
  					self.__list_lexema.append(self.c)

  				else:
  					self.__state = 1 # # estado 36
  					self.lexema = self.__list_lexema
  					self.__list_lexema = []
  					

  					token =  self.__TS.get_token(''.join(map(str, self.lexema))) # Pesquisa na Tabela de Simbolo
  					self.file_pointer()
  					self.column = self.column - 1
  					if token == None: 
  						# se nao encontrar na tabela de simbolo, insere.
  						token = Token(Tag_Type.ID, ''.join(map(str, self.lexema)), self.row, self.column)
	  					self.__TS.put_tabela_simbolo(token, randint(21,100)) # Cadastra na Tabela de Simbolo
	  					return token # retorna o novo token  					
  					return token

  			elif self.__state == 40:
  				if self.c.isdigit() or self.c.isalpha() and self.c != "'":
  					self.__list_const_char.append(self.c)  					
  				else:
  					if self.c == "'":
  						self.__state = 1
  						if len(self.__list_const_char) > 1:
  							print "Erro para formar a Constante Char"
  							return None
  						else:
  							return Token(Tag_Type.CON_CHAR, ''.join(map(str, self.__list_const_char)), self.row, self.column)
  					





def main():
	lexer = Lexer('HelloJavinha.jvn')
	while True:
		token = lexer.nex_token()
		if token == None:
			return
		if token.getLexema() == "EOF":
			return
		else:
			print >>sys.stderr, "Token: " + " '"+ str(token.toString()) +"' " + " Linha: " + str(lexer.row) + " Coluna: " + str(lexer.column)


if __name__ == '__main__':
	main()

