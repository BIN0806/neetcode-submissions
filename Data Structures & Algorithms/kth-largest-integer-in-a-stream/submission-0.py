class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k and val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0] 

