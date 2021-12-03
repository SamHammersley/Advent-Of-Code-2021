import input_util
import copy

def get_ones_freq(input):
  output_len = len(input[0])
  ones = [0] * output_len

  for input_string in input:
    for i in range(0, len(input_string)):
      digit = int(input_string[i])
      ones[i] += digit

  return ones

def part1(input):
  ones = get_ones_freq(input)
  gamma = ""
  epsilon = ""

  for freq in ones:
    zeroes = len(input) - freq
    gamma += "0" if zeroes > freq else "1"
    epsilon += "0" if zeroes < freq else "1"

  return int(gamma, 2) * int(epsilon, 2)

def part2(input):
  output_len = len(input[0])
  oxy_generator = copy.deepcopy(input)
  co2_scrubber = copy.deepcopy(input)

  for i in range(0, output_len):
    if (len(oxy_generator) <= 1):
        break
    oxy_ones = 0
    for val in oxy_generator:
      oxy_ones += int(val[i])
    oxy_digit = "1" if oxy_ones >= (len(oxy_generator) - oxy_ones) else "0"
    oxy_generator = list(filter(lambda val: val[i] == oxy_digit, oxy_generator))
 
  for i in range(0, output_len):
    if (len(co2_scrubber) <= 1):
        break
    co2_ones = 0
    for val in co2_scrubber:
      co2_ones += int(val[i])
    co2_digit = "0" if co2_ones >= (len(co2_scrubber) - co2_ones) else "1"
    co2_scrubber = list(filter(lambda val: val[i] == co2_digit, co2_scrubber))

  return int(oxy_generator[0], 2) * int(co2_scrubber[0], 2)

  
input = input_util.read_input_lines("../input/day_3_input", str.strip)
print(part1(input))
print(part2(input))
