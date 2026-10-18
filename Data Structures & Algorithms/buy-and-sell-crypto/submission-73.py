class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sliding window

        l = 0

        res = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r

        return res