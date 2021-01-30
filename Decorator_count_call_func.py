import random
"""Example how work decorator which count times run functions"""
PrintSeparator = "=" * 40


def CounterCall(func):
    """Decorator output function name and how much function was called"""
    Counters = {func.__name__: 0}

    def Wrapper(*args, **kwargs):
        Counters[func.__name__] += 1
        print(PrintSeparator)
        print(f"Function:{func.__name__} was called {Counters[func.__name__]}")
        return func(*args, *kwargs)
    return Wrapper


@CounterCall
def PrintFirst():
    print("Hello from first function")
    print(f"{PrintSeparator}\n")


@CounterCall
def PrintSecond():
    print("Hello from second function")
    print(f"{PrintSeparator}\n")


Functions = (PrintFirst, PrintSecond)
for _ in range(10):
    Functions[random.randint(0, 1)]()
