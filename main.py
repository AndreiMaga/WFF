from core import Core
from node import Node


input_phrase = "((P&(!Q))|(P&Q)))"

def __init__():
    c = Core(input_phrase)
    print(c.check_syntax())


if __name__ == "__main__":
    __init__()
