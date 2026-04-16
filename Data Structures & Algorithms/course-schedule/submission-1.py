class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 
        seen = set()

        edges = defaultdict(list)
        for c, required in prerequisites:
            edges[required].append(c) 

        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for req in edges[node]:
                if not dfs(req):
                    return False

            return True

        return dfs(0)
