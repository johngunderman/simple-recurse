import lexer

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
        self.root_node = ASTNode(None, None, lexer.ROOT)
        self._current_node = self._root_node
        
        for token in self._tokens:
            # (, add, 1, 3, )
            if token.is_open():
                new_node = ASTNode(self._current_node, None, lexer.EXP)
                self._current_node = new_node
            elif token.is_close():
                self._current_node = self._current_node.get_parent()
            elif token.is_symbol():
                new_node = ASTNode(self._current_node, token.value, lexer.SYMBOL)
                self._current_node.add_child(new_node)
            elif token.is_num():
                new_node = ASTNode(self._current_node, token.value, lexer.NUM)
                self._current_node.add_child(new_node)

        # check to make sure that our parentheses were balanced
        if  self._current_node != self._root_node:
            raise Exception("ERROR: Mismatched parenthesis")
                


        

class ASTNode(object):
    """
    A Node in our AST
    """
    
    def __init__(self, parent, value, n_type):
        """
        Generate a node with said parent, value,and type.
        
        Arguments:
        - `parent`:The parent for this node
        - `value`: The value contained by this node
        - `n_type`:The type of hte value contained by this node
        """
        self._parent = parent
        self._value = value
        self._n_type = n_type
        self._child_nodes = []

    def add_child(self, node):
        """
        Adds a child to thie list of children for this node
        
        Arguments:
        - `node`: The given ASTNode
        """
        node.set_parent_node(self)
        self._child_nodes.append(node)
        

    def set_parent_node(self, node):
        """
        Set this ASTNodes parent to `node`, and adds itself to the parent's listed child nodes.
        """
        self._parent = node
        # we should only have node == None for the root node
        if node != None:
            node.add_child(self);


    def get_parent(self, ):
        """
        Returns the parent of this node.
        """

        return self._parent
        
