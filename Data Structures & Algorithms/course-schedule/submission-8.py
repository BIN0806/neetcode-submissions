class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)

        path = set()
        def dfs(node):
            if node in path:
                return False

            path.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True