import input_util

def part1(input):
  depth = 0
  pos = 0
  for x in input:
    operation = x[0]
    operand = int(x[1])
    if (operation == "forward"):
      pos += operand
    elif (operation == "down"):
      depth += operand
    elif (operation == "up"):
      depth -= operand

  return depth * pos

def part2(input):
  depth = 0
  pos = 0
  aim = 0
  for x in input:
    operation = x[0]
    operand = int(x[1])
    if (operation == "forward"):
      pos += operand
      depth += aim * operand
    elif (operation == "down"):
      aim += operand
    elif (operation == "up"):
      aim -= operand

  return depth * pos

def parse(instruction):
  return instruction.split(" ")

input = input_util.read_input_lines("../input/day_2_input", parse)
print(part1(input))
print(part2(input))
