import time
import sys
from tabela_simbolo import TabelaSimbolo
from token import Token
from tag import Tag_Type
from random import *
import string
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
		self.__list_literal = []
		self.__list_double = []
		self.double = []
		self._result_double = []


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

	def panic_mode(self, row, column, type_erro):
		"""
			This methodo handles the panic mode
			tell() - 1: returns a position on the pointer
		"""
		self.row_ = row
		self.column_ = column
		self.type_erro = type_erro
		self.erros = []
		self.command = ''

		self.command = ''.join(map(str, str(self.type_erro) + " Linha: " + str(self.row_) + " Coluna: " + str(self.column_)))
		print self.command

		


	def close_file(self):
		self.__file.close()
		

	def nex_token(self):
		''' 
		This method handles the input file
		Scroll through each character of the file
		Returns a token when found
		TODO:
			Alter state
			
		'''
		
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
				
				elif self.c == "\n": # state 1
					self.row = self.row + 1 # increase the line
					self.column = 1 # returns the column count
					pass

				elif self.c == '\t': # state 1
					pass

				elif self.c == " ":	 # state 1				 
					pass

				elif self.c == "<":
					self.__state = 2 # state 2 return of the state 3 or 4

				elif self.c == "=":
					 self.__state = 5 # state 5 return of the state 6 or 7

				elif self.c == ">":
					self.__state = 8 # state 8 return of the state 9 or 10
 
				elif self.c == "!":
					self.__state = 11 # state 11 return of the 11

				elif self.c == "-": 
					self.__state = 1 # state 13
					return Token(Tag_Type.OP_MIN, "-", self.row, self.column) # return of the state 13

				elif self.c == "+":
					self.__state = 1 # state 14
					return Token(Tag_Type.OP_AD, "+", self.row, self.column) # return of the state 14

				elif self.c == "{":
					self.__state = 1 # state 25
					return Token(Tag_Type.SMB_OBC, "{", self.row, self.column) # return of the state 25
				
				elif self.c == "}":
					self.__state = 1 # state 26
					return Token(Tag_Type.SMB_CBC, "}", self.row, self.column) # return of the state 26
				
				elif self.c == "(":
					self.__state = 1 # state 27
					return Token(Tag_Type.SMB_OPA, "(", self.row, self.column)	# return of the state 27

				elif self.c == ")":
					self.__state = 1 # state 28
					return Token(Tag_Type.SMB_CPA, ")", self.row, self.column) # return of the state 28
				
				elif self.c == ",":
					self.__state = 1 # state 29
					return Token(Tag_Type.SMB_COM, ",", self.row, self.column) # return of the state 29				

				elif self.c == ";":
					self.__state = 1 # state 30
					return Token(Tag_Type.SMB_SEM, ";", self.row, self.column) # return of the state 30			
			
				elif self.c == "/":
					self.__state = 16

				# build num_const
				elif self.c.isdigit():
					self.__list_digit.append(self.c) # return of the state 34
					self.__state = 31

				# build id
				elif self.c.isalpha():
					self.__list_lexema.append(self.c) # return of the state 36 ( install ID)
					self.__state = 35

				elif self.c == "'":
					self.__state = 40 # return of the state 42 ( return a char_const )

				elif self.c == "\"":
					self.__state = 37

				else:
					self.panic_mode(self.row, self.column, "Invalid Character")

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
				if self.c == "=": # state 6
				   self.__state = 1
				   return Token(Tag_Type.OP_EQ, "==", self.row, self.column)					
				else:
					self.__state = 1 # state 7
					self.file_pointer()
					self.column = self.column - 1
					return Token(Tag_Type.OP_ASS, "=", self.row, self.column)					

			
			elif self.__state == 8: # CASE 8
				if self.c == "=":
					self.__state = 1 # state 9
					return Token(Tag_Type.OP_GE, ">=", self.row, self.column)	
				else:
					self.__state = 1 # state 10
					self.file_pointer()
					self.column = self.column - 1
					return Token(Tag_Type.OP_GT, ">", self.row, self.column)					

			elif self.__state == 11: # CASE 11
				if self.c == "=":
					self.__state = 1 # state 12
					return Token(Tag_Type.OP_NE, "!=", self.row, self.column)
				else:

					self.file_pointer()
					self.__state = 1 # state 13
					self.column = self.column - 1
					self.panic_mode(self.row, self.column, "Invalid Character, expected =")

			elif self.__state == 16:
				if self.c == "*":
					self.__state = 17

				elif self.c == "/":
					self.__state = 21

				else:
					self.__state = 1
					self.file_pointer()
					return Token(Tag_Type.OP_DIV, ''.join(map(str, self.__list_digit + self.__list_double)), self.row, self.column)
			

			elif self.__state == 17:

				if self.c != "*":
					self.__state = 17
				else:	
					self.__state = 19					

			elif self.__state == 19:

				if self.c == "/":
					self.__state = 1
					pass


				else:
					self.__state = 17





			elif self.__state == 21:
				if self.c == " " or self.c == "\t" or self.c in string.letters or self.c.isdigit():
					self.__state = 21
				else:
					self.__state = 1
					self.file_pointer()
					pass
					#return Token(Tag_Type.COMENTARIO_UMALINHA, ''.join(map(str, self.__list_digit + self.__list_double)), self.row, self.column)

  			elif self.__state == 31: # CASE 31
  				if self.c.isdigit():
  					self.__list_digit.append(self.c)
  					self.__state = 31



  				else:
  					if self.c == ".": 						
  						self.__list_digit.append(self.c)
  						self.__list_double = self.__list_digit
  						self.__list_digit = []
  						self.__state = 32 # state 32


  					else:
	  					self.__state = 1
	  					self.digit = self.__list_digit
	  					self.__list_digit = []

	  					self.file_pointer()
	  					self.column = self.column - 1
	  					return Token(Tag_Type.INTEGER, ''.join(map(str, self.digit)), self.row, self.column)

  			elif self.__state == 32:  # CASE 31	
  				if self.c.isdigit():
  					self.double.append(self.c)

  					self.__state = 32  


  				else:
  					if not self.c.isdigit():
  						if len(self.double) >= 1:
  							self.__state = 1	# state 34
  							self.file_pointer()  							
  							self._result_double = self.__list_double + self.double
  							self.digit = self.__list_digit
  							self.__list_double = []
  							self.__list_digit = []
  							self.double = []
  							return Token(Tag_Type.DOUBLE, ''.join(map(str, self._result_double)), self.row, self.column)
  						else:
  							self.__list_double = []
  							self.__list_digit = []
  							self.double = []
  							self.file_pointer()
  							self.panic_mode(self.row, self.column, "Invalid Character, expected a integer")
							self.__state = 1
  					

  			elif self.__state == 35: # Case 35
  				if self.c.isalpha() or self.c.isdigit(): 
  					self.__list_lexema.append(self.c)

  				else:
  					self.__state = 1 # # state 36
  					self.lexema = self.__list_lexema
  					self.__list_lexema = []

  					token =  self.__TS.get_token(''.join(map(str, self.lexema))) # Pesquisa na Tabela de Simbolo.
  					self.file_pointer()
  					self.column = self.column - 1

  					if token == None:
  						# if not found in the symbol table, insert.
  						token = Token(Tag_Type.ID, ''.join(map(str, self.lexema)), self.row, self.column)

	  					self.__TS.put_tabela_simbolo(token, randint(21,100)) # insert in the symbol table.
	  					return token # returns a new token object.  					
  					return token

  			elif self.__state == 37:  		
  					
  				if self.c in string.whitespace or self.c in string.letters:
  					self.__list_literal.append(self.c)
  					self.__state = 37	  					
  					#time.sleep(2)  				
  				else:
  					if self.c == "\"":
  						self.__state = 1
  						return Token(Tag_Type.LITERAL, ''.join(map(str, self.__list_literal)), self.row, self.column)
  					else:
  						self.panic_mode(self.row, self.column,"Invalid Character expected \"")
  						#sprint >>sys.stderr, "   ", "File ", self.__file.name, " \n\n\tLinha:", self.row , " Coluna: ", self.column - 1, "\n\t invalid", "\n\t expected ""\"" "\n"
  						self.file_pointer()
  						self.__state = 1


  			elif self.__state == 40:
  				if self.c.isdigit() or self.c.isalpha() and self.c != "'":
  					self.__list_const_char.append(self.c)  					
  				else:
  					if self.c == "'":
  						self.__state = 1
  						if len(self.__list_const_char) > 1:
  							print >>sys.stderr, "   ", "File ", self.__file.name, " \n\n\tLinha:", self.row , " Coluna: ", self.column - 1, "\n\t invalid", "\n\t literal must contain only one character\n"  							
						else:
  							return Token(Tag_Type.CON_CHAR, ''.join(map(str, self.__list_const_char)), self.row, self.column)
  					

def main():
	#print "Symbol Tablessssssssssssss"
	#ts = TabelaSimbolo()
	#ts.get_ts()
	lexer = Lexer('erro_cassio.psc')
	while True:
		token = lexer.nex_token()
		if (token == None) or (token.getLexema() == "EOF"):
			lexer.close_file()
			return
		else:
			print >>sys.stderr, "Token: " + " '"+ str(token.toString()) +"' " + " Linha: " + str(lexer.row) + " Coluna: " + str(lexer.column)


if __name__ == '__main__':
	main()

