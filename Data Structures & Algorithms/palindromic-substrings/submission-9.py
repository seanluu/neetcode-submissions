class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # Input: s = "abc"
        # Output: 3

        # since technically "a", "b", "c" are their own palindromes respectively
        # even if it isn't with the other characters in the string s 

        n = len(s)

        res = 0 

        dp = [[False] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res