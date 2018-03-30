import time
from Tabela_Simbolo import TabelaSimbolo
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
		self.__lexema = []
		self.__ponteiro = 0
		#print >>sys.stderr,'Terminando'
		try:
			self.__file = open(input_file,'r')
			self.__lookahead = self.__file.read()

		except IOError as e:
			print "Erro to open file."



	def next_tonken(self):

	
		for c in range(self.__ponteiro, len(self.__lookahead)):
			
			
			print "CCCCCC", c
			print "ponteirooooo", self.__ponteiro
			self.__ponteiro = self.__ponteiro + 1
			self.n_column = self.n_column + 1
			print "ESTADO", self.__estado
			print "CARACTER", self.__lookahead[c]
			if self.__estado == 1:		# Case 1

				if ((c+1) == len(self.__lookahead)):					
					return "fim arquivo"


				elif self.__lookahead[c] == "\n":						
					print "QUEBRA LINHA"
					#self.n_linha = self.n_linha + 1
					#self.n_column = 0
				
				elif self.__lookahead[c] == "\t":
					print "TABULACAO"
					#self.n_linha = self.n_linha + 3
				elif self.__lookahead[c] == ' ':
					print "ESPACO"
				
				elif self.__lookahead[c].isalpha():						
					print "IS ALPHA"

					self.__lexema.append(self.__lookahead[c])
					self.__estado = 2

				elif self.__lookahead[c] == ";":
					self.__ponteiro = self.__ponteiro - 1
					print "PARENTESE"

				elif self.__lookahead[c] == "}":
					self.__ponteiro = self.__ponteiro - 1
					print "TOKEM = }"



			elif self.__estado == 2:	# Case 2
				
				if self.__lookahead[c].isalpha() or self.__lookahead[c].isdigit():
					self.__lexema.append(self.__lookahead[c])
					
					if ((c+1) == len(self.__lookahead)):					
						print "LEXEMAs", self.__lexema
					

				else: # estado = 3
					
					self.__ponteiro = self.__ponteiro - 1
					print "lexema", self.__lexema
					self.__estado = 1
					self.__lexema = []


			elif self.__estado == 3:
				print "EST 3"
				self.__estado = 1
		


def main():
	lexer = Lexer('HelloJavinha.jvn')
	while True:
		 token = lexer.next_tonken()
		 print token
		 if token == None:
		 	break
	


if __name__ == '__main__':
	main()

