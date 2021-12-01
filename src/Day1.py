import input_util

def part1(input):
  total = 0
  for x in range(1, len(input)):
    if (input[x] > input[x-1]):
      total += 1
  return total
   
def part2(input):
  total = 0
  previous_window_sum = input[0] + input[1] + input[2]
  for x in range(3, len(input)):
    window_sum = input[x] + input[x-1] + input[x-2]
    if (window_sum > previous_window_sum):
      total += 1
    previous_window_sum = window_sum
  return total

input = input_util.read_input_lines("../input/day_1_input", int)

print("part 1: " + str(part1(input)))
print("part 2: " + str(part2(input)))
