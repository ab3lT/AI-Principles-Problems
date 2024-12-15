def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all unique solutions.

    Parameters:
    n (int): The size of the chessboard (n x n) and the number of queens to place.

    Returns:
    list: A list of solutions, where each solution is represented as a list of integers.
          Each integer represents the column index of the queen in the respective row.

    Example:
    >>> solve_n_queens(4)
    [[1, 3, 0, 2], [2, 0, 3, 1]]
    """
    def is_valid(row, col, columns, main_diag, anti_diag):
        return col not in columns and row - col not in main_diag and row + col not in anti_diag

    def backtrack(row, current_solution):
        if row == n:
            solutions.append(current_solution[:])
            return

        for col in range(n):
            if is_valid(row, col, columns, main_diag, anti_diag):
                # Place the queen
                columns.add(col)
                main_diag.add(row - col)
                anti_diag.add(row + col)
                current_solution.append(col)

                # Recurse to the next row
                backtrack(row + 1, current_solution)

                # Backtrack by removing the queen
                columns.remove(col)
                main_diag.remove(row - col)
                anti_diag.remove(row + col)
                current_solution.pop()

    solutions = []
    columns = set()
    main_diag = set()
    anti_diag = set()
    backtrack(0, [])
    return solutions

def print_solutions(solutions):
    """
    Print all solutions in a human-readable chessboard format.

    Parameters:
    solutions (list): List of solutions, where each solution is a list of integers.
    """
    for solution in solutions:
        print("Solution:")
        for row in solution:
            board = ["."] * len(solution)
            board[row] = "Q"
            print(" ".join(board))
        print()

def main():
    """
    Main function to solve the N-Queens problem for a user-specified board size.
    """
    print("Enter the value of N for the N-Queens problem:")
    n = int(input())
    solutions = solve_n_queens(n)

    if solutions:
        print(f"Found {len(solutions)} solutions for N = {n}:")
        print_solutions(solutions)
    else:
        print("No solutions exist for the given N.")

if __name__ == "__main__":
    main()
