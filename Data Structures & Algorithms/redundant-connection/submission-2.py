class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if not edges: return []

        # from collections import defaultdict
        # edge = defaultdict(list)
        # for u, v in edges:
        #     edge[u].append(v)

        # visited = set()
        # def dfs(node): 
        #     # dfs returns true if we need this node to see another node, 
        #     # else returns false bc we don't need this node to see any new nodes
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     for v in edges[node]:
        #         if not dfs(v):
        #             return False

        # for i in range(len(edge)):
        #     if not dfs(i):
        #         ret = edges[i]
        # return ret
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [ 1 for i in range(n)]

        def is_connected(n1, n2):
            return find(n1) == find(n2)

        def find(node):
            ptr = parent[node-1]
            while node != ptr:
                node = ptr - 1
                ptr = parent[node-1]
            return ptr

        def union(n1, n2):
            parent_1, parent_2 = find(n1), find(n2)
            rank_1, rank_2 = rank[parent_1], rank[parent_2]
            if parent_1 == parent_2: return False

            if rank_1 >= rank_2:
                parent[parent_2] = parent_1
                rank_1 += rank_2
            else:
                parent[parent_1] = parent_2
                rank_2 += rank_1
            return True

        for u,v in edges:
            if not union(u, v):
                return [u, v]
