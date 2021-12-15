import input_util
import copy

input = input_util.read_input_lines("../input/day_15_input", lambda line: list(map(int, line)))
sample = input_util.read_input_lines("../input/day_15_sample", lambda line: list(map(int, line)))

def get_neighbouring(pos, max_y, max_x):
  offsets = [-1, 0, 1]
  neighbours = []
  y,x = pos

  for x_offset in [offset for offset in offsets if offset + x <= max_x and offset + x >= 0]:
    for y_offset in [offset for offset in offsets if offset + y <= max_y and offset + y >= 0]:
      if abs(x_offset) != abs(y_offset):
        neighbours.append((y + y_offset, x + x_offset))

  return neighbours

def distance(pos, goal):
  return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_lowest_score_vertex(open, scores):
  min_score = float('inf')
  min_score_vertex = None

  for vertex in open:
    if scores[vertex] < min_score:
      min_score = scores[vertex]
      min_score_vertex = vertex

  return min_score_vertex

def dijkstra(start, goal, input):
  open = { start }
  came_from = { start: None }
  scores = { start: 0 }
  heuristic_scores = { start: distance(start, goal) }

  max_y = len(input) - 1
  max_x = len(input[0]) - 1

  while open:
    current = get_lowest_score_vertex(open, heuristic_scores)

    if current == goal:
      return scores[current]

    open.remove(current)
    for neighbour in get_neighbouring(current, max_y, max_x):
      n_y, n_x = neighbour
      new_score = scores[current] + input[n_y][n_x]

      if new_score < scores.get(neighbour, float('inf')):
        heuristic_scores[neighbour] = new_score + distance(neighbour, goal)
        scores[neighbour] = new_score
        came_from[neighbour] = current
        open.add(neighbour)

def backtrack(current, came_from):
  path = [current]
  while came_from[current] != None:
    prev = came_from[current]
    path.append(prev)
    current = prev
  return path

def scale_value(x_scale, y_scale, value):
  scaled = value + x_scale + y_scale
  return (scaled % 10 + scaled // 10)

def extend_input(input, scale):
  new_input = []
  for j in range(0, scale * len(input)):
    adjusted = []
    for k in range(0, scale):
      adjusted.extend(list(map(lambda x: scale_value(k, j // len(input), x), input[j % len(input)])))

    new_input.append(adjusted)

  return new_input

print("part 1: " + str(dijkstra((0,0), (len(input) - 1, len(input[len(input) - 1]) - 1), input)))
input = extend_input(input, 5)
print("part 2: " + str(dijkstra((0,0), (len(input) - 1, len(input[len(input) - 1]) - 1), input)))
