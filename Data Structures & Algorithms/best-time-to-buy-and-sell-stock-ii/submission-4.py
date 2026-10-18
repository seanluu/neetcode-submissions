class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # greedy rule: buy at every low, sell at the next high
        # repeat for every price rise, skip drops
        
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit