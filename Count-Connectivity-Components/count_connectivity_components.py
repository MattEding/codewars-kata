from collections import Counter, namedtuple

CELL_W, CELL_H = 4, 3

Point = namedtuple('Point', 'x, y')

class Cell:
    """Analyzes a cell by finding connection locations."""

    def __init__(self, point, cell):
        self.point = point
        self.cell = cell

        rows = tuple(cell.split('\n'))
        cols = tuple(zip(*rows))
        sides = (rows[0], cols[-1], rows[-1], cols[0])
        N, E, S, W = tuple(' ' in s for s in sides)
        self._compass = {(0, -1): N, (1, 0): E, (0, 1): S, (-1, 0): W}

    @property
    def neighbors(self):
        """Returns the point location of connected neighbors."""

        neighbors = set()
        for (x, y), direction in self._compass.items():
            if direction:
                neighbors.add(Point(self.point.x + x, self.point.y + y))
        return neighbors


def components(grid):
    """Returns a sorted list of (size, count) for connected cells in a 2d grid."""

    visited = set()
    def visit_connections(x, y, connection):
        """Returns a set of connected cells if they have not yet been visited."""

        cell = cells[x][y]
        if cell.point in visited:
            return None

        visited.add(cell.point)
        for point in (cell.neighbors - visited):
            visit_connections(point.x, point.y, connection)

        connection.add(cell)
        return connection

    #: Get width and height dimensions
    rows = [s for s in grid.split('\n')]
    grid_w = len(rows[0]) - 1
    grid_h = len(rows) - 1
    range_w = range(0, grid_w, CELL_W - 1)
    range_h = range(0, grid_h, CELL_H - 1)

    #: Split grid into individual cells
    cells = [[] for _ in range_w]
    for x, w in enumerate(range_w):
        for y, h in enumerate(range_h):
            point = Point(x, y)
            cell_w = slice(w, w + CELL_W)
            cell_h = slice(h, h + CELL_H)
            cell = '\n'.join(r[cell_w] for r in rows[cell_h])
            cells[x].append(Cell(point, cell))

    #: Record all connections in the grid
    connections = list()
    for x in range(x + 1):
        for y in range(y + 1):
            conn = visit_connections(x, y, set())
            connections.append(conn)

    counter = Counter(len(c) for c in connections if c)
    return sorted(counter.most_common(), key=lambda x: -x[0])
