class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque() # [2, 4, 5, ..., 1]
        n = len(nums)
        result = []
        for r in range(n):
            # [1,2,1,0,4,2,6] k = 3

            # queue: [1, ]
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            while queue and nums[queue[0]] < nums[r]:
                queue.popleft()
        
            queue.append(r)

            if (r >= k - 1):
                result.append(nums[queue[0]])

            print(queue)
        return result
