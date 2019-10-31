from node import Node
from utils import fail

class Syntax():

    def __init__(self, config: dict):
        self.config = config
        self.root = None
        self.atom_list = []
        self.operations = []

    def set_root(self, root: Node):
        self.root = root

    def recon(self, root: Node):
        rez = ""
        if(root.info in self.config["notations"]["binary"].values()):
            r = "(" + self.recon(root.childs[0]) + \
                root.info + self.recon(root.childs[1]) + ")"
            rez += r
            self.operations.append(r)
        elif(root.info in self.config["notations"]["unary"].values()):
            r = "(" + root.info + self.recon(root.childs[0]) + ")"
            rez += r
            self.operations.append(r)
        else:
            rez += root.info

        return rez

    def reconstruct(self):
        return self.recon(self.root)

    def check_childs(self, root: Node):
        if root.info in self.config["notations"]["binary"].values():
            if len(root.childs) != 2:
                return False
            return True
        elif root.info in self.config["notations"]["unary"].values():
            if len(root.childs) != 1:
                return False
            return True
        elif len(root.childs) != 0:
            return False
        return True

    def check(self, root: Node):
        if(root.info == ""):
            return False
        if len(root.childs) > 2:
            fail("syntax",(root,))
            return False

        for child in root.childs:
            if(self.check_childs(child)):
                self.check(child)
            else:
                fail("syntax", (child, ))
                return False
        return True

    def check_syntax(self):
        return self.check(self.root)

    def validate(self, input_string):
        import re
        # construct regex
        regex = "([A-Za-z"
        regex += ''.join([i for i in self.config['notations']['brackets'].values()])
        regex += ''.join([i for i in self.config['notations']['unary'].values()])
        regex += ''.join([i for i in self.config['notations']['binary'].values()])
        regex += "])"
        reg = re.findall(regex, input_string)
        if len(reg) != len(input_string):
            fail("val", (reg, input_string))

        # get all atoms
        regex = "([A-Za-z])"
        reg = re.findall(regex, input_string)
        for i in reg:
            if i not in self.atom_list:
                self.atom_list.append(i)
        return True