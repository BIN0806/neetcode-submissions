class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n  # most amount of money made at pos i  
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i])
        
        return max(dp)