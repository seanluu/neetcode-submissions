class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set() # hashset since we don't want dupe chars 

        l = 0 # left pointer

        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res