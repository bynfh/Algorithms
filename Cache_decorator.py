def cache(func):
    cache_store = {}

    def wrapper(*args):
        if args in cache_store:
            return True, cache_store[args]
        result = func(*args)
        cache_store[args] = result
        return False, result

    return wrapper


@cache
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(4, 4, 4)) == (False, 2)
assert (function(4, 4, 4)) == (True, 2)
assert (function(4, 16, 4)) == (False, 5)
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 33)

