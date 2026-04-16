class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        time, fresh = 0, 0
        row, col = len(grid), len(grid[0])

        def inBounds(r, c): return 0 <= r < row and 0 <= c < col

        from collections import deque
        q = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1: 
                    fresh += 1

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in DIR:
                    if not inBounds(r+dx, c+dy) or grid[r+dx][c+dy] != 1:
                        continue 

                    grid[r+dx][c+dy] = 2
                    q.append((r+dx, c+dy))
                    fresh -= 1
            time += 1

        print(fresh, time)
        return -1 if fresh else time 

