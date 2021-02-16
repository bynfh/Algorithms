from datetime import datetime
import time
# Set max timer for stare result function in cache.
max_timer_cache = 2


def Cache_sec(timer):
    cache = {}

    def inner_decorator(func):
        def wrapper(*args):
            if args in cache:
                time_alive_cache = int(datetime.now().second) - cache[args][1]
                if timer > time_alive_cache:
                    return True, cache[args][0]
            result = func(*args)
            cache[args] = [result, int(datetime.now().second)]
            return False, result
        return wrapper
    return inner_decorator


def Cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return True, cache[args]
        result = func(*args)
        cache[args] = result
        return False, result

    return wrapper


@Cache
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(4, 4, 4)) == (False, 2)
assert (function(4, 4, 4)) == (True, 2)
assert (function(4, 16, 4)) == (False, 5)
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 33)


@Cache_sec(max_timer_cache)
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(1, 1, 1)) == (False, 2)
assert (function(1, 1, 1)) == (True, 2)
time.sleep(max_timer_cache + 1)
assert (function(1, 1, 1)) == (False, 2)
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 15 + "END" + "=" * 15)

