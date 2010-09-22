
class Parser(object):
    """
    Takes an array of tokens and transforms them into a AST
    """
    
    def __init__(self, tokens):
        """
        
        Arguments:
        - `tokens`: an array of tokens
        """
        self._tokens = tokens
        
