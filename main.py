from core import Core
from node import Node
from pprint import pprint

input_phrase = "((P&R)|Q)"
config = {
    'P' : False,
    'R' : False,
    'Q' : True
}

def __init__():
    c = Core(input_phrase)
    c.createEvaluator(config)
    c.check_syntax()
    #print(c.evaluate())
    pprint(c.evaluate_all_interpretations())


if __name__ == "__main__":
    __init__()
