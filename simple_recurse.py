from lexer import Lexer
from parser import Parser
from vm import VM
import sys


class SimpleRecurse(object):
    """
    Combines our lexer, parser,and vm together into a nice working interpreter
    """
    
    def __init__(self, input_code):
        """
        
        Arguments:
        - `input_code`: a string representation of the code in the text file.
        """
        self._input_code = input_code

        



if __name__ == '__main__':
    fname = sys.argv[1]
    fhandle = open(fname, "r")

    SimpleRecurse(fhandle.read())
