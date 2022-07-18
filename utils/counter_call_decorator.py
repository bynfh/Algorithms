def counter_call(func):
    """Decorator output how much function was called."""
    counters_store = {func.__name__: 0}

    def wrapper(*args, **kwargs):
        counters_store[func.__name__] += 1
        return func(*args, *kwargs)

    return wrapper
