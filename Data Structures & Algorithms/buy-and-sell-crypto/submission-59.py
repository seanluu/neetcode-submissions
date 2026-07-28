class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 # return 0 by default since we want to return an integer

        l, r = 0, 1 # buy and sell point, sell always better than buy

        for r in range(len(prices)): # iterate from beginning to end of array
            if prices[l] < prices[r]: # if sell > buy point
                profit = prices[r] - prices[l] # calculate profit
                maxProfit = max(maxProfit, profit) # take highest profit of all days
            else:
                l = r # otherwise, the buy and sell are equal so we continue
            r += 1 # move window regardless since we realize that it isn't a profitable day
        return maxProfit # return final best time to buy and sell stock 

        # time complexity: O(n)
        # iterate through each price exactly once

        # space complexity: O(1)
        # no data structures used here, so automatically constant time O(1)