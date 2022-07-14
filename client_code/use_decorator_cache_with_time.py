import time

from utils.cache_decorator_with_time import cache_with_time

# Set max timer for stare result function in cache.
max_timer_cache = 2


@cache_with_time(max_timer_cache)
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(1, 1, 1)) == (False, 2)
assert (function(1, 1, 1)) == (True, 2)
time.sleep(max_timer_cache + 1)
assert (function(1, 1, 1)) == (False, 2)
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 15 + "END" + "=" * 15)
