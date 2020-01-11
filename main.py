from manager import Manager
from json import loads
import argparse

parser = argparse.ArgumentParser("Well-formatted formulas checker")

parser.add_argument('-i', metavar='i', required=True,
                    type=str,   help="The input.")
parser.add_argument('-p', dest='p', action="store_true", required=False,
                    help="Use it only if you want to parse, every command will also parse the input.")
parser.add_argument('-s', dest='s', action="store_true",
                    required=False, help="Will check the syntax of the input.")
parser.add_argument('-e', dest='e', action="store_true", required=False,
                    help="Will evaluate the input with the provided config, if it's missing will evaluate all interpretations.")
parser.add_argument('-c', metavar='c', required=False, type=loads,
                    help="The config for one evaluation. The format is {\\\"P\\\": \\\"False\\\", \\\"Q\\\": \\\"True\\\"}.")
parser.add_argument('-t', dest='t', action="store_true",
                    required=False,   help="Will print the tree.")
parser.add_argument('-r', dest='r', action="store_true", required=False,
                    help="Will print the reconstructed version of the input.")
parser.add_argument('-o', dest='o', required=False, type=str,
                    help="Will output to this file if specified, but it will also print to console. It works only for evaluation.")
parser.add_argument('-k', dest='k',action="store_true", required=False,
                    help="Will evaluate if the formula is Valid/Satisfiable/Not Satisfiable")
args = parser.parse_args()


def __init__():

    args.i = args.i.strip()
    # i
    m = Manager(args.i)

    # p
    if args.p == True:
        m.parse()

    # s
    if args.s == True:
        m.validate()
        m.check_syntax()

    if args. k == True:
        if args.e == True:
            m.sat_not_sat(True)
        else:
            m.sat_not_sat()
    elif args.e == True:
        # c
        if args.c != None:
            m.update_evaluator(args.c)
            m.evaluate(True)
        else:
            m.evaluate_all_interpretations()

    # t
    if args.t == True:
        m.print_tree()

    # r
    if args.r == True:
        print(m.reconstruct())

    if args.o != None:
        with open(args.o, "w", encoding="utf-8") as f:
            f.write(m.output)

if __name__ == "__main__":
    __init__()
