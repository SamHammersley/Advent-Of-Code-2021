import input_util

def parse_line(line_string):
  points = line_string.split(" -> ")
  return list(map(lambda point: tuple(map(int, point.split(","))), points))

input_file = "../input/day_5_input"
sample_file = "../input/day_5_sample"
input = input_util.read_input_lines(input_file, parse_line)

def occupy_pos(occupied, overlaps, pos):
  if (pos in occupied):
    overlaps.add(pos)
  else:
    occupied.add(pos)

def min_max(a, b):
  return (a, b) if a <= b else (b, a)

def solution(lines, include_diagonals):
  occupied = set()
  overlaps = set()

  for line in lines:
    x1,y1 = line[0]
    x2,y2 = line[1]
    min_x, max_x = min_max(x1, x2)
    min_y, max_y = min_max(y1, y2)

    if (y1 == y2): # horizontal line
      for x in range(min_x, max_x + 1):
        occupy_pos(occupied, overlaps, (x, y1))
  
    elif (x1 == x2): # vertical line
      for y in range(min_y, max_y + 1):
        occupy_pos(occupied, overlaps, (x1, y))

    elif (include_diagonals): # diagonal line
      gradient = (y1 - y2) // (x1 - x2)
      y_start = (min_y, max_y + 1) if gradient == 1 else (max_y, min_y - 1)
      positions = set(zip(range(min_x, max_x + 1), range(y_start[0], y_start[1], gradient)))
    
      for pos in positions:
        occupy_pos(occupied, overlaps, pos)

  return len(overlaps)

print("part 1: " + str(solution(input, False)))
print("part 2: " + str(solution(input, True)))
