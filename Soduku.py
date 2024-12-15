def is_valid(board, row, col, num):
    """
    Check if placing num at board[row][col] is valid.

    Parameters:
    board (list): A 2D list representing the Sudoku board.
    row (int): Row index.
    col (int): Column index.
    num (int): The number to place in the cell.

    Returns:
    bool: True if placing the number is valid, False otherwise.
    """
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in (board[i][col] for i in range(9)):
        return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.

    Parameters:
    board (list): A 2D list representing the Sudoku board. Empty cells are represented by 0.

    Returns:
    bool: True if the Sudoku puzzle is solved, False if unsolvable.
    """
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers 1-9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively attempt to solve
                            return True
                        board[row][col] = 0  # Backtrack if solving fails

                return False  # No valid number found for this cell
    return True  # Puzzle solved
def display_board(board):
    """
    Display the Sudoku board in a readable format.

    Parameters:
    board (list): A 2D list representing the Sudoku board.
    """
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))

def main():
    """
    Main function to solve a Sudoku puzzle and display the solution.

    Example:
    Input:
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    Output:
    Solved Sudoku board.
    """
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Initial Sudoku board:")
    display_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku board:")
        display_board(board)
    else:
        print("The Sudoku puzzle is unsolvable.")

if __name__ == "__main__":
    main()
