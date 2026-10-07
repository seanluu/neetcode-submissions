class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # amount gets solved multiple times in recursion, so
        # we can store the result the first time and reuse it
        # instead of recomputing it everytime

        # hashmap for storing results for already computed amts 
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9 # very large number

            # try every coin
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin)) # track the minimum

            memo[amount] = res
            return res
    
        minCoins = dfs(amount)
        # if final ans is still very large, then we return -1
        return -1 if minCoins >= 1e9 else minCoins