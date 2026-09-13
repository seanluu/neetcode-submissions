class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # choose a single day to buy, choose a diff day in the future to sell
        # but it must return the most profit

        # sounds like sliding window since we want the max result from the window of prices
        # that we're looking at
        
        maxProfit = 0

        l = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
        return maxProfit

        