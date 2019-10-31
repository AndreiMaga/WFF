# WFF


## Example

### First example

```py main.py -i "(((P&R)|Q)@S)" -e -c {\"P\":\"True\",\"R\":\"True\",\"Q\":\"True\",\"S\":\"False\"}```

should output

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
