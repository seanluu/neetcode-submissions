class Solution:
    def longestPalindrome(self, s: str) -> str:

        # expand around center: every palindrome mirrors around its middle,
        # so try each possible middle and grow outward while the ends match

        res = ""     # longest palindrome found so far
        resLen = 0   # its length

        for i in range(len(s)):

            # odd length palindromes: middle is a single character (like "aba")
            l, r = i, i
            # keep expanding while in bounds and the two ends match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # r - l + 1 is the length of s[l..r]
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]  # + 1 since slicing excludes the end
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length palindromes: middle is between two characters (like "abba")
            # only difference is that r = i + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res