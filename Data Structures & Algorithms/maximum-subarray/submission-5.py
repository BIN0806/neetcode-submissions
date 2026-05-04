class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # let dp[i][0] be the best val subarray we have seen so far from n to i 
        # let dp[i][1] be the best val seen from n to i where this is the begging
        dp = [[0] * 2 for _ in range(n)] 
        dp[n-1][1] = dp[n-1][0] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])
            dp[i][0] = max(dp[i][1], dp[i+1][0])

        return dp[0][0]
