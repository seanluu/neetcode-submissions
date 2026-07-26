class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        l, r = 0, 1 # sell always better than buy

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit