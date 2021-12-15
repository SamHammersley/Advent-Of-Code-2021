import input_util
import heapq
import copy

input = input_util.read_input_lines("../input/day_15_input", lambda line: list(map(int, line)))
sample = input_util.read_input_lines("../input/day_15_sample", lambda line: list(map(int, line)))

def get_neighbouring(pos, max_y, max_x):
  offset_positions = ((-1,0), (0,1), (1,0), (0,-1))
  neighbours = []
  y,x = pos

  for new_y, new_x in [(y + y_off,x + x_off) for y_off,x_off in offset_positions]:
    if new_y >= 0 and new_y <= max_y and new_x >= 0 and new_x <= max_x:
      neighbours.append((new_y, new_x))

  return neighbours

def distance(pos, goal):
  return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def dijkstra(start, goal, input):
  scores = { start: 0 }
  heuristic_scores = { start: distance(start, goal) }
  open = [(heuristic_scores[start], start)]

  max_y = len(input) - 1
  max_x = len(input[0]) - 1

  while open:
    score, current = heapq.heappop(open)

    if current == goal:
      return scores[current]

    for neighbour in get_neighbouring(current, max_y, max_x):
      n_y, n_x = neighbour
      new_score = scores[current] + input[n_y][n_x]

      if new_score < scores.get(neighbour, float('inf')):
        heuristic_scores[neighbour] = new_score + distance(neighbour, goal)
        scores[neighbour] = new_score
        heapq.heappush(open, (heuristic_scores[neighbour], neighbour))

def extend_input(input, scale):

  def scale_value(x_scale, y_scale, value):
    scaled = value + x_scale + y_scale
    return (scaled % 10 + scaled // 10)

  new_input = []
  initial_rows = len(input)
  for row in range(0, scale * initial_rows):
    adjusted = []
    for tile_column in range(0, scale):
      adjusted.extend(list(map(lambda x: scale_value(tile_column, row // initial_rows, x), input[row % initial_rows])))

    new_input.append(adjusted)

  return new_input

print("part 1: " + str(dijkstra((0,0), (len(input) - 1, len(input[len(input) - 1]) - 1), input)))
input = extend_input(input, 5)
print("part 2: " + str(dijkstra((0,0), (len(input) - 1, len(input[len(input) - 1]) - 1), input)))
