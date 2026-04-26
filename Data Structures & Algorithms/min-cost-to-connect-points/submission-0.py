class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        sorted_edges = []
        for (x1, y1) in points:
            for (x2, y2) in points:
                if (x1, y1) == (x2, y2):
                    continue
                distance = abs(x2-x1) + abs(y2-y1)
                sorted_edges.append( (distance, ((x1, y1), (x2, y2))) )

        sorted_edges.sort()
        print(sorted_edges)
        graph = collections.defaultdict(int) # nodes (x1, y1) : min_cost_to be connected in this MST
        for edge in sorted_edges:
            distance = edge[0]
            p1 = edge[1][0]
            p2 = edge[1][1]
            graph[p1] = min(graph[p1], distance)
            graph[p2] = min(graph[p1], distance)

        print(graph.values())
        return sum(graph.values())