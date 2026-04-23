class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1) # let dp[i] represent # of ways to get to position i
        dp[0] = 1
        res = 0
        for i in range(len(dp)):
            if i + 1 < len(dp):
                dp[i+1] += dp[i]
            if i + 2 < len(dp):
                dp[i+2] += dp[i]
        return dp[-1]