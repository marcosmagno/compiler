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
		#print >>sys.stderr,'Terminando'
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
			except IOError as e:
				raise e
			
			# Se chegar no fim do arquivo
			if not self.c:
				return False

			time.sleep(0.3)
			
			print "Read a character:", self.c
			if self.__estado == 1: # Case 1
				if not self.c:
					print "End of file"
					return False

				elif self.c == "\n":
					self.n_linha = self.n_linha + 1
					self.n_column = 0
					pass
				elif self.c == '\t':
					pass
				elif self.c == " ":
					pass

				elif self.c.isalpha():
					self.__list_lexema.append(self.c)
					self.__estado = 2

  			elif self.__estado == 2: # Case 2
  				if self.c.isalpha() or self.c.isdigit():
  					self.__list_lexema.append(self.c)
  				else:
  					self.__estado = 1 # Retorna para o comeco
  					self.lexema = self.__list_lexema
  					self.__list_lexema = []
  					 	
  					token =  self.__TS.get_token(''.join(map(str, self.lexema))) # converte lista em string

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
		print >>sys.stderr, "Token: " + str(token.toString())  + "Linha: " + str(lexer.n_linha) + " Coluna: " + str(lexer.n_column)
		if token == False:
			return


if __name__ == '__main__':
	main()

