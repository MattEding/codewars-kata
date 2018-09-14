from itertools import count, groupby
from operator import gt, ne

class MemoryOperator:
    """Applies a binary operator to a new value and the last seen value."""

    def __init__(self, operator, seed):
        self.operator = operator
        self.stored = seed

    def __call__(self, value):
        result = self.operator(value, self.stored)
        self.stored = value
        return result


def pick_peaks(numbers):
    """Finds local maxima in an array of numbers. Returns a mapping of values and positions."""

    maxima = dict(pos=[], peaks=[])

    #: Collapse plateaus while preserving positions
    memory_ne = MemoryOperator(ne, None)
    collapsed = ((num, index) for (num, index) in zip(numbers, count()) if memory_ne(num))

    #: Find maxima and their positions
    memory_gt = MemoryOperator(gt, (float('inf'), None))
    for increase, interval in groupby(collapsed, memory_gt):
        if increase:
            peak, pos = max(interval)
            maxima['pos'].append(pos)
            maxima['peaks'].append(peak)

    #: Ignore maxima at the edge
    if numbers and increase:
        maxima['pos'].pop()
        maxima['peaks'].pop()

    return maxima
