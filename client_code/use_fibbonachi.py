from utils.fibbonachi import fib_recursion_calculate, fib_iteration_calculate

print("=" * 5 + "Start tests first block" + "=" * 5)
assert fib_recursion_calculate(6) == 8
assert fib_iteration_calculate(5) == 8
assert fib_recursion_calculate(7) == 13
assert fib_iteration_calculate(6) == 13
assert fib_recursion_calculate(0) == 1
assert fib_iteration_calculate(0) == 1
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 33)
