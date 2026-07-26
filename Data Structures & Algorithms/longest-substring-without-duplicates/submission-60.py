class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # a substring is a contiguous seq of chars within a string, so consecutive

        dupe = set() # tracks chars currently in our window -> hashset for O(1) lookup

        res = 0 # tracks the max window length seen so far

        l = 0 # left pointer, starts at index 0

        # sliding window: r expands the window each step; whenever we hit a duplicate,
        # we shrink from the left until the duplicate is gone, keeping every window valid

        for r in range(len(s)): # r is the right pointer, expands one step at a time
            while s[r] in dupe: # rightmost char is already in the window
                dupe.remove(s[l]) # shrink from the left...
                l += 1            # ...until the duplicate is removed
            dupe.add(s[r]) # now safe to add — window [l, r] has no dupes
            res = max(res, r - l + 1) # r - l + 1 = window length (+1 for inclusive count)
        return res