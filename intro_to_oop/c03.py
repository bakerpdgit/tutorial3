from dataclasses import dataclass
from enum import Enum

# An enum is a group of named constants


class Player(Enum):
  BLANK = " "
  PLAYER1 = "x"
  PLAYER2 = "o"

# Board state record implemented as a dataclass


@dataclass
class BoardState:
  grid: list[list[str]]
  turn: Player

# Board related functions - it is now clear that they all require the
# board state


def print_board(board: BoardState) -> None:
  """
      Function to print the board
  """
  for row in board.grid:
    print("|".join(row))
    print("-" * 5)


def board_is_winner(board: BoardState) -> bool:
  """
      Function to check if the player to play won on a given board
  """
  # row checks
  for row in board.grid:
    if all(cell == board.turn.value for cell in row):
      return True
  # column checks
  for col in range(3):
    if all(board.grid[row][col] == board.turn.value for row in range(3)):
      return True
  # leading diagonal check
  if all(board.grid[i][i] == board.turn.value for i in range(3)):
    return True
  # other diagonal check
  if all(board.grid[i][2 - i] == board.turn.value for i in range(3)):
    return True
  # nothing found
  return False


def is_board_full(board: BoardState) -> bool:
  """
      Returns true if the board is full, false otherwise
  """
  return all(cell != " " for row in board.grid for cell in row)


def board_make_move(board: BoardState, row: int, col: int) -> bool:
  """
      Function to attempt to make a move for the player
      Returns true if the cell specified is empty, false otherwise
  """
  if board.grid[row][col] == " ":
    # enum.value gets the value of the named constant
    board.grid[row][col] = board.turn.value
    return True
  return False


def board_update_turn(board: BoardState) -> None:
  board.turn = Player.PLAYER2 if board.turn == Player.PLAYER1 else Player.PLAYER1


def main():
  """
      Function to run to play a game of tic tac toe
  """
  # initialise board state - this syntax will be explained in the second
  # chapter
  board = BoardState([[" " for _ in range(3)]
                     for _ in range(3)], Player.PLAYER1)

  # game loop
  while True:
    print_board(board)
    row = int(input("Enter row (0-2):"))
    col = int(input("Enter col (0-2):"))
    if not board_make_move(board, row, col):
      print("Invalid move. Try again.")
      continue
    if board_is_winner(board):
      print_board(board)
      print(f"Player {board.turn.value} wins!")
      break
    if is_board_full(board):
      print_board(board)
      print("It's a draw!")
      break
    board_update_turn(board)


main()
