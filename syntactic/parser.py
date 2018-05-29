#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        print "eat: " + str(self.token.getClass()) + ":" + str(self.token.getLexema()) + "   " + str(recv_token) + ":" + str(self.token.getLexema())
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
            sys.exit(0)

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
        else:
            if self.eat(self.tag.SMB_OBC) != True:  # {
                self.sinaliza_erro(
                    "Esperado { , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)

            self.stmt_list()

            if self.eat(self.tag.SMB_CBC) != True:
                self.sinaliza_erro(
                    "Esperado } , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)

    def decl_list(self):
        # decl_lit - > decl ";" decl-list | vazio
        self.decl()

        if self.eat(self.tag.SMB_SEM) != True:  # ;
            self.sinaliza_erro(
                "Esperado ; , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        self.body()
        if self.token.getClass() == self.tag.SMB_OBC:  # {
            return

    def decl(self):
        # decl-> type id-list
        if self.type():
            self.id_list()
            return
        else:
            return

    def type(self):
        # type -> "num" | "char"
        d = self.token.getClass()
        if self.eat(d) != True:
            self.sinaliza_erro(
                "Esperados num , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)
            return False
        else:
            return True

    def id_list(self):
        # id-list -> id | w
        if self.eat(self.tag.ID) != True:  # espera um ID
            self.sinaliza_erro(
                "Esperado ID  , encontrado: " + str(self.token.getLexema()))
            sys.exit(1)

        if self.token.getClass() == self.tag.SMB_COM:  # ,
            self.id_list_linha()
        else:
            return

    def id_list_linha(self):
        if self.eat(self.tag.SMB_COM) != True:  # ,
            self.sinaliza_erro(
                "Esperados , , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)
        else:
            self.id_list()

    def stmt_list(self):
        # stmp-list -> stmt ";" stmt-list | vazio
        if self.token.getClass() == self.tag.ID or self.token.getClass() == self.tag.KW_IF or self.token.getClass() == self.tag.KW_WHILE or self.token.getClass() == self.tag.KW_READ or self.token.getClass() == self.tag.KW_WRITE:
            self.stmt()
            if self.eat(self.tag.SMB_SEM) != True:
                self.sinaliza_erro(
                    "Esperado ;  , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)
            self.stmt_list()

        else:
            return  # retorna vazio

    def stmt(self):
        # stmt -> assing-stmt | if-stmt | while-stmt | read-stmt | write-stmt
        if self.token.getClass() == self.tag.ID:
            self.assing_stmt()

        elif self.token.getClass() == self.tag.KW_IF:
            self.if_stmt()

    def assing_stmt(self):
        # assing-stmt -> "id" "=" simple_exprt

        if self.eat(self.tag.ID) != True: 	# Id
            self.sinaliza_erro(
                "Esperadosss ID , encontrado: " + str(self.token.getLexema()))
            exit(0)

        if self.eat(self.tag.OP_ASS) != True:  # =
            self.sinaliza_erro(
                "Esperados = , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.simple_exprt()

    def if_stmt(self):
        if self.eat(self.tag.KW_IF) != True:
            self.sinaliza_erro(
                "Esperadosss IF , encontrado: " + str(self.token.getLexema()))
            exit(0)
        return

    def simple_exprt(self):
        # simple_exprt -> termA'
        # A' -> addop term | ε
        self.term()
        if self.token.getClass() == self.tag.OP_AD or self.token.getClass() == self.tag.OP_MIN or self.token.getClass() == self.tag.KW_OR:
            self.A_linha()
        else:
            return  # ε

    def term(self):
        # term -> factor-aB'
        # B' -> mulop factor - a | ε
        self.factor_a()
        if self.token.getClass() == self.tag.OP_MUL or self.token.getClass() == self.tag.OP_DIV or self.token.getClass() == self.tag.KW_AND:
            self.B_linha()
        else:
            return

    def factor_a(self):
        # factor-a -> factor | not factor
        if self.token.getClass() == self.tag.KW_NOT:
            if self.eat(self.tag.KW_NOT) != True:
                self.sinaliza_erro(
                    "Esperadosss not , encontrado: " + str(self.token.getLexema()))
                exit(0)

        self.factor()
        return

    def A_linha(self):
        addop = self.token.getClass()
        if self.eat(addop) != True:
            self.sinaliza_erro(
                "Esperados addop , encontrado: " + str(self.token.getLexema()))
            exit(0)
        self.term()

    def B_linha(self):
        mulop = self.token.getClass()
        if self.eat(mulop) != True:
            self.sinaliza_erro(
                "Esperadosss mulop , encontrado: " + str(self.token.getLexema()))
        self.term()

    def factor(self):
        # factor → “id” | constant | “(“ expression “)”
        if self.token.getClass() == self.tag.ID:
            if self.eat(self.tag.ID) != True:
                self.sinaliza_erro(
                    "Esperadosss ID , encontrado: " + str(self.token.getLexema()))
                exit(0)
            else:
                return
        elif self.token.getClass() == self.tag.CON_CHAR or self.token.getClass() == self.tag.CON_NUM:
            c = self.token.getClass()
            if self.eat(c) != True:
                self.sinaliza_erro(
                    "Esperados CON_NUM ou CON_CHAR , encontrado: " + str(self.token.getLexema()))
                exit(0)
            else:
                return

        elif self.token.getClass() == self.tag.SMB_OPA:  # (
            self.expression()

        return

    def expression(self):

        if self.eat(self.tag.SMB_OPA) != True:  # (
            self.sinaliza_erro(
                "Esperadosss ( , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.simple_exprt()  # expression -> simple-expr | c

        if self.token.getClass() == self.tag.OP_NE or self.token.getClass() == self.tag.OP_EQ or self.token.getClass() == self.tag.OP_GE or self.token.getClass() == self.tag.OP_LE or self.token.getClass() == self.tag.OP_GT or self.token.getClass() == self.tag.OP_LT:
            self.C()
        

        if self.eat(self.tag.SMB_CPA) != True:  # )
            self.sinaliza_erro(
                "Esperadosss ) , encontrado: " + str(self.token.getLexema()))
            exit(0)

        return

    def C(self):
        r = self.token.getClass()
        if self.eat(r) != True:  # (
            self.sinaliza_erro(
                "Esperadosss ( , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.simple_exprt()
