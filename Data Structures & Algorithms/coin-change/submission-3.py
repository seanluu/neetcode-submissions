class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # amount gets solved multiple times in recursion, so
        # we can store the result the first time and reuse it
        # instead of recomputing it every time

        # hashmap for storing results for already computed amts
        memo = {}

        def dfs(remaining):
            # base case: nothing left to make, so 0 coins
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            res = 1e9  # very large number, means impossible until proven otherwise

            # try every coin that fits
            for coin in coins:
                if remaining - coin >= 0:
                    # use this coin (1) and solve the rest, track the minimum
                    res = min(res, 1 + dfs(remaining - coin))

            memo[remaining] = res
            return res

        minCoins = dfs(amount)
        # if final ans is still very large, no combination works, so return -1
        return -1 if minCoins >= 1e9 else minCoins