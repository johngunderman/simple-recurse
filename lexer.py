import string


SYMBOL = "symbol"
NUM = "num"
ROOT = "root"
EXPR = "expr"


class Lexer(object):
    """
    Tokenizes our input file.
    """
    
    def __init__(self, input_code):
        """
        Takes in a string of code and breaks it into an array of its component parts
        Arguments:
        - `input_code`: a string of code
        """
        self._input_code = input_code
        self.tokens = []

        self.tokenize()


    def tokenize(self):
        tokens = [] # array of Token objects
        temp_token = ""
        
        for char in self._input_code:
            if char in "()":
                self.tokens.append(Token(char))
            elif char in string.letters:
                temp_token += char
            elif char in string.digits:
                temp_token += char
            elif char in string.whitespace:
                self.tokens.append(Token(temp_token))
                temp_token = ""

        return tokens


                
            
class Token(object):
    """
    data associated with a token
    """
    
    def __init__(self, value):
        """Make a new Token with given value and type
        
        Arguments:
        - `value`: literal value of the token
        """
        self.value = value

        if self.value in "()":
            self.t_type = SYMBOL
        if self.value[0] in string.letters:
            self.t_type = #FUUUUUU I forgot to add another type for () versus symbol-table symbols. Must fix after class.
        if self.value.isdigit():
            self.t_type = NUM
            self.value = float(self.value)


    def is_symbol(self, ):
        """
        Returns true if the  Token is of type symbol
        """
        return self.t_type == SYMBOL


    def is_num(self, ):
        """
        Returns true if Token is of type num
        """
        return  self.t_type == NUM


    def is_open(self):
        """
        Returns true if Token is '('
        """
        return self.value == '('

    def is_close(self):
        """
        Returns true if Token is ')'
        """
        return self.value == ')'
