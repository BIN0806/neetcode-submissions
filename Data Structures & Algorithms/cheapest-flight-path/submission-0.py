class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        shortest_distance = [float('inf')] * n # the shortest distance from src to all nodes
        stops_taken_to_reach = [float('inf')] * n # # of stops taken to get to node s.t. <= k
        adj_list = collections.defaultdict(list)

        for s, d, cost in flights: adj_list[s].append((d, cost))
        
        shortest_distance[src] = 0 # base case
        stops_taken_to_reach[src] = -1
        min_heap = [(0, src, -1)] # 0 cost to get to src node with -1 stops
        while min_heap:
            cost, node, stops = min_heap.pop()
            if node == dst: return cost # based on prioirty queue implementaiton?
            if stops == k or shortest_distance[node] < cost: continue
            for nei, w in adj_list[node]:
                nextCost = cost + w
                nextStop = stops + 1
                shortest_distance[node] = cost 
                stops_taken_to_reach[node] = stops
                if shortest_distance[nei] > nextCost:
                    shortest_distance[nei] = nextCost
                    heapq.heappush(min_heap, (nextCost, nei, nextStop))
        return -1
