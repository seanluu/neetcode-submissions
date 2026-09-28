class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # choose a single day to buy, then a later day to sell it

        l = 0

        maxProfit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
        return maxProfit