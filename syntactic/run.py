from lexer import Lexer
from parser import Parser
import argparse

__author__ = "Marcos Magno de Carvalho"


class RunSyntatic(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        self.args = arg

    def start_syntatic(self):
        lexer = Lexer(self.args.file)
        parser = Parser(lexer)
        parser.start_parse()

        """
			implementar print TSstart_parse

        """


def main():    parser = argparse.ArgumentParser(
        description='Parse pra o AG')

    parser.add_argument('--file', type=str, required=False,
                        default='program_1.pasc', help='Um nome de arquivo para o Parse')

    run = RunSyntatic(parser.parse_args())
    run.start_syntatic()

if __name__ == '__main__':
    main()
