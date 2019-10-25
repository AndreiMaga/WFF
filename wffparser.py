from node import Node


class Parser():

    def __init__(self, input_phrase, config):
        self.input_phrase = input_phrase
        self.root = Node()
        self.config = config

    def parse(self):
        self.root = Node()
        self.parser(self.input_phrase, self.root, 0)

        self.root = self.root.childs[0]

    def fail(self, type="", args=()):
        import sys
        if type == "ret":
            print(
                "The input string is not a WFF. As the brakets are not ok at position", args[0])

        if type == "parse":
            print("Error at parsing the string. Error occured at ", args[0])

        sys.exit(1)

    def parser(self, input_phrase, root=None, p=0):
        if input_phrase == "":
            self.fail("parse", (p, ))

        if(len(root.childs) == 0):
                n = Node()
                n.parent = root
                root.childs.append(n)

        if(len(input_phrase) == 1 and input_phrase in self.config["notations"]["brackets"].values()):
            return
        ch = 0
        if root.childs[0].info != "":
            ch = 1

        if(input_phrase[0] == self.config["notations"]["brackets"]["open"]):
            self.parser(input_phrase[1:], root.childs[ch], p + 1)

        elif(input_phrase[0] in self.config["notations"]["binary"].values()):
            root.set_info(input_phrase[0])
            n = Node()
            n.parent = root
            root.childs.append(n)
            self.parser(input_phrase[1:], root, p + 1)

        elif(input_phrase[0] in self.config["notations"]["unary"].values()):
            root.set_info(input_phrase[0])
            self.parser(input_phrase[1:], root, p + 1)

        elif(input_phrase[0] == self.config["notations"]["brackets"]["close"]):
            if(root.parent.info in self.config["notations"]["unary"].values()):
                self.parser(input_phrase[1:], root.parent.parent, p + 1)
            else:
                self.parser(input_phrase[1:], root.parent, p + 1)
        else:
            root.childs[ch].info = input_phrase[0]
            self.parser(input_phrase[1:], root, p + 1)
