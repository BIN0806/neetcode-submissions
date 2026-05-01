class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_h(nums):
            n = len(nums)
            dp = [0] * (n) # the max amount of money rob by i
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            if n == 1: return nums[0]
            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return max(dp)
            
        return max(rob_h(nums[:-1]), rob_h(nums[1:]))