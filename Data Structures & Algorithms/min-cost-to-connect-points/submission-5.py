class Solution:
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #     import heapq

    #     rank = [1 for i in range(len(points))]
    #     parent = [i for i in range(len(points))]

    #     def find(n1):
    #         if parent[n1] != n1:
    #             parent[n1] = find(parent[n1]) # path-compression
    #         return parent[n1]

    #     def union(n1, n2):
    #         p1, p2 = find(n1), find(n2)
    #         r1, r2 = rank[p1], rank[p2]
            
    #         if r1 >= r2: parent[p2] = p1
    #         else: parent[p1] = p2

    #     def is_connected(n1, n2): return find(n1) == find(n2)

    #     sorted_edges = collections.defaultdict(list)
    #     for (x1, y1) in points:
    #         for (x2, y2) in points:
    #             if (x1, y1) == (x2, y2):
    #                 continue
    #             distance = abs(x2-x1) + abs(y2-y1)
    #             heapq.heappush(sorted_edges[(x1, x2)], (distance, ((x1, y1), (x2, y2))) )

    #     # print(sorted_edges)
    #     graph = collections.defaultdict(int) # nodes (x1, y1) : min_cost_to be connected in this MST
    #     for edge in sorted_edges:
    #         distance = edge[0]
    #         p1 = edge[1][0]
    #         p2 = edge[1][1]

    #         # print(distance)
    #         # print(p1, p2)
    #         graph[p1] = min(graph[p1], distance)
    #         graph[p2] = min(graph[p1], distance)

    #     # print(graph.values())
    #     return sum(graph.values())

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)
                adj_list[i].append((distance, j))
                adj_list[j].append((distance, i))

        import heapq
        min_heap = [[0, 0]] # [cost, point]
        visit = set()
        total_cost = 0

        while len(visit) < n:
            cost, node = heapq.heappop(min_heap)

            if node in visit:
                continue

            visit.add(node) 
            total_cost += cost

            for neiCost, nei in adj_list[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, [neiCost, nei])

        return total_cost