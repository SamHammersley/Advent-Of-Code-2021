import input_util

input = input_util.read_input_lines("../input/day_10_input", str)
sample = input_util.read_input_lines("../input/day_10_sample", str)

bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
syntax_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_scores = {'(':1, '[':2, '{':3, '<':4}

def part1(input):
  syntax_error_score = 0

  for line in input:
    stack = []
    for bracket in line:
      if bracket in bracket_pairs:
        opening_bracket = stack.pop()
        if opening_bracket != bracket_pairs[bracket]:
          syntax_error_score += syntax_scores[bracket]
          break
      else:
        stack.append(bracket)

  return syntax_error_score

def part2(input):
  scores = []

  for line in input:
    stack = []
    syntax_error = False
    for bracket in line:
      if bracket in bracket_pairs:
        opening_bracket = stack.pop()
        if opening_bracket != bracket_pairs[bracket]:
          syntax_error = True
          break
      else:
        stack.append(bracket)

    if not syntax_error:
      line_score = 0
      extension = stack[::-1]
      for score in list(map(lambda bracket: autocomplete_scores[bracket], extension)):
        line_score *= 5
        line_score += score

      scores.append(line_score)

  return sorted(scores)[len(scores) // 2]

print(part2(input))
