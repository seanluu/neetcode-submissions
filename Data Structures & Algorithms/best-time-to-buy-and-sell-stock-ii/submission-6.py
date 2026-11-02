class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        # any multi-day trade adds up to the same total as its day-to-day gains,
        # so collecting every upward move gives the max profit
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:  # price went up since yesterday
                profit += prices[i] - prices[i - 1]  # buy yesterday, sell today
        return profit