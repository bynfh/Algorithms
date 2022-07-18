import random

from utils.counter_call_decorator import counter_call

PRINT_SEPARATOR = "=" * 40


@counter_call
def print_first():
    print("Hello from first function")
    print(f"{PRINT_SEPARATOR}\n")


@counter_call
def print_second():
    print("Hello from second function")
    print(f"{PRINT_SEPARATOR}\n")


functions = (print_first, print_second)
for _ in range(10):
    functions[random.randint(0, 1)]()
