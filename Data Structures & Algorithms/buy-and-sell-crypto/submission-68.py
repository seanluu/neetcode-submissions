class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # choose a single day to buy one neetcoin, choose a diff day
        # in the future to sell it

        # we want to return the max profit that we can achieve, but we can
        # choose to not make any transactions as well (profit is 0)

        l = 0  # buy day

        maxProfit = 0  # base case: make no transactions

        # r = the day we try to sell, checking every day once
        for r in range(len(prices)):
            # selling today makes a profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)  # keep the best profit so far
            else:
                l = r  # found a cheaper (or equal) price, so buy here instead
        return maxProfit

        # time: O(n), one pass through prices
        # space: O(1)