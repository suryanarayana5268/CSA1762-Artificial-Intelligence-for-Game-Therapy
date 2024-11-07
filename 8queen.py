def solve(n):
    board = [-1] * n

    def is_safe(r, c):
        return all(board[i] != c and abs(board[i] - c) != r - i for i in range(r))

    def place_queens(r):
        if r == n:
            print_board()
            return True
        for c in range(n):
            if is_safe(r, c):
                board[r] = c
                if place_queens(r + 1):
                    return True
        return False

    def print_board():
        for r in range(n):
            print(" ".join("Q" if board[r] == c else "." for c in range(n)))
        print()

    place_queens(0)


solve(8)