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

    def createEvaluator(self, config:dict):
        self.evaluator.eval_config = config


    def load_config(self):
        with open("config.json") as f:
            from json import load
            self.config = load(f)

    def parse(self):
        self.parser.parse()
        self.syntax.set_root(self.parser.root)

    def validate(self):
        if(self.syntax.root == None):
            self.parse()
        return self.syntax.validate()

    def check_syntax(self):
        if(self.syntax.root == None):
            self.parse()
        return self.syntax.check_syntax()

    def reconstruct(self):
        if(self.syntax.root == None):
            self.parse()
        return self.syntax.reconstruct()

    def evaluate(self):
        if(self.syntax.root == None):
            self.parse()
        if(self.evaluator.was_set == False):
            self.evaluator.setValues(self.syntax.root)
        return self.evaluator.evaluate(self.syntax.root)

    def evaluate_all_interpretations(self):
        if(self.syntax.root == None):
            self.parse()
        p = 2 ** len(self.evaluator.eval_config.keys()) - 1 # number of bits we need
        lbits = len(bin(p).split("b")[1])
        rez = []
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
            rez.append((l,self.evaluate()))
            p -= 1
        return rez

        