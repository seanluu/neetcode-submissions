class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # palindrome = string that reads the same forward and backward

        n = len(s)

        res = 0

        # let dp[i][j] be true if substring s[i .. j] is a palindrome
        dp = [[False] * n for i in range(n)]

        # traverse the string from bottom to top for i
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # for every (i, j) where j >= i
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True # mark as True 
                    res += 1
        return res