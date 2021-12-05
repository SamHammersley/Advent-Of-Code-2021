import input_util
import math

def parse_input(line):
  return list(map(int, line.split(',')))

input = input_util.read_input_lines("../input/day_7_input", parse_input)[0]

input_min = min(input)
input_max = max(input)

def part1(input):
  min_total_diff = math.inf
  for i in range(input_min, input_max + 1):
    min_total_diff = min(min_total_diff, sum(map(lambda x: abs(x - i), input)))

  return min_total_diff

def sum_natural_num(n):
  return n * (n + 1) // 2

def part2(input):
  min_total_diff = math.inf
  for i in range(input_min, input_max + 1):
    difference = sum(map(lambda x: sum_natural_num(abs(x - i)), input))
    min_total_diff = min(min_total_diff, difference)

  return min_total_diff

print("part 1: " + str(part1(input)))
print("part 2: " + str(part2(input)))
