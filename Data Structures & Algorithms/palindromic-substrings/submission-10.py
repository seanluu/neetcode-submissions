class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # palindrome = string that reads the same forward and backward

        n = len(s)

        res = 0

        # let dp[i][j] be true 
        dp = [[False] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res