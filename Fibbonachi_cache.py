"""I can use decorator from module functools,
   but i want to try create my decorator"""
#from functools import lru_cache


def Cache(func):
    """Decorator for which save result function. It is Cache decorator."""
    DictCache = {}

    def Wrapper(*args, **kwargs):
        if args in DictCache:
            return DictCache[args]
        else:
            DictCache[args] = func(*args, **kwargs)
            return DictCache[args]

    return Wrapper


#@lru_cache
@Cache
def FibRecursion(numb):
    """Function for calculate numb of Fibbonachi"""
    if numb < 2:
        return numb
    return FibRecursion(numb - 2) + FibRecursion(numb - 1)


print(FibRecursion(100))