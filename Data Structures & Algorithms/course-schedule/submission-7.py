class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)

        visit = set()
        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            return True
        
        for i in range(numCourses):
            if i in visit:
                continue
            if not dfs(i):
                return False
        return True