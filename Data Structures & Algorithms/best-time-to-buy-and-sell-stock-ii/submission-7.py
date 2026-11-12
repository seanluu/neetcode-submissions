class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # return the max profit we achieve
        profit = 0

        for i in range(1, len(prices)): # start at 1 so we can compare each day with the day before
            if prices[i] > prices[i - 1]: # if the price went up from yesterday
                profit += prices[i] - prices[i - 1] # take that day's gain (buy yesterday, sell today)
        return profit