class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # length of the longest substring without dupe chars

        # no dupes = use a hashset

        charSet = set()

        # use sliding window since there's only a certain amount of chars
        # where there is a longest substring without repeating chars

        l = 0

        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res