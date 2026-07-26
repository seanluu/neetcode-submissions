class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # a substring is a contiguous seq of chars within a string, so consecutive

        dupe = set() # no dupe chars -> hashset

        res = 0 # return an integer
        
        l, r = 0, len(s) - 1 # first and last index

        # we know to use sliding window here, because we want to find the max length
        # before we have a constraint like repeating chars
        # using sliding window will help us restrict

        for r in range(len(s)): # iterate til we get to last index
            while s[r] in dupe: # while rightmost element is in our set
            # that means that we have a duplicate, so remove the leftmost char
                dupe.remove(s[l])
                l += 1 # slide window to check the next char in the string
            dupe.add(s[r]) # add rightmost element since we know it isn't a dupe
            res = max(res, r - l + 1) # return longest substring without repeating chars
            # r - l + 1 is just the length of the word, +1 since we need to be inclusive
        return res
