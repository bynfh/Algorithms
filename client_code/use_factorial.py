"""Function with recursion restrict count of call.

Max count of call == 998 Function with loop don't have restrict in call
"""
from utils.factorials import calculate_fact_by_recursion, calculate_fact_by_loop

print("=" * 5 + "Start tests first block" + "=" * 5)
assert calculate_fact_by_recursion(5) == 120
assert calculate_fact_by_loop(5) == 120
assert calculate_fact_by_recursion(0) == 1
assert calculate_fact_by_loop(0) == 1
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 33)
