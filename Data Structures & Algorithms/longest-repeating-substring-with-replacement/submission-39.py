class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # string s consists of only uppercase English chars and an integer k

        # choose up to k chars of the string and replace them with any other uppercase English char

        # after performating at most k replacements, 
        # we return the length of the longest substring which contains only one distinct character

        res = 0 # final ans

        l = 0

        maxf = 0 # keep track of char that happens most often

        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1 - maxf > k):
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
