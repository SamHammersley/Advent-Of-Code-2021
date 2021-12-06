import input_util

input = list(input_util.read_input_lines("../input/day_6_input", lambda x: map(int, x.split(",")))[0])

def freq(input):
    return {x: input.count(x) for x in range(0, 9)}

def solution(input, days):
  frequencies = freq(input)
  for day in range(0, days):
    temp = frequencies[0]
    for cycle in range(0, 8):
       frequencies[cycle] = frequencies[cycle + 1]
    frequencies[6] += temp
    frequencies[8] = temp

  return sum(frequencies.values())

print("part 1: " + str(solution(input, 80)))
print("part 2: " + str(solution(input, 256)))
