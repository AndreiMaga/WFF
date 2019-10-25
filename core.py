from node import Node
from wffparser import Parser
from syntax import Syntax


class Core():

    input_phrase = ""
    config = {}

    def __init__(self, input_phrase):
        self.input_phrase = input_phrase
        self.root = Node()
        self.load_config()
        self.syntax = Syntax(self.config)
        self.parser = Parser(input_phrase, self.config)

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
