class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 # buy day

        maxProfit = 0 # base case: make no transactions

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # found a cheaper or equal price, so we buy on this day instead
        return maxProfit