class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len(edges)
        # adj = [[] for _ in range(n+1)]

        # def dfs(node, parent): 
        #     # dfs returns true if we need this node to see another node, 
        #     # else returns false bc we don't need this node to see any new nodes
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     for v in edges[node]:
        #         if not dfs(v):
        #             return False

        # for u, v in edges:
        #     if not dfs(i):
        #         ret = edges[i]
            
        #     if dfs()
        # return []

        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [ 1 for i in range(n + 1)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return node

        def union(n1, n2):
            parent_1, parent_2 = find(n1), find(n2)
            if parent_1 == parent_2: return False

            rank_1, rank_2 = rank[parent_1], rank[parent_2]
            if rank_1 >= rank_2:
                parent[parent_2] = parent_1
                rank_1 += rank_2
            else:
                parent[parent_1] = parent_2
                rank_2 += rank_1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
