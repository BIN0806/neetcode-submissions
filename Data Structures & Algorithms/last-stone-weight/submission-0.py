from _heapq import heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq 
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1 : 
            y, x = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if x < y: heapq.heappush(stones, -1 * (y-x))

        return -1*heapq.heappop(stones) if stones else 0