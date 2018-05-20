import logging
import sys
import time
from tag import Tag_type


class Parser(object):
	"""docstring for Parser"""

	def __init__(self, lexer):
		self.lexer = lexer
		self.tag = Tag_type()
		self.token = self.lexer.nex_token()

	def sinaliza_erro(self, mensagem):

		print "Erro Sintatico:" + str(self.lexer.get_row())
		print mensagem

	def advance(self):
		self.token = self.lexer.nex_token()

	def eat(self, recv_token):
		print "eat: " + str(self.token.getClass()) + " " + str(recv_token)
		if (self.token.getClass() == recv_token):
			self.advance()
			return True
		else:
			return False

	def start_parse(self):
		# prog -> "program"
		if self.token.getClass() == self.tag.KW_PROGRAM:
			self.prog()  # chama o procedimento para o nao terminal prog
		else:
			self.sinaliza_erro(
				"Esperado program, encontrado: " + str(self.token.getLexema()))

		"""

			Todos os procedimentos para nao terminal

	"""

	def prog(self):
		# prog -> "program" "id" body
		if (self.eat(self.tag.KW_PROGRAM)):  # se for True
			if self.eat(self.tag.ID) != True:  # espera um ID
				print "Erro. Esperado ID, encontrado: ", self.token.getLexema()
				exit(1)
		self.body()

	def body(self):
		# body -> decl-list "{" stmt-list "}"
		if self.token.getClass() == self.tag.KW_NUM or self.token.getClass() == self.tag.KW_CHAR:
			self.decl_list()
		elif self.token.getClass() == self.tag.SMB_OBC:
				if self.eat(self.tag.SMB_OBC) != True:
					self.sinaliza_erro(
					"Esperado { , encontrado: " + str(self.token.getLexema()))
				
				self.stmt_list()
				if self.eat(self.tag.SMB_CBC) != True:
					print "erro, esperado } encontrado", self.token.getClass()
		else:
			self.sinaliza_erro(
				"Esperado dcls , encontrado: " + str(self.token.getLexema()))


	def decl_list(self):
		# decl_lit - > decl ";" decl-list | vazio
		self.decl()
		if self.eat(self.tag.SMB_SEM) != True: #;
			self.sinaliza_erro(
				"Esperado ; , encontrado: " + str(self.token.getLexema()))
		
		self.body()
		if self.token.getClass() == self.tag.SMB_OBC:  # {
			return

	def decl(self):
		# decl-> type id-list
		if self.type():
			self.id_list()
			return True
		else:
			return 

	def type(self):
		# type -> "num" | "char"
		if self.token.getClass() == self.tag.KW_NUM or self.token.getClass() == self.tag.KW_CHAR:
			d = self.token.getClass()
			if self.eat(d) != True:
				self.sinaliza_erro(
					"Esperadosss num , encontrado: " + str(self.token.getLexema()))
				return False
			else:
				return True
		else:
			return

	def id_list(self):
		# id-list -> id | w
		if self.eat(self.tag.ID) != True:  # espera um ID
			print "Erro. Esperado ID, encontrado: ", self.token.getLexema()
			exit(1)


		if self.token.getClass() == self.tag.SMB_COM:  # ,
			self.id_list_linha()

		else:
			return
	def id_list_linha(self):
		if self.eat(self.tag.SMB_COM) != True: #,
			self.sinaliza_erro(
				"Esperadosss , , encontrado: " + str(self.token.getLexema()))

		else:
			self.id_list()

	def stmt_list(self):
		print "Procedimento smt)list"

		return


