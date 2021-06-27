"""Function with recursion restrict count of call. Max count of call == 997
   Function with loop don't have restrict in call"""


def FactorialRecursion(numb: int) -> int:
    """Function calculate factorial numb. Max numb == 998"""
    if numb == 0 or numb == 1:
        return 1
    return FactorialRecursion(numb - 1) * numb


def FactorialLoop(numb: int) -> int:
    """Function calculate factorial numb"""
    factorial = 1
    while numb > 1:
        factorial *= numb
        numb -= 1
    return factorial


print(FactorialLoop(1000))
print(FactorialLoop(997))
