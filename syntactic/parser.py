#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
import time
from tag import Tag_type


class Parser(object):
    """ This class is responsible for being part of the pasc grammar
        Attributes:
            lexer   (object)    : An object of class Lexer
            tag     (object)    : An object of class Tag_type
            token   (string)    : A string representing a token
    """

    def __init__(self, lexer):
        """ This is constructor of class Parser """
        self.lexer = lexer
        self.tag = Tag_type()
        self.token = self.lexer.next_token()

    def sinaliza_erro(self, mensagem):
        """ This method is responsible for signaling an error
            Attributes:
                mensagem (string)   : A string representing a erro mensagem
        """
        print "Erro Sintatico:" + str(self.lexer.get_row())
        print mensagem

    def advance(self):
        self.token = self.lexer.next_token()  # get next token

    def eat(self, recv_token):
        """ This method is responsible for consume a token """

        print "eat: " + str(self.token.getClass()) + ":" + str(self.token.getLexema()) + "   " + str(recv_token) + ":" + str(self.token.getLexema())
        if (self.token.getClass() == recv_token):
            self.advance()
            return True
        else:
            return False

    def start_parse(self):

        if self.token.getClass() == self.tag.KW_PROGRAM:
            self.prog()  # chama o procedimento para o nao terminal prog
        else:
            self.sinaliza_erro(
                "Esperado program, encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

    def prog(self):
        """ To produce:
                prog -> "program" "id" body(1)
        """

        if (self.eat(self.tag.KW_PROGRAM)):
            if self.eat(self.tag.ID) != True:  # Expect an ID
                print "Erro. Esperado ID, encontrado: ", self.token.getLexema()
                exit(1)
        self.body()

    def body(self):
        """ (1)
            To produce:
                body -> decl-list "{" stmt-list "}" (2)
        """

        # Expect a constant
        if self.token.getClass() == self.tag.KW_NUM or self.token.getClass() == self.tag.KW_CHAR:
            self.decl_list()
        else:
            if self.eat(self.tag.SMB_OBC) != True:  # {
                self.sinaliza_erro(
                    "Esperado { , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)

            self.stmt_list()

            if self.eat(self.tag.SMB_CBC) != True:  # }
                self.sinaliza_erro(
                    "Esperado } , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)

            if self.token.getClass() == self.tag.EOF:
                sys.exit(0)
            else:
                self.start_parse()

    def decl_list(self):
        """ To produce:
                decl_lit - > decl ";" decl-list (3) | vazio(4)
        """
        self.decl()

        if self.eat(self.tag.SMB_SEM) != True:  # Expect a ;
            self.sinaliza_erro(
                "Esperado ; , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        self.body()  # Call body
        if self.token.getClass() == self.tag.SMB_OBC:  # {
            return

    def decl(self):
        """ To produce:
                decl-> type id-list (5)
        """

        if self.type():
            self.id_list()
            return
        else:
            return

    def type(self):
        """ To produce:
                type -> "num" (6) | "char" (7)
        """
        d = self.token.getClass()
        if self.eat(d) != True:
            self.sinaliza_erro(
                "Esperados num , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)
            return False
        else:
            return True

    def id_list(self):
        """ To produce:
                id-list -> "id" id_list' (8)
        """
        if self.eat(self.tag.ID) != True:  # Expect a ID
            self.sinaliza_erro(
                "Esperado ID  , encontrado: " + str(self.token.getLexema()))
            sys.exit(1)

        if self.token.getClass() == self.tag.SMB_COM:
            self.id_list_linha()
        else:
            return

    def id_list_linha(self):
        """ To produce:
                id-list' -> "," id_list (9)
        """
        if self.eat(self.tag.SMB_COM) != True:  # Expect a ,
            self.sinaliza_erro(
                "Esperados , , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)
        else:
            self.id_list()  # (9)

    def stmt_list(self):
        """ (2)
            To produce:
                stmp-list -> stmt ";" stmt-list (11) | vazio (12)
        """
        if self.token.getClass() == self.tag.ID or self.token.getClass() == self.tag.KW_IF or self.token.getClass() == self.tag.KW_WHILE or self.token.getClass() == self.tag.KW_READ or self.token.getClass() == self.tag.KW_WRITE:
            self.stmt()
            if self.eat(self.tag.SMB_SEM) != True:
                self.sinaliza_erro(
                    "Esperado ;  , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)

            self.stmt_list()  # (11)
        else:
            return  # return to (1)

    def stmt(self):
        """ To produce:
            stmt -> assing-stmt (13) | if-stmt (14) | while-stmt (15) | read-stmt (16) | write-stmt (17)
        """

        if self.token.getClass() == self.tag.ID:
            self.assing_stmt()

        elif self.token.getClass() == self.tag.KW_IF:
            self.if_stmt()

        elif self.token.getClass() == self.tag.KW_WHILE:
            self.while_stmt()

        elif self.token.getClass() == self.tag.KW_READ:
            self.read_stmt()

        elif self.token.getClass() == self.tag.KW_WRITE:
            self.write_stmt()

    def assing_stmt(self):
        """ To produce:
                assing-stmt -> "id" "=" simple_exprt (18)
        """

        if self.eat(self.tag.ID) != True: 	# Expect q id
            self.sinaliza_erro(
                "Esperadosss ID , encontrado: " + str(self.token.getLexema()))
            exit(0)

        if self.eat(self.tag.OP_ASS) != True:  # Expect a =
            self.sinaliza_erro(
                "Esperados = , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.simple_exprt()

    def if_stmt(self):
        """
            produces:
                if-stmt -> "if" "(" condition ")" "{" stmt-list "}" if_stmt' (19)
        """

        if self.eat(self.tag.KW_IF) != True:  # Expect a if
            self.sinaliza_erro(
                "Esperado IF , encontrado: " + str(self.token.getLexema()))
            exit(0)

        # produce ( and call expression
        if self.token.getClass() == self.tag.SMB_OPA:
            self.expression()

        # prodduce { and call stm_list
        if self.eat(self.tag.SMB_OBC) != True:  # Expect a {
            self.sinaliza_erro(
                "Esperado { , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.stmt_list()

        if self.eat(self.tag.SMB_CBC) != True:  # Expect a }
            self.sinaliza_erro(
                "Esperado } , encontrado: " + str(self.token.getLexema()))
            exit(0)

        # produce else
        if self.token.getClass() == self.tag.KW_ELSE:
            self.if_stmt_linha()

        return

    def if_stmt_linha(self):
        """ To produces:
                if-stmt_linha -> "else" "{" stmt-list "}" (20) | vazio (21)
        """
        if self.eat(self.tag.KW_ELSE) != True:  # Expect a else
            self.sinaliza_erro(
                "Esperado else , encontrado: " + str(self.token.getLexema()))
            exit(0)

        if self.eat(self.tag.SMB_OBC) != True:  # Expect a  {
            self.sinaliza_erro(
                "Esperado { , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.stmt_list()  # Produc stm_list

        if self.eat(self.tag.SMB_CBC) != True:  # Expect a  }
            self.sinaliza_erro(
                "Esperado } , encontrado: " + str(self.token.getLexema()))
            exit(0)

    def while_stmt(self):
        """ To produces:
                while-stmt → stmt-prefix “{“ stmt-list “}” (23)
        """

        self.stmt_prefix()

        if self.eat(self.tag.SMB_OBC) != True:  # Expect a {
            self.sinaliza_erro(
                "Esperado { , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        self.stmt_list()

        if self.eat(self.tag.SMB_CBC) != True:  # Expect a }
            self.sinaliza_erro(
                "Esperado } , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        return

    def stmt_prefix(self):
        """To produces:
                "while" "(" condition ")" (24)
        """

        if self.eat(self.tag.KW_WHILE) != True:  # Expect awhile
            self.sinaliza_erro(
                "Esperado while , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.expression()

        return

    def read_stmt(self):
        """To proceduces:
                "read" "id" (25)
        """

        if self.eat(self.tag.KW_READ) != True:  # Expect a {
            self.sinaliza_erro(
                "Esperado { , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        if self.eat(self.tag.ID) != True:  # Expect a id
            self.sinaliza_erro(
                "Esperado ID , encontrado: " + str(self.token.getLexema()))
            exit(0)

    def write_stmt(self):
        """To proceduces:
                "write" writable
        """
        if self.eat(self.tag.KW_WRITE) != True:  # {
            self.sinaliza_erro(
                "Esperado write , encontrado: " + str(self.token.getLexema()))
            sys.exit(0)

        self.writable()

    def writable(self):
        """ To proceduces:
                writable-> simple-expr (27) | "literal" (28)
        """
        if self.token.getClass() == self.tag.LIT:
            if self.eat(self.tag.KW_WRITE) != True:  # {
                self.sinaliza_erro(
                    "Esperado write , encontrado: " + str(self.token.getLexema()))
                sys.exit(0)
        else:
            self.simple_exprt()

        return

   def expression(self):
        """ To proceduces:
                expression-> simple-expr expression_linha (29)
        """    
        if self.eat(self.tag.SMB_OPA) != True:  # (
            self.sinaliza_erro(
                "Esperados ( , encontrado: " + str(self.token.getLexema()))
            exit(0)

        self.simple_exprt() 

        # call expression_linha
        if self.token.getClass() == self.tag.OP_NE or self.token.getClass() == self.tag.OP_EQ or self.token.getClass() == self.tag.OP_GE or self.token.getClass() == self.tag.OP_LE or self.token.getClass() == self.tag.OP_GT or self.token.getClass() == self.tag.OP_LT:
            self.expression_linha()

        if self.eat(self.tag.SMB_CPA) != True:  # )
            self.sinaliza_erro(
                "Esperado ) , encontrado: " + str(self.token.getLexema()))
            exit(0)

        return



    def expression_linha(self):
        """ To proceduces:
                expression_linha-> relop expression (30) | vazio (31)
            Attribue:
                r (string): An string representing a signal reloop
        """           
        r = self.token.getClass()
        if self.eat(r) != True:  # Expect a (
            self.sinaliza_erro(
                "Esperadosss ( , encontrado: " + str(self.token.getLexema()))
            exit(0)
        # call simple_exprt
        self.simple_exprt() 


    def simple_exprt(self):
        """ To proceduces:
                simple-expr-> term simple_expr_linha (32)
        """              
        self.term()
        if self.token.getClass() == self.tag.OP_AD or self.token.getClass() == self.tag.OP_MIN or self.token.getClass() == self.tag.KW_OR:
            self.simple_expr_linha()
        else:
            return # return empty


    def simple_expr_linha(self):
        """ To proceduces:
                simple_expr_linha -> term simple_expr (33) | vazio (34)
            Attribue:
                addop (string): An string representing a signal addop
        """              
        addop = self.token.getClass()
        if self.eat(addop) != True:
            self.sinaliza_erro(
                "Esperados addop , encontrado: " + str(self.token.getLexema()))
            exit(0)
        self.term()


    def term(self):
        """ To produce:
                term -> factor_a term_linha (35)
        """
        self.factor_a()

        if self.token.getClass() == self.tag.OP_MUL or self.token.getClass() == self.tag.OP_DIV or self.token.getClass() == self.tag.KW_AND:
            self.term_linha()
        else:
            return


    def term_linha(self):
        """ To produce:
                term_linha -> mulop factor_a term_linha (36) | vazio (37)
            Attribute:
                mulop  (string) : An string representing a signal addop
        """        
        mulop = self.token.getClass()
        if self.eat(mulop) != True:
            self.sinaliza_erro(
                "Esperadosss mulop , encontrado: " + str(self.token.getLexema()))
       
        self.term()

    def factor_a(self):
        """ To produce:
                factor_a -> factor (38) | not factor (39)
        """
        if self.token.getClass() == self.tag.KW_NOT:
            if self.eat(self.tag.KW_NOT) != True:
                self.sinaliza_erro(
                    "Esperadosss not , encontrado: " + str(self.token.getLexema()))
                exit(0)

        self.factor()
        return


    def factor(self):
        """ To produce:
                factor -> “id” (40) | constant (41) | “(“ expression “)” (42)
            Attribute:
                c (string) : An string representing a signal addop
        """

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

 
