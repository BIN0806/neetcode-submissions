class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        DIR = [(-1,0), (0,-1), (1,0), (0,1)]
        seen = set()
        INF = 2 ** 31
        def inBounds(r, c): return (0 <= r < row and 0 <= c < col)

        from collections import deque

        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    seen.add((r, c))
        dist = 0          
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist                        

                for dx, dy in DIR:
                    if (r+dx, c+dy) in seen or not inBounds(r+dx, c+dy) or grid[r+dx][c+dy] == -1: 
                        continue
                    queue.append((r+dx, c+dy))
                    seen.add((r+dx, c + dy))
            dist += 1

                