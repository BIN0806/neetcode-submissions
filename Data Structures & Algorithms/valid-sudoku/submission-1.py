class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        row = defaultdict(set) # row index: seen set()
        col = defaultdict(set) # col index: seen set()
        square = defaultdict(set) # 9 boxes: seen set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                box = (r // 3, c // 3)
                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in square[box]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[box].add(board[r][c])
        return True
        