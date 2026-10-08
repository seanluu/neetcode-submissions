class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 # left pointer for us to slide the window later

        dupe = set() # use a hashset, since we want to avoid duplicate characters

        res = 0

        # iterate through each char of the string s
        # r is our right pointer, for increasing the size of the window
        for r in range(len(s)):
            # s[r] is already in the window, so shrink from the left
            # until its earlier copy is gone
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1 # slide window forward to prevent invalid window
            dupe.add(s[r]) # add rightmost element to the hashset
            res = max(res, r - l + 1) # replace with best size window so far
        return res