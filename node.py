

class Node():

    def __init__(self):
        self.parent = ""
        self.childs = []
        self.info = ""
        self.truth = False
        self.depth = 0
        self.nr = 0

    def set_info(self, info):
        self.info = info


    def to_string(self):
        if(self.parent.info != ""):
            return "Child number "+ str(self.nr)+" of " + self.parent.to_string() + " at " + self.info
        return self.info

    def atom(self):
        return self.truth
