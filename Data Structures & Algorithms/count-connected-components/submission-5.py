class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # from collections import defaultdict
        # edge = defaultdict(list)
        # for u, v in edges:
        #     edge[u].append(v)
        #     edge[v].append(u)

        # visited = set()
        # def dfs(i):
        #     if i in visited:
        #         return False
            
        #     visited.add(i)
        #     for node in edge[i]:
        #         dfs(node)

        #     return True

        # count = 0
        # for i in range(n):
        #     if dfs(i):
        #         count += 1

        # return count

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)] 

        def find(n1):
            res = n1
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return count
            if rank[parent1] > parent[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else: 
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return 1

        count = n
        for u, v in edges:
           count -= union(u, v)
        return count 
