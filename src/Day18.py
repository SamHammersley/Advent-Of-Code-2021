import input_util
import ast

input = input_util.read_input_lines("../input/day_18_input", ast.literal_eval)
sample = input_util.read_input_lines("../input/day_18_sample", ast.literal_eval)

left_side = 0
right_side = 1

class SnailfishNumber:
  def __init__(self, value, left, right, parent, side, depth):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent
    self.side = side
    self.depth = depth

def parse(snailfish_num, depth=0, parent=None, side=None):
  left,right = snailfish_num
  result = SnailfishNumber(None, None, None, parent, side, depth)

  if isinstance(left, int):
    result.left = SnailfishNumber(left, None, None, result, left_side, depth+1)
  else:
    result.left = parse(left, depth+1, result, left_side)

  if isinstance(right, int):
    result.right = SnailfishNumber(right, None, None, result, right_side, depth+1)
  else:
    result.right = parse(right, depth+1, result, right_side)

  return result

def add_adjacent(snailfish, value, side):
  adj = snailfish
  while adj.parent and adj.side == side:
    adj = adj.parent
  if adj.parent:
    adj = adj.parent.left if side == left_side else adj.parent.right
    while adj.right if side == left_side else adj.left:
      adj = adj.right if side == left_side else adj.left
    adj.value += value

def apply_explosion(snailfish):
  stack = [snailfish]

  while stack:
    current = stack.pop()

    if current.left and current.right and current.depth >= 4:
      add_adjacent(current, current.left.value, left_side)
      add_adjacent(current, current.right.value, right_side)

      current.value = 0
      current.left = None
      current.right = None
      return True

    if current.left and current.right:
      stack.append(current.right)
      stack.append(current.left)

def apply_split(snailfish):
  stack = [snailfish]

  while stack:
    current = stack.pop()

    if isinstance(current.value, int) and current.value >= 10:
      left, right = current.value // 2, (current.value + 1) // 2
      current.left = SnailfishNumber(left, None, None, current, left_side, current.depth+1)
      current.right = SnailfishNumber(right, None, None, current, right_side, current.depth+1)
      current.value = None
      return True

    if current.left and current.right:
      stack.append(current.right)
      stack.append(current.left)

def reduce(number):
  while apply_explosion(number) or apply_split(number):
    continue

  return number

def calc_magnitude(snailfish_num):
  if isinstance(snailfish_num.value, int):
    return snailfish_num.value

  return 3 * calc_magnitude(snailfish_num.left) + 2 * calc_magnitude(snailfish_num.right)

def add_snailfish_num(op1, op2):
  parent = SnailfishNumber(None, op1, op2, None, None, 0)

  op1.side = left_side
  op2.side = right_side
  op1.parent = parent
  op2.parent = parent

  stack = [parent.right, parent.left]
  while stack:
    current = stack.pop()
    current.depth += 1

    if current.left and current.right:
      stack.append(current.right)
      stack.append(current.left)

  return parent

def part1(input):
  total = parse(input[0])

  for next in map(parse, input[1:]):
    total = reduce(add_snailfish_num(total, next))

  return calc_magnitude(total)

def part2(input):
  max_magnitude = 0

  for i in range(0, len(input)):
    for j in range(0, len(input)):
      if i == j: continue
      magnitude = calc_mag(parse(input[i]), parse(input[j]))
      max_magnitude = max(magnitude, max_magnitude)

  return max_magnitude

def calc_mag(num1, num2):
  sum = add_snailfish_num(num1, num2)
  return calc_magnitude(reduce(sum))

print(part1(input))
print(part2(input))
