class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)

        path = set()
        seen = set()
        result = []

        def dfs(node):
            if node in path:
                return False

            if node in seen:
                return True

            path.add(node)
            seen.add(node)

            for nei in adj_list[node]:
                if not dfs(nei):
                    print(nei)
                    return False

            path.remove(node)
            result.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result 