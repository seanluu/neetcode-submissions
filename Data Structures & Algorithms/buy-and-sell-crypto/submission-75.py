class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # we know to use sliding window here since we need a buy day and a later
        # sell day where the difference gives us the most profit

        l = 0 # left pointer (buy day), only slide when prices[r] <= prices[l], since that's a cheaper day to buy

        res = 0 # output

        # iterate through each sell price that there is
        # try each day as the sell day
        for r in range(len(prices)):
            if prices[l] < prices[r]: # if sell > buy
                profit = prices[r] - prices[l] # calculate the profit we would get from that day
                res = max(res, profit) # take highest profit day
            else:
                l = r # found a cheaper price, buy here instead

        return res

        # tc: O(n), iterate through each price once
        # sc: O(1), no crazy data structures used