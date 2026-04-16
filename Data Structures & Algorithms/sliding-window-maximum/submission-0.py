class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        n, result = len(nums), []
        queue = deque()
        l, r = 0, 0 
        while r < n:
            while queue and nums[r] > nums[queue[-1]]:
               queue.pop()

            if queue and queue[0] < l:
                queue.popleft() 

            queue.append(r)
            
            if r + 1 >= k:
                result.append(nums[queue[0]])
                l += 1
            r += 1
        return result
