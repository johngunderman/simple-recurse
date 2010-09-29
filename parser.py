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
        self._current_node = self.root_node
        
        for token in self._tokens:
            # (, add, 1, 3, )
            if token.is_open():
                new_node = ASTNode(self._current_node, None, lexer.EXPR)
                self._current_node = new_node
            elif token.is_close():
                # check to make sure we are not trying to move up to a parent
                # that doesn't exist.
                if self._current_node.get_parent() == None:
                    raise Exception("ERROR: Mismatched Parentheses! (Too many)")
                self._current_node = self._current_node.get_parent()
            elif token.is_symbol():
                new_node = ASTNode(self._current_node, token.value, lexer.SYMBOL)
                self._current_node.add_child(new_node)
            elif token.is_num():
                new_node = ASTNode(self._current_node, token.value, lexer.NUM)
                self._current_node.add_child(new_node)

        # check to make sure that our parentheses were balanced
        if  self._current_node != self.root_node:
            raise Exception("ERROR: Mismatched parentheses (Too few)")


    def pretty_print(self, node, string="" ):
        """
        `node` : The node we want to pretty-print
        `string` : The current string representing our tree. Necessary for recursion.
        
        Print out the tree nicely. or as nicely as can be expected.
        Nice and recursive.
        """

        if node.n_type == lexer.EXPR or node.n_type == lexer.ROOT :
            for child in node.child_nodes:
                string += "("
                string += self.pretty_print(node=child, string=string)
                string += ")"
        if node.n_type == lexer.SYMBOL or node.n_type == lexer.NUM:
            string += str(node.value)

        return string
        

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
        self.value = value
        self.n_type = n_type
        self.child_nodes = []

    def add_child(self, node, set_parent=True):
        """
        Adds a child to thie list of children for this node
        
        Arguments:
        - `node`: The given ASTNode
        - `set_parent`: whether or not to set the child of the parent as the child.
        """
        if set_parent:
            node.set_parent_node(self)
        
        self.child_nodes.append(node)
        

    def set_parent_node(self, node):
        """
        Set this ASTNodes parent to `node`, and adds itself to the parent's listed child nodes.
        """
        self._parent = node
        # we should only have node == None for the root node
        if node != None:
            # we don't want infinite recursion, so set_parent=False
            node.add_child(self, set_parent=False);


    def get_parent(self, ):
        """
        Returns the parent of this node.
        """

        return self._parent
        
