import input_util
import copy

input = input_util.read_input_lines("../input/day_11_input", lambda x: list(map(int, x)))
sample = input_util.read_input_lines("../input/day_11_sample", lambda line: list(map(int, line)))

s = list(map(lambda line: list(map(int, line)), ["11111","19991","19191","19991","11111"]))

def calc_flash(input, flashed, row, column):
  if (row,column) in flashed:
    return 0
  input[row][column] += 1
  if input[row][column] <= 9:
    return 0

  flash_count = 1
  flashed.add((row,column))

  for i in range(row - 1, row + 2):
    if (i < 0) or (i > len(input)-1):
      continue
    for j in range(column - 1, column + 2):
      if (j < 0) or (j > len(input[i])-1):
        continue
      if i == row and j == column:
        continue

      flash_count += calc_flash(input, flashed, i, j)

  input[row][column] = 0
  return flash_count

def part1(input, steps):
  input_copy = copy.deepcopy(input)
  flash_count = 0

  for step in range(0, steps):
    flashed = set()
    for i in range(0, len(input_copy)):
      for j in range(0, len(input_copy[i])):
        flash_count += calc_flash(input_copy, flashed, i, j)

  return flash_count
 
def part2(input):
  input_copy = copy.deepcopy(input)
  input_size = len(input) * len(input[0])
  step = 1 

  while True:
    flashed = set()
    step_flash_count = 0
    for i in range(0, len(input_copy)):
      for j in range(0, len(input_copy[i])):
        step_flash_count += calc_flash(input_copy, flashed, i, j)

    if step_flash_count == input_size:
      return step
    step += 1

print(part1(input, 100))
print(part2(input))
