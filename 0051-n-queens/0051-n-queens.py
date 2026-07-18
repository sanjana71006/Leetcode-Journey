from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        x = [-1] * n      # x[row] = column where queen is placed

        # Check whether queen can be placed at (k, i)
        def place(k, i):
            for j in range(k):
                if x[j] == i or abs(x[j] - i) == abs(j - k):
                    return False
            return True

        # Backtracking function
        def n_queens(k):
            if k == n:
                board = []
                for row in range(n):
                    s = ['.'] * n
                    s[x[row]] = 'Q'
                    board.append("".join(s))
                ans.append(board)
                return

            for i in range(n):
                if place(k, i):
                    x[k] = i
                    n_queens(k + 1)
                    x[k] = -1      # Backtrack

        n_queens(0)
        return ans