from lexer import Lexer
from parser import Parser
__author__ = "Marcos Magno de Carvalho"


class RunSyntatic(object):
    """docstring for ClassName"""

    def start_syntatic(self):
        
        lexer = Lexer("program_1.pasc")
        parser = Parser(lexer)
        parser.start_parse()


        """
			implementar print TSstart_parse

        """

def main():
    run = RunSyntatic()
    run.start_syntatic()

if __name__ == '__main__':
    main()
