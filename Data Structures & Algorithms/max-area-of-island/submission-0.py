class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIR = [(-1,0), (0,-1), (1,0), (0,1)]
        seen = set()
        max_area = 0
        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(x, y):
            if not(0 <= x < n_rows and 0 <= y < n_cols) or (x,y) in seen or grid[x][y] == 0:
                return 0
            
            seen.add((x, y))
            area = 1
            for dx, dy in DIR:
                area += dfs(x+dx,y+dy)
            return area

        for r in range(n_rows):
            for c in range(n_cols):                    
                max_area = max(max_area, dfs(r, c))

        return max_area