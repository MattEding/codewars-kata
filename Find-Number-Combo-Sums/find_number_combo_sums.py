from collections import Counter


def combos(number):
    """Return a list of lists of positive integers that sum to number."""

    results = set()
    previous = Counter()

    def dfs(num, prev):
        if not num:
            tpl = tuple(prev.elements())
            results.add(tpl)

        for n in range(1, num + 1):
            prev[n] += 1
            dfs(num - n, prev)
            prev[n] -= 1

    dfs(number, previous)
    return [list(r) for r in results]
