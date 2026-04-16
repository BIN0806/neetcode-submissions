class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        DIR = [(-1,0), (0,-1), (1,0), (0,1)]
        seen = set()
        INF = 2 ** 31
        def inBounds(r, c): return 0 <= r < row and 0 <= c < col

        def dfs(r, c):
            if (r, c) in seen: 
                return
            
            seen.add((r,c))

            for dx, dy in DIR:
                if not inBounds(r+dx, c+dy): 
                    continue
                if grid[r+dx][c+dy] == -1: 
                    continue
                elif grid[r+dx][c+dy] > 0:
                    grid[r+dx][c+dy] =  min(grid[r+dx][c+dy], 1 + grid[r][c])
                    dfs(r+dx, c+dy)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    dfs(r, c)
                