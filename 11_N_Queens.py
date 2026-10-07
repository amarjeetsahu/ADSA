n = int(input("Enter value of N: "))

board = [-1] * n


def is_safe(row, col):

    for i in range(row):

        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):

    if row == n:
        return True

    for col in range(n):

        if is_safe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False


if solve(0):

    print("Solution:")

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

else:
    print("No solution exists")
