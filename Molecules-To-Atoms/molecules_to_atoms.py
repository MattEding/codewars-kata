import re
from collections import defaultdict


def parse_molecule(formula):
    """Return a list of ("atom", amount) of each atom given in a chemical
    formula represented by a string."""
    
    atom_pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
    right_pattern = re.compile(r'[\]})](\d+)')
    left_pattern = re.compile(r'[\[{(](\w+)$')

    right = re.search(right_pattern, formula)
    while right:
        r = right.start()
        left = re.search(left_pattern, formula[:r])
        l = left.start() + 1

        sub_formula = formula[l:r]
        atom_matches = re.findall(atom_pattern, sub_formula)
        multiplier = int(right.group(1))

        parts = []
        for atom, amount in atom_matches:
            amount = int(amount if amount else 1) * multiplier
            parts.append(atom + str(amount))

        old = left.group() + right.group()
        new = ''.join(parts)
        formula = formula.replace(old, new)
        right = re.search(right_pattern, formula)

    elements = defaultdict(int)
    atom_matches = re.findall(atom_pattern, formula)
    for atom, amount in atom_matches:
        elements[atom] += int(amount if amount else 1)

    return elements
