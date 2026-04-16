class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0 
        for r in range(len(prices)):
            if profit < prices[r] - prices[l]:
                profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r

        return profit


        [100, 99, 100, 1, 1, 1]