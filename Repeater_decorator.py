count_repeat = 2


def Repeater(count):
    def inner_decorator(func):
        def wrapper(*args):
            result = []
            for _ in range(count):
                result.append(func(*args))
            print(result)
            return result
        return wrapper
    return inner_decorator


@Repeater(count_repeat)
def function(x, y, z):
    return (x + y) / z


print("=" * 5 + "Start tests first block" + "=" * 5)
assert (function(1, 1, 1)) == ([2] * count_repeat)
assert (function(4, 4, 2)) == ([4] * count_repeat)
print("=" * 9 + "Tests completed" + "=" * 9)
