class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx, resLen = 0, 0 # start index & len of the longest palindrome so far
        # but none have been found so far, so 0 for both

        n = len(s)

        # dp[i][j] is true if s[i..j] is a palindrome
        # start all as False, since nothing is a palindrome until proven
        dp = [[False] * n for i in range(n)]

         # go backward so the inside of each substring is already solved
        # (checking s[i..j] needs dp[i + 1][j - 1], which starts one later at i + 1)
        for i in range(n - 1, -1, -1):
            # j = end of substring, so we try every end from i to the last char
            for j in range(i, n):
                # ends match and either:
                # j - i <= 2 : 3 chars or less, so matching ends is enough
                # dp[i + 1][j - 1] : inside (without the ends) is a palindrome
                # so it covers 4 chars or more
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True # means s[i..j] is a palindrome
                    if resLen < (j - i + 1): # if resLen is less than the new length of the window
                        resIdx = i # save that length
                        resLen = (j - i + 1)

        # slice from start index for resLen chars
        # s[start:stop] includes start but stops right before stop
        return s[resIdx : resIdx + resLen]

        # suppose we have string s = "xyabaz". we have a and a as our ends. 
        # our i is at 2 and our j is at 4 since a and a are at those points 
        # respectively. therefore, when we do j - i <= 2, we get 4 - 2 = 2, 
        # and 2 <= 2 is true. so the substring is 3 characters or fewer, and 
        # since the ends match (s[2] == s[4], a == a), "aba" is a palindrome. 
        # The b in the middle doesn't need checking, because a single character
        # is always a palindrome on its own.