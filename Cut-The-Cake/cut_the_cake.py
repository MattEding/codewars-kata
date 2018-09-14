import numpy as np


RAISIN = 'o'
CAKE = '.'


class StopRecursion(Exception):
    """Signal the end of a recursive process."""


class Cake:
    """Cut a cake into pieces of equal area such that each piece contains exactly one raisin."""

    def __init__(self, cake):
        #: Map characters to integers to facilitate computations
        self.cake = np.array([[int(item == RAISIN) for item in row] for row in cake.split()], dtype='i1')
        self.x = self.cake.shape[0]
        self.y = self.cake.shape[1]
        self._slices = self._get_slices()
        self._pieces = []

    def _get_area(self):
        raisins = self.cake.sum()
        area = self.x * self.y / raisins
        if not area.is_integer():
            raise ValueError('Cannot evenly divide cake into rectangles with integer dimensions')
        return int(area)

    def _get_slices(self):
        factors = factor_pairs_gen(self._get_area())
        slices = [(x, y) for (x, y) in factors if x <= self.x if y <= self.y]
        return slices

    def _partition_cake(self, cake):
        #: Find location of next uncut part of cake
        try:
            (i, *_), (j, *_) = np.where(cake <= 1)
        except ValueError:
            raise StopRecursion

        for x, y in self._slices:
            xs = slice(i, i + x)
            ys = slice(j, j + y)
            if (xs.stop > self.x) or (ys.stop > self.y):
                continue

            #: Each piece contains exactly one raisin
            if cake[xs, ys].sum() != 1:
                continue

            cake_copy = cake.copy()
            self._pieces.append(cake_copy[xs, ys].copy())

            #: Mark piece as cut
            cake_copy[xs, ys] = 2
            self._partition_cake(cake_copy)
            self._pieces.pop()

    def cut(self):
        """Return a list of all pieces of equal area containing one raisin. If not possible, return []."""
        try:
            self._partition_cake(self.cake)
        except StopRecursion:
            pass

        #: Normalize results
        cuts = []
        for piece in self._pieces:
            result_vec = np.vectorize(lambda v: (CAKE, RAISIN)[v])
            result_gen = (''.join(r) for r in result_vec(piece))
            result_str = '\n'.join(result_gen)
            cuts.append(result_str)
        return cuts


def factor_pairs_gen(number):
    """Return a generator that produces all factor pairs whose product is number."""
    factors = [n for n in range(1, number + 1) if number % n == 0]
    extras = (number // f for f in factors)
    return zip(factors, extras)


def cut(cake):
    c = Cake(cake)
    return c.cut()
