class Solution:
    def countSubstrings(self, s: str) -> int:

        # 2d dp: dp[i][j] = True if s[i..j] is a palindrome
        # a substring is a palindrome if its ends match and its inside is a palindrome
        # recurrence: dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        n, res = len(s), 0  # res counts every palindromic substring

        dp = [[False] * n for _ in range(n)]

        # i goes from the bottom up since dp[i][j] needs dp[i + 1][j - 1],
        # which is in the row below, so that row has to be filled first
        for i in range(n - 1, -1, -1):
            # j starts at i since a substring can't end before it starts
            for j in range(i, n):
                # ends must match, and either:
                #   j - i <= 2  -> length 1, 2, or 3, so the inside is empty or one char
                #                  (always a palindrome, no need to check dp)
                #   dp[i + 1][j - 1] -> the inside is already a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1  # s[i..j] is a palindrome, count it

        return res  # O(n^2) time, O(n^2) space