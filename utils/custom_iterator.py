class CustomIterator:
    """Let's say for some purposes we needed to bypass the list
    numb_bypass_iterable times, so that each time the value is increased by the
    number by iteration count."""

    def __init__(self, iterable, numb_bypass_iterable: int = 1):
        self.iterable = iterable
        self.index_iterable: int = 0
        self.numb_bypass_iterable = numb_bypass_iterable
        self.multiply_numbs: list = list(range(numb_bypass_iterable, 0, -1))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_iterable < len(self.iterable):
            result = self.iterable[self.index_iterable] * self.multiply_numbs[self.numb_bypass_iterable - 1]
            self.index_iterable += 1
            return result

        elif self.numb_bypass_iterable > 1:
            self.numb_bypass_iterable -= 1
            self.index_iterable = 0
            return self.__next__()
        else:
            raise StopIteration()
