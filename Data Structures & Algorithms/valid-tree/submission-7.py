class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        edge = defaultdict(list)
        
        if not n or len(edges) > n-1: return False 

        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)

        visit = set()
        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            for v in edge[node]:
                if v == node:
                    continue
                if not dfs(v):
                    return False

            return True
        
        return dfs(0) and len(visit) == n