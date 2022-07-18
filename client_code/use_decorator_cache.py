from utils.cache_decorator import cache


@cache
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(4, 4, 4)) == (False, 2), "False, because Calculate, don't get from cache"
assert (function(4, 4, 4)) == (True, 2), "Get from cache"
assert (function(4, 16, 4)) == (False, 5), "False, because Calculate, don't get from cache"
print("=" * 9 + "Tests completed" + "=" * 9)
print("=" * 33)
