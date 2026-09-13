class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # choose a single day to buy, choose a diff day in the future to sell
        # but it must return the most profit

        # sounds like sliding window since we want the max result from the window of prices
        # that we're looking at
        
        maxProfit = 0 # base price since we can choose not to make any transactions, so profit is 0

        l = 0 # left pointer for sliding window is only changed whenever we want to shrink the window

        # iterate through the rightmost price of prices
        for r in range(len(prices)):
            if prices[r] > prices[l]: # if sell > buy
                profit = prices[r] - prices[l] # then we have profit
                maxProfit = max(maxProfit, profit) # take highest profit that 
                # we have so far amongst all profit so far
            else:
                l = r # found a new lower price, so update our "buy" pointer to here
        return maxProfit # return highest profit so far

        # time complexity: O(n)
        # iterate through each price at least once

        # space complexity: O(1)
        # no crazy data structures used so far

        