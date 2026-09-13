class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0

        res = 0

        dupe = set()

        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1
            dupe.add(s[r])
            res = max(res, r - l + 1)
        return res
            