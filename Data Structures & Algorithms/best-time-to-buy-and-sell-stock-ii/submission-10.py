class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for i in range(1, len(prices)): # start at day 1 so we can always compare to yesterday (i - 1) 
            if prices[i] > prices[i - 1]: # if today's price > yesterday's price
                profit += prices[i] - prices[i - 1] # adds up every gain
        return profit