def fail(type:str="", args:tuple=()):
        """Fail method
        
        Keyword Arguments:
            type {str} -- The type of the erro (default: {""})
            args {tuple} -- Arguments for printing (default: {()})
        """
        if type == "ret":
            print("Parser: ❌")
            print(
                "The input string is not a WFF. As the brakets are not ok at position", args[0])

        if type == "parse":
            print("Parser: ❌")
            print("Error at parsing the string. Error occured at", args[0])

        if type == "syntax":
            print("Syntax: ❌")
            print("Failed at", args[0].to_string())

        if type == "404":
            print("Atom: ❌")
            print("The atom "+ args[0] +" was not found in the config.")
        if type == "val":
            print("Symbols: ❌")
            for i in args[0]:
                if i not in args[1]:
                    print("The symbol",i, " is not supported.")
        if type == "config":
            print("Unrecognised value",args[1],"at", args[0])
        raise SystemExit(1)