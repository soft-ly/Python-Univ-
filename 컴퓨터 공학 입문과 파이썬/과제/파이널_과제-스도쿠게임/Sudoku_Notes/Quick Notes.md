1. sudoku.board property  ([[Basic Sudoku Game Overview#2. Using `py-sudoku` for Board and Solver]])


2. Sudoku Difficulty [[Basic Sudoku Game Overview#2. Using `py-sudoku` for Board and Solver]]
In the current setup, the difficulty level is set when an instance of the `Board` class is created, and it cannot be changed afterward. If you want to allow the difficulty level to be adjustable after the `Board` object has been created, you'll need to add a method to reset or change the board with a new difficulty level.

Here’s how you can modify the `Board` class to include a method for adjusting the difficulty:

### Modified `Board` Class

```python
from sudoku import Sudoku

class Board:
    def __init__(self, difficulty='easy'):
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        # Initialize the Sudoku puzzle with the specified difficulty
        self.sudoku = Sudoku(3).difficulty(difficulty)
        # Store the generated board in the self.board attribute
        self.board = self.sudoku.board

    def get_board(self):
        # Return the current state of the board
        return self.board

    def is_valid(self, row, col, num):
        # Check if placing num at (row, col) is valid according to Sudoku rules
        return self.sudoku.is_valid_move(row, col, num)

    def get_solution(self):
        # Solve the Sudoku puzzle and return the solved board
        return self.sudoku.solve().board

    def print_board(self):
        # Print the board to the console for debugging purposes
        for row in self.board:
            print(row)
```

### Usage Example with Difficulty Adjustment

Now, you can create an instance of `Board` with a specific difficulty and change it later:

```python
# main.py
from board import Board

def main():
    # Create a Sudoku board with 'medium' difficulty
    board = Board(difficulty='medium')
    
    # Print the initial board
    print("Initial Board (Medium Difficulty):")
    board.print_board()
    
    # Adjust difficulty to 'hard'
    board.set_difficulty('hard')
    
    # Print the new board with 'hard' difficulty
    print("\nNew Board (Hard Difficulty):")
    board.print_board()
    
    # Get the solution to the board
    solution = board.get_solution()
    
    # Print the solved board
    print("\nSolved Board:")
    for row in solution:
        print(row)

if __name__ == "__main__":
    main()
```

### Explanation

- **Initialization (`__init__`)**: The `Board` class constructor initializes the board with a given difficulty level.
- **Set Difficulty (`set_difficulty`)**: This method allows you to change the difficulty level of the board at any time. It reinitializes the `Sudoku` object with the new difficulty and updates the board.
- **Usage Example**: The main function demonstrates creating a board, adjusting the difficulty, and printing the board before and after the difficulty adjustment.

This approach gives you the flexibility to change the difficulty level dynamically during the runtime of your application.

