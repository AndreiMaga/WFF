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