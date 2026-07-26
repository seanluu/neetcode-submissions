class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # a substring is a contiguous seq of chars within a string, so consecutive

        dupe = set() # no dupe chars -> hashset
        # tracks chars currently in our window -> hashset for O(1) lookup

        res = 0 # return an integer
        
        l = 0 # left pointer, starts at index 0

        # we know to use sliding window here, because we want to find the max length
        # before we have a constraint like repeating chars
        # using sliding window will help us restrict

        # sliding window: r expands the window each step; whenever we hit a duplicate,
        # we shrink from the left until the duplicate is gone, keeping every window valid

        # r is the right pointer, expands one step at a time
        for r in range(len(s)): # iterate til we get to last index
            while s[r] in dupe: # rightmost char is already in the window
            # that means that we have a duplicate, so remove the leftmost char
                dupe.remove(s[l])
                l += 1 # slide window to check the next char in the string
            dupe.add(s[r]) # add rightmost element to our sliding window 
            # since we know it isn't a dupe, [l, r] has no dupes by this point
            res = max(res, r - l + 1) # return longest substring without repeating chars
            # r - l + 1 is just the length of the window, +1 since we need to be inclusive for count
        return res