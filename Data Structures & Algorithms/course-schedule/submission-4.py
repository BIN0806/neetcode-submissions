class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 

        edges = defaultdict(list)
        for c, required in prerequisites:
            edges[c].append(required) 

        path = set()
        def dfs(node):
            if node in path:
                return False
            if path == []:
                return True

            path.add(node)
            for req in edges[node]:
                if not dfs(req):
                    return False
            edges[node] = []  
            path.remove(node) 
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
