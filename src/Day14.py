import input_util
import copy

def associate(input_lines):
  template = input_lines[0]
  input_lines = list(map(lambda x: x.split(' -> '), input_lines[2:]))
  return (template, {association[0]: association[1] for association in input_lines})

input = associate(input_util.read_input_lines("../input/day_14_input", str))
sample = associate(input_util.read_input_lines("../input/day_14_sample", str))

def construct_table():
  table = []
  for i in range(0, 26):
    row = []
    for j in range(0, 26):
      row.append(0)
    table.append(row)
  return table

def do_step(table, associations):
  new_table = construct_table()

  for i in range(0, len(new_table)):
    new_table_row = []
    for j in range(0, len(new_table)):
      pair = chr(i + 65) + chr(j + 65)
      number_of_pairs = table[i][j]

      if pair in associations:
        association = ord(associations[pair]) - 65
        new_table[i][association] += number_of_pairs
        new_table[association][j] += number_of_pairs

  return new_table

def do_insertions(template, associations, steps):
  table = construct_table()

  for i in range(0, len(template) - 1):
    row = ord(template[i]) - 65
    column = ord(template[i+1]) - 65
    table[row][column] += 1

  for _ in range(0, steps):
    table = do_step(table, associations)

  last_char = ord(template[-1]) - 65
  table[last_char][0] += 1

  max_freq = 0
  min_freq = float('inf')
  for i in range(0, len(table)):
    row_sum = sum(table[i])
    max_freq = max(max_freq, row_sum)
    if row_sum > 0:
      min_freq = min(min_freq, row_sum)

  return max_freq - min_freq

print(do_insertions(*sample, 10))
print(do_insertions(*input, 40))
