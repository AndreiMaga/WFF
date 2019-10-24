from node import Node
class Parser():

    def __init__(self, input_phrase, config):
        self.input_phrase = input_phrase
        self.root = Node()
        self.config = config

    def parse(self):
        self.root = Node()
        ret = self.parser(self.input_phrase, self.root, 0)
        if ( ret != 0):
            import sys
            print("The input string is not a WFF. As the brakets are not ok at position",ret)
            sys.exit(1)
        
        self.root = self.root.childs[0]

    def parser(self, input_phrase, root = None, p = 0):
        if input_phrase == "":
            return 0

        if( len(root.childs) == 0):
                n = Node()
                n.parent = root
                root.childs.append(n)
                
        ch = 0
        if root.childs[0].info != "":
            ch = 1
            
        if(input_phrase[0] == self.config["notations"]["brackets"]["open"]):
            lb = input_phrase.rfind(self.config["notations"]["brackets"]["close"])
            if(lb == -1):
                return p + 1
            return self.parser(input_phrase[1:lb], root.childs[ch], p + 1)

        elif(input_phrase[0] in self.config["notations"]["binary"].values()):
            root.set_info(input_phrase[0])
            n = Node()
            n.parent = root
            root.childs.append(n)
            return self.parser(input_phrase[1:], root, p + 1)

        elif(input_phrase[0] in self.config["notations"]["unary"].values()):
            root.set_info(input_phrase[0])
            return self.parser(input_phrase[1:], root, p + 1)

        else:
            root.childs[ch].info = input_phrase[0]
            return self.parser(input_phrase[1:], root, p + 1)