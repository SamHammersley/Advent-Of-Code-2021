def read_input_lines(input_file_name, map_func):
  with open(input_file_name, 'r') as input_file:
    input = input_file.readlines()
    return list(map(map_func, input))
