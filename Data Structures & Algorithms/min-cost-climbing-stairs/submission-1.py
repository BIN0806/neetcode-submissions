class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1) # let dp[i] = min cost to get to position i
                                # transitions = either take the i+1 or i+2 which you pay the cost
        dp[0] = 0
        dp[1] = 0
        for i in range(n):
            # basically decide if taking this route is the min way to do so.
            # at each i we can take either i + 1 or i + 2 for the
            # price of cost[i]
            if i + 1 <= n:
                dp[i+1] = min(dp[i+1], cost[i] + dp[i])
            if i + 2 <= n:   
                dp[i+2] = min(dp[i+2], cost[i] + dp[i])

        print(dp)
        return dp[n]

