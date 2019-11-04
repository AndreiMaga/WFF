from node import Node
from wffparser import Parser
from syntax import Syntax
from evaluator import Evaluator

class Core():

    input_phrase = ""
    config = {}
    eval_config = {}

    def __init__(self, input_phrase:str):
        self.input_phrase = input_phrase
        self.root = Node()
        self.load_config()
        self.syntax = Syntax(self.config)
        self.parser = Parser(input_phrase, self.config)
        self.evaluator = Evaluator(self.eval_config, self.config)

    def update_evaluator(self, config:dict):
        for k in config:
            v = config[k]
            if(v == "True"):
                config[k] = True
            elif(v == "False"):
                config[k] = False
            else:
                from utils import fail
                fail("config", (k,v))
            
        self.evaluator.eval_config = config


    def load_config(self):
        with open("config.json") as f:
            from json import load
            self.config = load(f)

    def parse(self):
        self.syntax.validate(self.input_phrase)
        self.parser.parse()
        self.syntax.set_root(self.parser.root)

    def validate(self):
        if(self.syntax.root == None):
            self.parse()
        ret = self.syntax.validate(self.input_phrase)
        self.evaluator.eval_config = {i : False for i in self.syntax.atom_list}
        return ret

    def check_syntax(self):
        if(self.syntax.root == None):
            self.parse()
        return self.syntax.check_syntax()

    def reconstruct(self,):
        if(self.syntax.root == None):
            self.parse()
        return self.syntax.reconstruct()

    def evaluate(self, p = False):
        if(self.syntax.root == None):
            self.parse()
        if(self.evaluator.was_set == False):
            self.evaluator.setValues(self.syntax.root)

        rez = self.evaluator.evaluate(self.syntax.root)
        if p == True:
            from prettytable import PrettyTable
            self.reconstruct()
            table = PrettyTable([k for k in self.evaluator.eval_config.keys()] + self.syntax.operations)
            table.add_row([k for k in self.evaluator.eval_config.values()] + self.evaluator.results)
            print(str(table))
        return rez

    def evaluate_all_interpretations(self):
        if(len(self.evaluator.eval_config) == 0):
            self.validate()
            
        p = 2 ** len(self.evaluator.eval_config.keys()) - 1 # number of bits we need
        lbits = len(bin(p).split("b")[1])
        from prettytable import PrettyTable
        self.reconstruct()
        rez = PrettyTable([k for k in self.evaluator.eval_config.keys()] + self.syntax.operations)
        while p != -1:
            bits = [int(c) for c in bin(p).split("b")[1]]
            while( len(bits) < lbits):
                bits.insert(0, 0)
            i = 0
            l = []
            for k in self.evaluator.eval_config.keys():
                self.evaluator.eval_config[k] = bool(bits[i])
                l.append(bool(bits[i]))
                i += 1
            self.evaluator.was_set = False
            r = [self.evaluate()]
            rez.add_row(l + self.evaluator.results)
            self.evaluator.results = []
            p -= 1
        print(str(rez))

    def print_tree(self):
        if(self.syntax.root == None):
            self.parse()
        from pptree import print_tree
        print_tree(self.syntax.root, childattr='childs', nameattr='info')