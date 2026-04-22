class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict

        edges = defaultdict(list)
        visit = set()
        minheap = [(0, k)] # cost and k and it does matter that weight is first for minHeap 
        time = 0

        for u, v, t in times:
            edges[u].append((v, t)) # map node to (neigh, egde_cost)

        while minheap:
            time_1, node_1 = heapq.heappop(minheap)
            if node_1 in visit:
                continue

            visit.add(node_1)
            time = time_1 # update the time that we are in this node

            for node_2, time_2 in edges[node_1]:
                if node_2 not in visit:
                    heapq.heappush(minheap, (time_1 + time_2, node_2))


        return time if len(visit) == n else -1