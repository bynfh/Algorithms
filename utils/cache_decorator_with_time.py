from datetime import datetime


def cache_with_time(max_time_alive: int = 2):
    """Декоратор для кэширования с временем жизни кэша."""
    cache = {}

    def inner_decorator(func):
        def wrapper(*args):
            if args in cache:
                time_alive_cache = int(datetime.now().second) - cache[args][1]
                if max_time_alive > time_alive_cache:
                    return True, cache[args][0]
            result = func(*args)
            cache[args] = [result, int(datetime.now().second)]
            return False, result
        return wrapper
    return inner_decorator

