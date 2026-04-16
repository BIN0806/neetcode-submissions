class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 

        edges = defaultdict(list)
        for c, required in prerequisites:
            edges[c].append(required) 

        def dfs(node, path):
            if node in path:
                return False

            path.add(node)
            for req in edges[node]:
                if not dfs(req, path):
                    return False
                    
            return True
            
        for i in range(numCourses):
            path = set()
            if not dfs(i, path):
                return False
        return True
