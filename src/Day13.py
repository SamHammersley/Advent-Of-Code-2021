import input_util
import copy
import sys

def parse_input(input_string):
  input_string = input_string.strip()
  parts = input_string.split("\n\n")
  dots = list(map(lambda x: tuple(map(int, x.split(","))), parts[0].split("\n")))
  fold_lines = parts[1].split("\n")
  return (fold_lines, dots)

input = input_util.read_input_string("../input/day_13_input", parse_input)
sample = input_util.read_input_string("../input/day_13_sample", parse_input)

def fold_on(dots, fold):
  output = set()
  axis,intercept = fold.split("=")
  intercept = int(intercept)
  axis = axis[-1]

  for dot in dots:
    x,y = dot

    if (axis == 'x' and x > intercept):
      x = intercept - (x - intercept)

    elif (axis == 'y' and y > intercept):
      y = intercept - (y - intercept)

    output.add((x, y))

  return output

def fold(dots, fold_lines):
  max_x = 0
  max_y = 0
  min_x = float('inf')

  for fold in fold_lines:
    dots = fold_on(dots, fold)

  for dot in dots:
    min_x = min(min_x, dot[0])
    max_x = max(max_x, dot[0])
    max_y = max(max_y, dot[1])

  return (min_x, max_x, max_y, dots)

def print_output(min_x, max_x, max_y, output, output_stream):
  output_table = []

  print(f'min x: {min_x}, max x: {max_x}, max y: {max_y}')

  for j in range(0, max_y + 1):
    row = []
    for i in range(0, max_x + 1):
      row.append('.')
    output_table.append(row)

  for dot in [i for i in output if i[0] <= max_x and i[1] >= 0]:
    output_table[dot[1]][dot[0]] = '#'

  for row in output_table:
    output_stream.write("".join(row) + "\n")

input_fold_lines, input_dots = input
sample_fold_lines, sample_dots = sample

print(len(fold_on(input_dots, input_fold_lines[0])))

folded_sample = fold(sample_dots, sample_fold_lines)
print_output(*folded_sample, sys.stdout)

folded = fold(input_dots, input_fold_lines)
print_output(*folded, sys.stdout)
