class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # choose a single day to buy, choose a diff day in the future to sell

        # means that there is a specific answer in the window that is best

        # therefore, we should use sliding window here to find the max profit

        l = 0

        maxProfit = 0

        # iterate through each price, end at the rightmost element
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # difference
                maxProfit = max(maxProfit, profit) 
            else:
                l = r # otherwise
        return maxProfit