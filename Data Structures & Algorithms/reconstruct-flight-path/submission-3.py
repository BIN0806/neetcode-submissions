class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for s, e in tickets:
            heapq.heappush(graph[s], e)

        # res = []
        # stack = ["JFK"]
        # while stack:
        #     while graph[stack[-1]]:
        #         next_vertex = heapq.heappop(graph[stack[-1]])
        #         stack.append(next_vertex)
        #     res.append(stack.pop())

        # res.reverse()

        # return res


        res = []
        # post_order dfs
        def visit(vertex):
            while graph[vertex]:
                next_vertex = heapq.heappop(graph[vertex])
                visit(next_vertex)
            res.append(vertex)
        
        visit("JFK")
        res.reverse()
        return res