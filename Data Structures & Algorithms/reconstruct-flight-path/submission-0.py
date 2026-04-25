class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        adj_list = defaultdict(list)

        tickets.sort()
        for u, v in tickets:
            adj_list[u].append(v)

        path = ["JFK"] 
        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True
            if node not in adj_list:
                return False

            temp = list(adj_list[node])
            for i, neigh in enumerate(temp):
                adj_list[node].pop(i)
                path.append(neigh)

                if dfs(neigh):
                    return True

                adj_list[node].insert(i, neigh)
                path.pop()

            return False

        dfs("JFK")
        return path