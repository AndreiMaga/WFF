def fail(type:str="", args:tuple=()):
        """Fail method
        
        Keyword Arguments:
            type {str} -- The type of the erro (default: {""})
            args {tuple} -- Arguments for printing (default: {()})
        """
        if type == "ret":
            print(
                "The input string is not a WFF. As the brakets are not ok at position", args[0])

        if type == "parse":
            print("Error at parsing the string. Error occured at", args[0])

        if type == "syntax":
            print("Failed at", args[0].to_string())

        if type == "404":
            print("The atom "+ args[0] +" was not found in the config.")
        raise SystemExit(1)