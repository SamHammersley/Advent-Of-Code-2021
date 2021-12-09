import input_util
import queue
import copy

input = input_util.read_input_lines("../input/day_9_input", str)
sample = input_util.read_input_lines("../input/day_9_sample", str)

def low_points(input):
  low_points = []

  for i in range(0, len(input)):
    for j in range(0, len(input[i])):
      adjacents = get_adjacents(input, (i,j))
      cell_value = int(input[i][j])

      if cell_value >= min(map(lambda x: int(input[x[0]][x[1]]), adjacents)):
        continue

      low_points.append((i, j))

  return low_points

def part1(input):
  lows = low_points(input)
  return sum(map(lambda point: int(input[point[0]][point[1]]) + 1, lows))

def get_adjacents(input, position):
  adjacents = set()
  i,j = position

  if i > 0:
    adjacents.add((i - 1, j))

  if i < len(input) - 1:
    adjacents.add((i + 1, j))

  if j > 0:
    adjacents.add((i, j - 1))

  if j < len(input[i]) - 1:
    adjacents.add((i, j + 1))

  return adjacents

def scan_basin(input, start):
  basin_size = 0
  visited = set()

  q = queue.Queue()
  q.put(start)

  while not q.empty():
    vertex = q.get()
    if vertex in visited:
      continue

    adjacents = get_adjacents(input, vertex)
    vertex_value = int(input[vertex[0]][vertex[1]])

    if vertex_value < 9:
      basin_size += 1
      for adjacent in [x for x in adjacents if x not in visited]:
        q.put(adjacent)

    visited.add(vertex)
  
  return basin_size

def part2(input):
  lows = low_points(input)
  basin_sizes = []

  for low in lows:
    basin_sizes.append(scan_basin(input, low))

  basin_sizes = sorted(basin_sizes)[:-4:-1]
  product = 1
  for size in basin_sizes: product *= size

  return product

print("input: " + str(part1(input)) + ", sample: " + str(part1(sample)))
print("input: " + str(part2(input)) + ", sample: " + str(part2(sample)))
