class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # palindrome = string that reads the same forward and backward
        # end chars match: s[i] == s[j]
        # inside substring s[i + 1 .. j - 1] is also a palindrome
        # (or length is <= 2, which is always a palindrome if ends match)

        # instead of re-checking chars every time, we reuse previous results
        # store whether a substring is palindromic in a DP table
        # build sols for longer substrings using shorter ones

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