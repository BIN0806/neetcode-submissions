class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        points = [[(x ** 2 + y ** 2)**(1/2), (x, y)] for x,y in points]
        results = []
        for _ in range(k):
            results.append(heapq.heappop(points)[1])
        return results