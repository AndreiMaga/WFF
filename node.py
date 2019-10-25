

class Node():

    def __init__(self):
        self.parent = ""
        self.childs = []
        self.info = ""
        self.truth = False

    def set_info(self, info):
        self.info = info

    def to_string(self):
        return "Informatia parintelui : " + self.parent.info + "\n" + "Informatia obiectului : " + self.info

    def atom(self):
        return self.truth
