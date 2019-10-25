from node import Node


class Syntax():

    def __init__(self, config):
        self.config = config
        self.root = None

    def set_root(self, root):
        self.root = root

    def recon(self, root):
        rez = ""
        for child in root.childs:
            if(child.info in self.config["notations"]["binary"]):
                rez += self.recon(child) + child.info + \
                    self.recon(root.childs[1])
            elif(child.info in self.config["notations"]["unary"]):
                rez += child.info + self.recon(child)
            else:
                rez += child.info

        return rez

    def reconstruct(self):
        return self.recon(self.root)

    def check_childs(self, child):
        if (child.info in self.config["notations"]["binary"]) and \
                len(child.childs != 2):
            return False
        if child.info in self.config["notations"]["unary"] and \
                len(child.childs != 1):
            return False
        elif len(child.childs) != 0:
            return False
        return True

    def check(self, root):
        for child in root.childs:
            if(self.check_childs(child)):
                return self.check(child)
            else:
                print("Failed at child ", child.to_string())
                return False
        return True

    def check_syntax(self):
        return self.check(self.root)

    def validate(self):
        import re
