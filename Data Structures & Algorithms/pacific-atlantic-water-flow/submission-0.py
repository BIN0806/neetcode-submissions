class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        result = []
        DIR = [(-1,0),(0,-1),(1,0),(0,1)]
        seen = set()

        def inBounds(r, c): 
            return 0 <= r < ROWS and 0 <= c < COLS
        pacific_set = set()
        atlantic_set = set()

        def dfs(r, c, visit):
            if (r, c) in visit: return
            visit.add((r, c))
            for dx, dy in DIR: 
                if not inBounds(r+dx, c+dy) or \
                heights[r][c] > heights[r+dx][c+dy] or \
                (r+dx, c+dy) in visit:
                    continue
                dfs(r+dx, c+dy, visit)

        for r in range(ROWS):
            dfs(r, 0, pacific_set)
            dfs(r, COLS-1, atlantic_set)

        for c in range(COLS):
            dfs(0, c, pacific_set)
            dfs(ROWS-1, c, atlantic_set)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    result.append((r, c))

        return result