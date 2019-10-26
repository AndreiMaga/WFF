from node import Node
from utils import fail
class Evaluator():

    def __init__(self, eval_config:dict, config:dict):
        self.config = config
        self.eval_config = eval_config
        self.was_set = False

    def setValues(self, root:Node):
        if(len(root.childs) == 0):
            if(root.info in self.eval_config):
                root.truth = self.eval_config[root.info]
            else:
                fail("404", (root.info, ))
        else:
            for child in root.childs:
                self.setValues(child)
        self.was_set = True

    def evaluate(self, root:Node):
        if(len(root.childs) == 2):
            if(root.info == self.config["notations"]["binary"]["and"]):
                rez = self.evaluate(root.childs[0]) and self.evaluate(root.childs[1])
                return rez
            if(root.info == self.config["notations"]["binary"]["or"]):
                rez = self.evaluate(root.childs[0]) or self.evaluate(root.childs[1])
                return rez
            if(root.info == self.config["notations"]["binary"]["equals"]):
                rez = self.evaluate(root.childs[0]) == self.evaluate(root.childs[1])
                return rez
            if(root.info == self.config["notations"]["binary"]["implies"]):
                rez = self.implies(self.evaluate(root.childs[0]),self.evaluate(root.childs[1]))
                return rez
        elif(len(root.childs) == 1):
            if(root.info == self.config["notations"]["unary"]["not"]):
                return not self.evaluate(root.childs[0])
        else:
            return root.atom()
    def implies(self, a:bool,b:bool):
        if(a == True and b == False):
            return False
        return True