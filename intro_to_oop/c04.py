from dataclasses import dataclass
from enum import Enum

# An enum is a group of named constants
class Player(Enum):
    BLANK = " "
    PLAYER1 = "x"
    PLAYER2 = "o"

# Board record with methods
@dataclass
class Board:

    grid: list[list[str]]
    turn: Player

    def print(self) -> None:
        """
            Function to print the board
        """
        for row in self.grid:
            print("|".join(row))
            print("-" * 5)

    def is_turn_winner(self) -> bool:
        """
            Function to check if the player to play won on a given board
        """
        # row checks
        for row in self.grid:
            if all(cell == self.turn.value for cell in row):
                return True
        # column checks
        for col in range(3):
            if all(self.grid[row][col] == self.turn.value for row in range(3)):
                return True
        # leading diagonal check
        if all(self.grid[i][i] == self.turn.value for i in range(3)):
            return True
        # other diagonal check
        if all(self.grid[i][2-i] == self.turn.value for i in range(3)):
            return True
        # nothing found
        return False
        
    def is_full(self) -> bool:
        """
            Returns true if the board is full, false otherwise
        """
        return all(cell != " " for row in self.grid for cell in row)

    def make_move(self, row: int, col: int) -> bool:
        """
            Function to attempt to make a move for the player
            Returns true if the cell specified is empty, false otherwise
        """
        if self.grid[row][col] == " ":
            # enum.value gets the value of the named constant
            self.grid[row][col] = self.turn.value
            return True
        return False

    def update_turn(self) -> None:
        self.turn = Player.PLAYER2 if self.turn == Player.PLAYER1 else Player.PLAYER1

def main(): 
    """
        Function to run to play a game of tic tac toe
    """
    # initialise board state - this syntax will be explained in the second chapter
    board = Board([[" " for _ in range(3)] for _ in range(3)], Player.PLAYER1)

    # game loop
    while True:
        board.print()
        row = int(input("Enter row (0-2):"))
        col = int(input("Enter col (0-2):"))
        if not board.make_move(row, col):
            print("Invalid move. Try again.")
            continue
        if board.is_turn_winner():
            board.print()
            print(f"Player {board.turn.value} wins!")
            break
        if board.is_full():
            board.print()
            print("It's a draw!")
            break
        board.update_turn()

main()

