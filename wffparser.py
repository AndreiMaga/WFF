from node import Node
from utils import fail

class Parser():
    """Parser for well formated formulas
    
    Returns:
        Parser -- instance of Parser
    """

    def __init__(self, input_phrase, config):
        """Constructor
        
        Arguments:
            input_phrase {str} -- The input string
            config {dict} -- The dictionary containing the configuration
        """
        self.input_phrase = input_phrase
        self.root = Node()
        self.config = config
        self.expected_depth = 0

    def parse(self):
        """The parse method, this should be called from outside the class
        """
        self.parser(self.input_phrase, self.root, 0)

        if(len(self.root.childs) != 0):
            self.root = self.root.childs[0]

    def add_node(self, root, ch):
        """Add a node to root
        
        Arguments:
            root {Node} -- The root you want to add a node to
        """
        n = Node()
        n.parent = root
        n.nr = ch
        n.depth = root.depth + 1
        root.childs.append(n)

    def check_depth_rec(self, root: Node, max_depth: int):
        """Check the depth recursevly
        
        Arguments:
            root {Node} -- The root
            max_depth {int} -- the maximum depth found
        
        Returns:
            int -- The maximum value of max_depth and the depth of the root
        """
        if len(root.childs) != 0:
            for child in root.childs:
                max_depth = self.check_depth_rec(child, max_depth)
        return max(max_depth, root.depth)

    def check_depth(self, root: Node):
        """Check the depth, will call the recursive one
        
        Arguments:
            root {Node} -- The starting node
        """
        if(self.expected_depth == 0):
            self.get_expected_depth(self.input_phrase)
        ch = self.check_depth_rec(root, 1)
        if(ch != self.expected_depth or root.childs[0].info == ""):
            fail("ret", (-1, ))

    def get_expected_depth(self, input_phrase: str):
        """Will calculate the expected depth from brackets
        
        Arguments:
            input_phrase {str} -- The input string
        """
        max_par = 0
        cur_par = 0
        for c in input_phrase:
            if(c is self.config["notations"]["brackets"]["open"]):
                cur_par += 1
            elif(c is self.config["notations"]["brackets"]["close"]):
                cur_par -= 1
            max_par = max(max_par, cur_par)

        self.expected_depth = max_par + 1

    def parser(self, input_phrase, root: Node = None, p: int = 0):
        """The parser method, it parses the input_phrase and stores the output in root

        Arguments:
            input_phrase {str} -- The input string
            root {Node} -- The current node (default: {None})
            p {int} -- The current position (default: {0})
        """
        if len(input_phrase) == 1:
            if input_phrase == ")":
                """Last character should be ) or else, fail
                """
                self.check_depth(self.root)
                return
            fail("ret", (p, ))
        ch = 0
        if(len(root.childs) == 0):
            """If the root has 0 childs, create 1
            """
            self.add_node(root, ch)

        if root.childs[0].info != "":
            """Change to the second child if the first one is filled
            """
            ch = 1
        try:
            if(input_phrase[0] == self.config["notations"]["brackets"]["open"]):
                """ If it's an open bracket, go to the child of root
                """
                self.parser(input_phrase[1:], root.childs[ch], p + 1)

            elif(input_phrase[0] in self.config["notations"]["binary"].values()):
                """This should be hit only when a binary relation is hit
                Set the root info to the sign, add a new node for the second 
                atom, and continue
                """
                root.set_info(input_phrase[0])
                self.add_node(root, ch)
                self.parser(input_phrase[1:], root, p + 1)

            elif(input_phrase[0] in self.config["notations"]["unary"].values()):
                """This should be hit only when a negation is hit
                Set the root to the negation sign and continue
                """
                root.set_info(input_phrase[0])
                self.parser(input_phrase[1:], root, p + 1)

            elif(input_phrase[0] == self.config["notations"]["brackets"]["close"]):
                """If the character is an closed bracket, jump back with the root
                """
                if(root.parent.info in self.config["notations"]["unary"].values()):
                    """If it's negation, jump twice
                    """
                    self.parser(input_phrase[1:], root.parent.parent, p + 1)
                else:
                    self.parser(input_phrase[1:], root.parent, p + 1)

            else:
                """This should be hit only when it's an atom
                """
                root.childs[ch].info = input_phrase[0]
                self.parser(input_phrase[1:], root, p + 1)
        except:
            fail("parse", (p,))
