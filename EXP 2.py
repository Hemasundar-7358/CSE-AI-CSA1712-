Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def is_safe(board, row, col):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
... 
...     return True
... 
... 
... def solve(board, row):
...     if row == 8:
...         return True
... 
...     for col in range(8):
...         if is_safe(board, row, col):
...             board[row] = col
... 
...             if solve(board, row + 1):
...                 return True
... 
...             board[row] = -1
... 
...     return False
... 
... 
... board = [-1] * 8
... 
... if solve(board, 0):
...     print("Solution:")
... 
...     for row in range(8):
...         for col in range(8):
...             if board[row] == col:
...                 print("Q", end=" ")
...             else:
...                 print(".", end=" ")
...         print()
... else:
