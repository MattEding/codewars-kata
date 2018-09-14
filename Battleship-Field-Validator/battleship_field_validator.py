from collections import defaultdict, namedtuple
from itertools import product


Point = namedtuple('Point', 'x y')

#: ship length vs ship count
valid_ships = {4: 1, 3: 2, 2: 3, 1: 4}


def get_neighbors(field, point):
    """For each neighbor to a point, yield the neighbor's position and whether it is occupied."""
    for (i, j) in product(range(-1, 2), repeat=2):
        m = point.x + i
        n = point.y + j
        if m < 0 or n < 0:
            continue
        try:
            neighbor = field[m][n]
        except IndexError:
            continue
        yield Point(m, n), bool(neighbor)


def link_occupied(field, point, visited=None):
    """Return a set of occupied points that are connected by neighboring each other."""
    occupied = field[point.x][point.y]
    if not occupied:
        return set()

    if visited is None:
        visited = {point}

    for pt, bln in get_neighbors(field, point):
        cond1 = not bln
        cond2 = pt in visited
        if cond1 or cond2:
            continue
        visited.add(pt)
        link_occupied(field, pt, visited)

    return visited


def validate_link(link):
    """Return True if a link is contained in a straight line; False otherwise."""
    if not link:
        return True

    xs = {pt.x for pt in link}
    ys = {pt.y for pt in link}
    cond1 = len(xs) == 1
    cond2 = len(ys) == 1
    return cond1 or cond2


def validateBattlefield(field):
    """Return True if the field is a valid battleship field; False otherwise."""
    m, n = len(field), len(field[0])
    visited = set()
    lengths = defaultdict(int)

    for i, j in product(range(m), range(n)):
        pt = Point(i, j)
        if pt in visited:
            continue

        link = link_occupied(field, pt)
        visited.update(link)
        valid = validate_link(link)

        if valid:
            length = len(link)
            lengths[length] += 1
        else:
            return False

    try:
        del lengths[0]
    except KeyError:
        pass

    return lengths == valid_ships
