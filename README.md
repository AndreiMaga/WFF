# WFF

A tool for checking syntax and creating truth tables for well-formated formulas.

## Usage

```py main.py -i <input> -<actions>```

```<input>``` should be a in the strict type of writing (for each operation, there needs to be a pair of parentheses ).

List of available actions

p - Will parse the input (this will run by default with any other action).  
s - Will check the syntax.  
e - Will evaluate all the possible interpretations. See [second example](#second-example).  
c - In conjunction with ```e``` will run only 1 interpretation passed as an argument with a dictionary. See [first example](#first-example).  
t - Will print the tree. See [third example](#third-example).  
r - Will print the reconstructed tree (as a formula).  

## Example

### First example

```py main.py -i "(((P&R)|Q)@S)" -e -c {\"P\":\"True\",\"R\":\"True\",\"Q\":\"True\",\"S\":\"False\"}```

```txt
+------+------+------+-------+-------+-----------+---------------+
|  P   |  R   |  Q   |   S   | (P&R) | ((P&R)|Q) | (((P&R)|Q)@S) |
+------+------+------+-------+-------+-----------+---------------+
| True | True | True | False |  True |    True   |     False     |
+------+------+------+-------+-------+-----------+---------------+
```

### Second example

```py main.py -i "((P&R)|Q)" -e```

```txt
+-------+-------+-------+-------+-----------+
|   P   |   R   |   Q   | (P&R) | ((P&R)|Q) |
+-------+-------+-------+-------+-----------+
|  True |  True |  True |  True |    True   |
|  True |  True | False |  True |    True   |
|  True | False |  True | False |    True   |
|  True | False | False | False |   False   |
| False |  True |  True | False |    True   |
| False |  True | False | False |   False   |
| False | False |  True | False |    True   |
| False | False | False | False |   False   |
+-------+-------+-------+-------+-----------+
```

### Third example

```py main.py -i "((P&R)|Q)" -t```

```txt
  ┌Q
 |┤
  │ ┌P
  └&┤
    └R
```
