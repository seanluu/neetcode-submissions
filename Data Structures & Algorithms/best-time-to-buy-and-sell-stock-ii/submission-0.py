class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Input: prices = [7,1,5,3,6,4]
        # Output: 7

        # buy on day 2 (price = 1)
        # sell on day 3 (price = 5, so profit = 5 - 1 = 4)
        # buy on day 4 (price = 3)
        # sell on day 5 (price = 6, so profit = 6 - 3 = 3)
        # total profit = 4 + 3 = 7 (each buy price is only subtracted once)

        # buy at each low, sell at the next high (ride every upswing)
        # repeat for every rise; skip the drops

        # original is only one trade, meanwhile this is unlimited trades

        profit = 0

        # start at day 2 (i = 1) so we can compare to the day before
        for i in range(1, len(prices)):
            # if today's price is higher than yesterday's, we profit, so add it.
            # otherwise skip it, but keep going since a later rise
            # can still add profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit