import bisect


class SortedSet(set):
    """A sorted set that can be indexed."""
    def __init__(self, iterable):
        super().__init__(iterable)
        self._list = sorted(self)

    def __getitem__(self, index):
        return self._list[index]

    def add(self, item):
        if item in self:
            return
        super().add(item)
        bisect.insort(self._list, item)

    def update(self, iterable):
        for item in iterable:
            self.add(item)


def dbl_linear(n):
    """Return the element u(n) of the ordered sequence u such that:
    1. The number u(0) = 1 is the first one in u.
    2. For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    3. There are no other numbers in u.
    """
    values = SortedSet([1])

    for i in range(n):
        x = values[i]
        y = 2 * x + 1
        z = x + y
        values.update([y, z])

    return values[n]
