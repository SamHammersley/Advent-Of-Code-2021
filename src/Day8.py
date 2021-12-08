import input_util
import collections

input = input_util.read_input_lines("../input/day_8_input", lambda x: x.split(' | '))
sample = input_util.read_input_lines("../input/day_8_sample", lambda x: x.split(' | '))

def part1(input):
  digit_segments = {1:2, 4:4, 7:3, 8:7}
  found_digits = 0

  for line in input:
    output = line[1].split(' ')
    for digit in output:
      for segments in digit_segments.values():
        if (len(digit) == segments):
          found_digits += 1

  return found_digits

def replace_digit(output, to_replace, replacement):
  while to_replace in output:
    index = output.index(to_replace)
    output[index] = replacement
    
def part2(input):
  segments = {0:6, 2:5, 3:5, 5:5, 6:6, 9:6}
  unique_segments = {2:1, 4:4, 3:7, 7:8}
  total = 0

  for line in input:
    output_digits = list(map(set, line[1].split(' ')))
    digit_connections = {}
    digits = line[0].split(' ')

    length_groups = {}
    for segment_count in segments.values():
      length_groups[segment_count] = [set(digit) for digit in digits if len(digit) == segment_count]

    for digit in digits:
      digit_length = len(digit)
      if digit_length in unique_segments.keys():
        digit_num = unique_segments[digit_length]
        digit = set(digit)
        digit_connections[digit_num] = digit
        replace_digit(output_digits, digit, digit_num)

    # find the string for digit 9
    for digit in length_groups[6]:
      four_connections = digit_connections[4]
      if four_connections.issubset(digit):
        digit_connections[9] = digit
        length_groups[6].remove(digit)
        replace_digit(output_digits, set(digit), 9)

    # find the string for digit 3 this must be done before finding 5 and 2.
    for digit in length_groups[5]:
      if digit_connections[1].issubset(digit):
        digit_connections[3] = digit
        length_groups[5].remove(digit)
        replace_digit(output_digits, set(digit), 3)

    # find the strings for digits 5 and 2
    for digit in length_groups[5]:
      if digit_connections[9] == digit.union(digit_connections[1]):
        digit_connections[5] = digit
        replace_digit(output_digits, set(digit), 5)
      else:
        digit_connections[2] = digit
        replace_digit(output_digits, set(digit), 2)

    # find the strings for digits 6 and 0
    for digit in length_groups[6]:
      digit_signals = digit.union(digit_connections[1])

      if digit_connections[8] == digit_signals:
        digit_connections[6] = digit
        replace_digit(output_digits, set(digit), 6)
      else:
        digit_connections[0] = digit
        replace_digit(output_digits, set(digit), 0)

    total += int("".join(map(str, output_digits)))

  return total

print("sample part 2: " + str(part2(sample)))
print("part 2: " + str(part2(input)))
