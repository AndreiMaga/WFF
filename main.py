from core import Core
from node import Node
input_phrase = "(P&!Q)"


def __init__():
    c = Core(input_phrase)
    print(c.evaluate())


if __name__ == "__main__":
    __init__()
