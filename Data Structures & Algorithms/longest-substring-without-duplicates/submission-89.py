class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # use sliding window since we're trying to see how far we can go
        # without repeating characters; we'll stop if we go past our allowed window
        
        l = 0 # left pointer, only slide window forward if it becomes invalid

        dupe = set() # use hashset since this handles dupe chars automatically

        res = 0

        # iterate through each char in the string s (right pointer)
        for r in range(len(s)):
            while s[r] in dupe: # while rightmost element in dupe
                dupe.remove(s[l]) # remove leftmost element since we saw it already
                l += 1 # slide window forward to expand window
            dupe.add(s[r]) # add rightmost element to dupe
            res = max(res, r - l + 1) # return best size of window so far
        return res

        # tc: O(n)
        # iterate through each char in string s once

        # sc: O(n)
        # hashset of every char in string s
                    