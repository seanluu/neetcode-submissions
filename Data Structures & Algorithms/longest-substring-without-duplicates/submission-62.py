class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dupe = set() # use a hashset since we don't want duplicate characters

        l = 0 # left pointer since we need to shrink da window

        res = 0 # since we want to return an integer

        for r in range(len(s)): # iterate from start to end
            while s[r] in dupe: # rightmost element in the window means we have a dupe
                dupe.remove(s[l]) # remove dupe element (leftmost element) from window
                l += 1 # slide window forward since it is now invalid and we move onto a new window
            dupe.add(s[r]) # add non-dupe element to our window since we know it doesn't repeat
            res = max(res, r - l + 1) # return longest substring without repeating chars
            # r - l + 1 is the length of the window
        return res # return longest

        # time complexity: O(n * m)
        # n is the length of the string and  
        # m is the total number of unique characters in the string

        # space complexity: O(m)
        # we used a hashset, so worst case scenario we return all chars