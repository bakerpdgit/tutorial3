# constants
BLANK: str = " "
PLAYER1: str = "x"
PLAYER2: str = "o"


def print_board(board: list[list[str]]) -> None:
  """
      Function to print the board
  """
  for row in board:
    print("|".join(row))
    print("-" * 5)


def board_is_winner(board: list[list[str]], turn: str) -> bool:
  """
      Function to check if the player to play won on a given board
  """
  # row checks
  for row in board:
    if all(cell == turn for cell in row):
      return True
  # column checks
  for col in range(3):
    if all(board[row][col] == turn for row in range(3)):
      return True
  # leading diagonal check
  if all(board[i][i] == turn for i in range(3)):
    return True
  # other diagonal check
  if all(board[i][2 - i] == turn for i in range(3)):
    return True
  # nothing found
  return False


def is_board_full(board: list[list[str]]) -> bool:
  """
      Returns true if the board is full, false otherwise
  """
  return all(cell != " " for row in board for cell in row)


def board_make_move(board: list[list[str]],
                    turn: str, row: int, col: int) -> bool:
  """
      Function to attempt to make a move for the player
      Returns true if the cell specified is empty, false otherwise
  """
  if board[row][col] == " ":
    board[row][col] = turn
    return True
  return False


def main():
  """
      Function to run to play a game of tic tac toe
  """
  # initialise board and player turn
  board: list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]
  turn = PLAYER1

  # game loop
  while True:
    print_board(board)
    row = int(input("Enter row (0-2):"))
    col = int(input("Enter col (0-2):"))
    if not board_make_move(board, turn, row, col):
      print("Invalid move. Try again.")
      continue
    if board_is_winner(board, turn):
      print_board(board)
      print(f"Player {turn} wins!")
      break
    if is_board_full(board):
      print_board(board)
      print("It's a draw!")
      break
    turn = PLAYER2 if turn == PLAYER1 else PLAYER1


main()
