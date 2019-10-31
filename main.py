from core import Core
from json import loads
import argparse

parser = argparse.ArgumentParser("Well-formatted formulas checker")

parser.add_argument('-i', metavar='i',required=True, type=str, help="The input.")
parser.add_argument('-p', metavar='p',required=False, type=bool, help="Use it only if you want to parse, every command will also parse the input.")
parser.add_argument('-s', metavar='s',required=False, type=bool, help="Will check the syntax of the input.")
parser.add_argument('-e', metavar='e',required=False, type=bool, help="Will evaluate the input with the provided config, if it's missing will evaluate all interpretations.")
parser.add_argument('-c', metavar='c',required=False, type=loads, help="The config for one evaluation. The format is {\\\"P\\\": \\\"False\\\", \\\"Q\\\": \\\"True\\\"}.")
parser.add_argument('-v',metavar='v',required=False, type=bool, help="Will print the tree.")
parser.add_argument('-r', metavar='r',required=False, type=bool, help="Will print the reconstructed version of the input.")

args = parser.parse_args()

def __init__():

    args.i = args.i.strip()
    # i
    c = Core(args.i)

    # p
    if args.p == True:
        c.parse()

    # s
    if args.s == True:
        c.validate()
        c.check_syntax()

    # e
    if args.e == True:
        # c
        if args.c != None:
            c.update_evaluator(args.c)
            c.evaluate(p=True)
        else:
            c.evaluate_all_interpretations()

    # v
    if args.v == True:
        c.print_tree()

    if args.r == True:
        print(c.reconstruct())
    

if __name__ == "__main__":
    __init__()
