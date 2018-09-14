from operator import add, sub, mul, truediv


class Calculator(object):
  """
  Creates a calculator that when given a string of operations and numbers seperated by
  spaces returns the value of that expression using the order of operations provided.
  The order of operations is expected to be a sequence of mappings.
  """

  def __init__(self, order_of_operations=None):
    if order_of_operations is None:
      order_of_operations = [{'*': mul, '/': truediv}, {'+': add, '-': sub}]
    self.order_of_operations = order_of_operations
    self._decomposition = []

  def evaluate(self, expression):
    """Returns a float of the evaluated expression using the given order of operations."""
    self._decompose(expression)
    for tier in self.order_of_operations:
      self._simplify_tier(tier)
    evaluation = self._decomposition.pop()
    return evaluation

  def _decompose(self, expression):
    """Decomposes the expression into a list of numbers and operations."""
    parts = expression.split()
    for i, char in enumerate(parts):
      try:
        parts[i] = float(char)
      except ValueError:
        for tier in self.order_of_operations:
          try:
            parts[i] = tier[char]
          except KeyError:
            continue
          else:
            break
    self._decomposition = parts

  def _simplify_tier(self, tier):
    """Simplifies in place all operations in a given tier from left to right."""
    while True:
      indices = [self._get_index(oper) for oper in tier.values()]
      index = min(indices)
      try:
        self._simplify_binary_operation(index)
      except TypeError:
        break

  def _get_index(self, operation):
    """Returns the index before the provided operation."""
    try:
      index = self._decomposition.index(operation) - 1
    except ValueError:
      index = float('INF')
    return index

  def _simplify_binary_operation(self, index):
    """Simplifies in place a binary operation starting at index."""
    num1, func, num2 = [self._decomposition.pop(index) for _ in range(3)]
    value = func(num1, num2)
    self._decomposition.insert(index, value)
