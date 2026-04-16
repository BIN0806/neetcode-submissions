class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 
        seen = set()

        edges = defaultdict(list)
        for c, required in prerequisites:
            edges[c].append(required) 

        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for req in edges[node]:
                if not dfs(req):
                    return False
                    
            return True
            
        for i in range(numCourses):
            return dfs(i)
        return True
