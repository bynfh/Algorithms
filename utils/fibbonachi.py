from functools import lru_cache


@lru_cache
def fib_recursion_calculate(numb: int) -> int:
    """Function for calculate numb of Fibbonachi recursion method."""
    if numb <= 1:
        return 1
    return fib_recursion_calculate(numb - 1) + fib_recursion_calculate(numb - 2)


@lru_cache
def fib_iteration_calculate(numb: int) -> int:
    """Function for calculate numb of Fibbonachi iteration method."""
    a, b = 0, 1
    for _ in range(numb):
        a, b = b, a + b
    return b
