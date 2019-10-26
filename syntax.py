from node import Node
from utils import fail

class Syntax():

    def __init__(self, config: dict):
        self.config = config
        self.root = None

    def set_root(self, root: Node):
        self.root = root

    def recon(self, root: Node):
        rez = ""
        if(root.info in self.config["notations"]["binary"].values()):
            rez += "(" + self.recon(root.childs[0]) + \
                root.info + self.recon(root.childs[1]) + ")"
        elif(root.info in self.config["notations"]["unary"].values()):
            rez += "(" + root.info + self.recon(root.childs[0]) + ")"
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

    def validate(self):
        import re
