class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(1, len(prices)): # start at day 1 so there's always a yesterday (i - 1) to compare with
            if prices[i] > prices[i - 1]: # if price went up from yesterday
                profit += prices[i] - prices[i - 1] # take that day's gain (buy yesterday, sell today)
        return profit