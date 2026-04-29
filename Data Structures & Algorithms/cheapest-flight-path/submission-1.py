class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # stops_taken_to_reach = [float('inf')] * n # # of stops taken to get to node s.t. <= k
        # adj_list = collections.defaultdict(list)

        # for s, d, cost in flights: adj_list[s].append((d, cost))
        
        # stops_taken_to_reach[src] = -1
        # min_heap = [(0, src, -1)] # 0 cost to get to src node with -1 stops
        # while min_heap:
        #     cost, node, stops = min_heap.pop()
        #     if node == dst: return cost # based on prioirty queue implementaiton?
        #     if stops == k or shortest_distance[node] < cost: continue
        #     for nei, w in adj_list[node]:
        #         nextCost = cost + w
        #         nextStop = stops + 1
        #         stops_taken_to_reach[node] = stops
        #         heapq.heappush(min_heap, (nextCost, nei, nextStop))
        # return -1

        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            temp = prices.copy() # allows use to dynamically keep a copy of k-1 state
            for src, dst, price in flights:
                if prices[src] != float('inf'):
                    temp[dst] = min(temp[dst], price + prices[src])
            prices = temp

        return -1 if prices[dst] == float('inf') else prices[dst]