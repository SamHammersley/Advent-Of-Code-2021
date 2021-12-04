import input_util

non_blank = bool

def parse_row(row):
  return list(map(int, filter(non_blank, row.split(' '))))

def parse_board(board):
  return list(map(parse_row, board))

def parse_boards(boards_input):
  return list(map(parse_board, [boards_input[i:i + 5] for i in range(1, len(boards_input), 6)]))

def find_draw(draw, board):
  for row_index in range(0, len(board)):
    for column_index in range(0, len(board[0])):
      if (draw == board[row_index][column_index]):
        return (row_index, column_index)

def scan_horizontal(previous_finds, board, start_pos):
  start_x = start_pos[1]
  while (start_x < len(board[0]) - 1):
    start_x += 1
    if (board[start_pos[0]][start_x] not in previous_finds):
      return False

  start_x = start_pos[1]
  while (start_x > 0):
    start_x -= 1
    if (board[start_pos[0]][start_x] not in previous_finds):
      return False

  return True

def scan_vertical(previous_finds, board, start_pos):
  start_y = start_pos[0]
  while (start_y < len(board) - 1):
    start_y += 1
    if (board[start_y][start_pos[1]] not in previous_finds):
      return False

  start_y = start_pos[0]
  while (start_y > 0):
    start_y -= 1
    if (board[start_y][start_pos[1]] not in previous_finds):
      return False

  return True

def find_wins(draws, boards):
  winning_boards = {}
  board_matches = {}

  for draw in draws:
    for board_index in range(0, len(boards)):
      if (board_index in winning_boards):
        continue

      board = boards[board_index]

      found_pos = find_draw(draw, board)
      if (found_pos is None):
        continue

      previous_finds = board_matches.get(board_index, set())
      previous_finds.add(draw)
      board_matches[board_index] = previous_finds

      if (scan_horizontal(previous_finds, board, found_pos) or scan_vertical(previous_finds, board, found_pos)):
        winning_boards[board_index] = draw * (sum(map(sum, board)) - sum(previous_finds))

  return winning_boards

input_file = "../input/day_4_input"
input = input_util.read_input_lines(input_file, lambda x: x)

draws = list(map(int, input[0].split(",")))
boards_input = parse_boards(input[1:])

winning_board_outputs = find_wins(draws, boards_input)
values = list(winning_board_outputs.values())
print(values[0])
print(values[-1])
