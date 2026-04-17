class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        pre = defaultdict(list)
        for c, req in prerequisites: 
            pre[c].append(req)

        # [class 0] : [class1 ,class2] means u need to take 1 and 2 before 0
        path, visit = set(), set()
        result = []
        def dfs(node):
            if node in path:
                return False

            if not pre[node]:
                if node not in visit:
                    result.append(node)
                    visit.add(node)
                return True

            path.add(node)
            for req in pre[node]:
                if not dfs(req):
                    return False

            result.append(node)
            visit.add(node)
            pre[node] = []      
            path.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result 