class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        edge = defaultdict(list)
        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)
        # print(edge)
        visit = set()
        def dfs(node):
            if node in visit:
                # print("skip", node)
                return False
            # print(node)
            visit.add(node)
            for v in edge[node]:
                # print("traversing", v)
                edge[v].remove(node)
                if not dfs(v):
                    return False
            # visit.remove(node)
            return True

        return dfs(0)