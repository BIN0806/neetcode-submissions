class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        # dp = [0] * (n+1) # let dp[i] represent # of ways to get to position i
        # dp[0] = 1
        # 

        # for i in range(len(dp)):
        #     if i + 1 < len(dp):
        #         dp[i+1] += dp[i]
        #     if i + 2 < len(dp):
        #         dp[i+2] += dp[i]
        # return dp[-1]