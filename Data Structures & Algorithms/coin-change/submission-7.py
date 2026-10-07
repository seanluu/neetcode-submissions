class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Input: coins = [1,5,10], amount = 12
        # Output: 3

        # we choose 10 + 1 + 1, since that is the fewest number of coins
        # that we need to make up the exact target amount
        
        # bottom-up dp

        # build answers from smaller amts to larger ones

        # if we know the minimum coins to make a - coin, then we
        # can make a using 1 extra coin

        # dp where dp[a] = minimum coins needed to make amount a
        dp = [amount + 1] * (amount + 1) # all other values as a large number (amount + 1)
        dp[0] = 0 # since 0 coins to make amount 0

        # for every amt a from 1 to amount
        for a in range(1, amount + 1):
            # for every coin
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # if dp[amount] is still large, we return -1
        # otherwise, we'll return dp[amount]
        return dp[amount] if dp[amount] != amount + 1 else -1