class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for i in range(n)]
        DIR = [(-1, 1), (1, -1), (1, 1), (-1, -1)]

        seen_cols = set()
        seen_pos_diags = set() # r + c
        seen_neg_diags = set() # r - c

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in seen_cols or (r + c) in seen_pos_diags or (r - c) in seen_neg_diags: continue
                    
                seen_cols.add(c)
                seen_neg_diags.add(r-c)
                seen_pos_diags.add(r+c)
                board[r][c] = "Q"

                backtrack(r + 1)

                seen_cols.remove(c)
                seen_neg_diags.remove(r-c)
                seen_pos_diags.remove(r+c)
                board[r][c] = "."

        backtrack(0)
        return result