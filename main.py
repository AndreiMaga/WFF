from core import Core
from node import Node


input_phrase = "(((P&(!Q))@(Q@R))&(P&R))"
config = {
    'P' : True,
    'Q' : False,
    'R' : False
}

def __init__():
    c = Core(input_phrase)
    c.createEvaluator(config)
    print(c.evaluate())


if __name__ == "__main__":
    __init__()
