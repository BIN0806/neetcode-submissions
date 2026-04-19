class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        edge = defaultdict(list)
        for u, v in edges:
            edge[u].append(v)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            
            print("haven't seen:", i)
            visited.add(i)
            for node in edge[i]:
                if not dfs(i):
                    print("seen alr:", node)
                    return False

            return True

        count = 0
        for i in range(n):
            if dfs(i):
                count += 1
        return count