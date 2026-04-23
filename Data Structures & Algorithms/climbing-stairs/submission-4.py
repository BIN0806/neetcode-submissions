class Solution:



    def climbStairs(self, n: int) -> int:
        self.dp = {}
        self.dp[0] = 1

        def cs(n):
            if n < 0:
                return 0
            if n in self.dp:
                return self.dp[n]
            self.dp[n] = cs(n-1) + cs(n-2)
            return self.dp[n]

        cs(n)
        return self.dp[n]


    
        # dp = [0] * (n+1) # let dp[i] represent # of ways to get to position i
        # dp[0] = 1
        # 

        # for i in range(len(dp)):
        #     if i + 1 < len(dp):
        #         dp[i+1] += dp[i]
        #     if i + 2 < len(dp):
        #         dp[i+2] += dp[i]
        # return dp[-1]