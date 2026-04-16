class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [(-1,0), (0,-1), (1,0), (0,1)]
        seen = set()
        rows, cols = len(grid), len(grid[0])

        count = 0 
        def dfs(x, y):
            seen.add((x, y))
            for dx, dy in DIR:
                if 0 <= x+dx < rows and 0 <= y+dy < cols and (x+dx, y+dy) not in seen and grid[x+dx][y+dy] == "1":
                    dfs(x+dx, y+dy)
            return 1

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen or grid[r][c] == "0":
                    continue 
                count += dfs(r, c)

        return count