class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque() # [2, 4, 5, ..., 1]
        n = len(nums)
        result = []
        for r in range(n):
            # [1, -1]  k =  1
            # r = 0
            # q: [0,]
            # res: [1, ]

            while queue and queue[0] <= r - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
        
            queue.append(r)

            if (r >= k - 1):
                result.append(nums[queue[0]])

            # print(queue)
        return result
