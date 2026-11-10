class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # use sliding window since we're trying to see how far we can go
        # without repeating characters; shrink from the left when we hit a repeat

        l = 0 # left pointer, only slide forward when the window has a repeat

        dupe = set() # chars currently in the window, O(1) lookup to detect a repeat

        res = 0

        # iterate through each char in the string s (right pointer)
        for r in range(len(s)):
            while s[r] in dupe: # s[r] is a repeat, window is invalid
                dupe.remove(s[l]) # drop chars from the left until s[r] is gone
                l += 1 # shrink window from the left
            dupe.add(s[r]) # s[r] is now safe to add
            res = max(res, r - l + 1) # track longest valid window so far
        return res

        # tc: O(n)
        # each char is added once and removed at most once

        # sc: O(n)
        # set holds the current window's chars, at most n (or the charset size)