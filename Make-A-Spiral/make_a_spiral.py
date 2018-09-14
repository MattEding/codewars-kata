from itertools import cycle
import numpy as np


def spiralize(size):
    """Return an NxN clockwise spiral starting from the top left corner made
    of 0's and 1's, where N is given by size. 1's represent the spiral and
    0's represent the space between.
    """

    if size <= 0:
        return []

    arr = np.zeros((size, size), dtype=int)
    arr[0] = 1

    i, j = 0, -1
    length = size + 1

    for rot, cyc in enumerate(cycle(range(4)), start=1):
        arr = np.rot90(arr)

        if length <= 1:
            break

        if cyc % 2 == 0:
            length -= 2

        if cyc == 0:
            j += 2
        elif cyc == 3:
            i += 2

        arr[i, j: j + length] = 1

    arr = np.rot90(arr, k=-rot)
    return arr.tolist()
