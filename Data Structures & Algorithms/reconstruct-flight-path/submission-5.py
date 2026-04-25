class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        flights = collections.defaultdict(list)
        for start, stop in tickets:
            flights[start].append(stop)
        
        res = ["JFK"]
        def backtrack(airport):
            if len(res) == len(tickets) + 1:
                return True
            
            for i, next_airport in enumerate(flights[airport]):
                res.append(next_airport)
                flights[airport].pop(i)

                if backtrack(next_airport):
                    return True

                res.pop()
                flights[airport].insert(i, next_airport)
            return False

        backtrack("JFK")
        return res

        # graph = collections.defaultdict(list)
        # for s, e in tickets:
        #     heapq.heappush(graph[s], e)

        # res = []
        # # post_order dfs
        # def dfs(vertex):
        #     while graph[vertex]:
        #         next_vertex = heapq.heappop(graph[vertex])
        #         dfs(next_vertex)
        #     res.append(vertex)
        
        # dfs("JFK")
        # res.reverse()
        # return res


        # res = []
        # stack = ["JFK"]
        # while stack:
        #     while graph[stack[-1]]:
        #         next_vertex = heapq.heappop(graph[stack[-1]])
        #         stack.append(next_vertex)
        #     res.append(stack.pop())

        # res.reverse()

        # return res
