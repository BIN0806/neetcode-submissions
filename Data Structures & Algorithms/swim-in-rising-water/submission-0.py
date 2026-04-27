class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # parent = [i for i in range(n * n + 1)]
        # rank = [1 for i in range(n * n + 1)]

        # def find(node):
        #     if node != parent[node]:
        #         parent[node] = find(parent[node])
        #     return parent[node]
        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     r1, r2 = rank[p1], rank[p2]

        #     if r1 >= r2:
        #         parent[p2] = parent[p1]
        #         rank[p1] += rank[p2]
        #     else:
        #         parent[p1] = parent[p2]
        #         rank[p2] += rank[p1]

        # def is_connected(n1, n2): return find(n1) == find(n2)

        # positions = sorted((grid[r][c], r, c) for r in range(n) for c in range(n))
        # DIR =  [(0,1), (1,0), (-1,0), (0,-1)]

        # for t, r, c in positions:
        #     for dr, dc in DIR:
        #         nr, nc = r + dr, c + dc
        #         if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
        #             union(r * n + c, nr * n + nc)   

        #     if is_connected(0, n*n -1):
        #         return t

        import heapq
        min_heap = [(grid[0][0], 0, 0)]
        visit = set()
        n = len(grid)
        # for r in range(n):
        #     for c in range(n):
        DIR =  [(0,1), (1,0), (-1,0), (0,-1)]

        visit.add((0, 0))
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == n-1 and c == n-1:
                return t

            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(min_heap, (max(grid[nr][nc], t), nr, nc))
