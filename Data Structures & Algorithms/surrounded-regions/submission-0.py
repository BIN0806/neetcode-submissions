class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        seen = set()
        ROWS, COLS = len(board), len(board[0])

        def inBounds(r, c): return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c):
            print(r, c)
            if not (inBounds(r, c)) or \
               board[r][c] != "O" or \
               (r, c) in seen: \
               return
            print("past:", r, c)

            seen.add((r, c))
            board[r][c] = "#"
            for dx, dy in DIR:
                dfs(r+dx, c+dy)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)           
        
        for r in range(ROWS):
            for c in range(COLS):   
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"