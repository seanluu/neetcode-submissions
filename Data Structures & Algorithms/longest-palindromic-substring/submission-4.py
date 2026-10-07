class Solution:
    def longestPalindrome(self, s: str) -> str:

        # start index and length of the longest palindrome so far, none found yet
        resIdx, resLen = 0, 0

        n = len(s)

        # dp[i][j] = True if s[i..j] is a palindrome
        # starts all False since nothing is a palindrome until proven
        dp = [[False] * n for _ in range(n)]

        # i = start of the substring, going from the end of s backward
        # (dp[i][j] needs dp[i + 1][j - 1], so row i + 1 has to be filled first)
        for i in range(n - 1, -1, -1):
            # j = end of the substring, trying every end from i to the last char
            for j in range(i, n):
                # the ends match, and either:
                #   j - i <= 2: it's 3 chars or less, so matching ends is enough
                #   dp[i + 1][j - 1]: the inside (without the ends) is a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True  # s[i..j] is a palindrome

                    # j - i + 1 is its length, save it if it's the longest so far
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = (j - i + 1)

        # slice from the start index for resLen characters
        return s[resIdx : resIdx + resLen]