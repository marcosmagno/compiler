from lexer import Lexer
from parser import Parser
__author__ = "Marcos Magno de Carvalho"


class RunSyntatic(object):
    """docstring for ClassName"""

    def start(self):
        
        lexer = Lexer("program_1.pasc")
        parser = Parser()



def main():
    run = RunSyntatic()
    run.start()

if __name__ == '__main__':
    main()
