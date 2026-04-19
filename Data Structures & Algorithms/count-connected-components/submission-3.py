class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        edge = defaultdict(list)
        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)

        visited = set()
        def dfs(i):
            if i in visited:
                return True
            
            visited.add(i)
            for node in edge[i]:
                dfs(node)

            return True

        count = 0
        for i in range(n):
            if dfs(i):
                count += 1

        return count