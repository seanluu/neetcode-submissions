class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # find length of the longest substring without dupe chars

        # no dupe chars -> use a hashset since that prevents dupes

        dupe = set()

        # since we want to find the longest we can go without dupes,
        # therefore we should use sliding window

        l = 0

        res = 0

        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1
            dupe.add(s[r])
            res = max(res, r - l + 1)
        return res