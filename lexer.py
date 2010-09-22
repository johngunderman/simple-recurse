

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
        
