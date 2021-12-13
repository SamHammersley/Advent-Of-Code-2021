import input_util
import copy

input = input_util.read_input_lines("../input/day_12_input", str)
sample = input_util.read_input_lines("../input/day_12_sample", str)

def create_graph(input):
  edges = {}

  def add_edge(n1, n2):
    connections = edges.get(n1, set())
    connections.add(n2)
    edges[n1] = connections

  for line in input:
    a,b = line.split('-')
    add_edge(a, b)
    add_edge(b, a)

  return edges

def find_paths(start, graph, visited):
  if start == 'end':
    return 1

  if start == start.lower():
    visited.add(start)

  path_count = 0
  for node in [n for n in graph.get(start, []) if n not in visited]:
    visited_copy = copy.copy(visited)
    path_count += find_paths(node, graph, visited_copy)

  return path_count

def find_paths_revisit(start, graph, visited, revisitable, current_path):
  current_path.append(start)
  if start == 'end':
    return { tuple(current_path) }

  if start == start.lower():
    visited[start] = visited.get(start, 0) + 1

  paths = set()
  for node in graph.get(start, []):
    if node in visited and (node != revisitable or visited[node] > 1):
      continue
    visited_copy = copy.copy(visited)
    current_path_copy = copy.copy(current_path)
    paths.update(find_paths_revisit(node, graph, visited_copy, revisitable, current_path_copy))

  return paths

def part2(graph):
  paths = set()
  for node in [n for n in graph if n == n.lower() and n not in ('start','end')]:
    paths.update(find_paths_revisit('start', graph, {'start': 1}, node, []))
  return paths

input_graph = create_graph(input)
sample_graph = create_graph(sample)
print("part 1: " + str(find_paths('start', input_graph, {'start'})))
print("part 2: " + str(len(part2(input_graph))))
