class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        l = 0

        dupe = set() # hashset since we don't want dupe chars

        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1
            dupe.add(s[r]) 
            res = max(res, r - l + 1)
        return res