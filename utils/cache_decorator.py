def cache(func):
    cache_store = {}

    def wrapper(*args):
        if args in cache_store:
            return True, cache_store[args]
        result = func(*args)
        cache_store[args] = result
        return False, result

    return wrapper
