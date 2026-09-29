class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        # no dupe chars -> use a hashset
        dupe = set()

        l = 0 

        # iterate through each letter in the string s
        for r in range(len(s)):
            while s[r] in dupe: # while rightmost element is in the set
                dupe.remove(s[l]) # remove leftmost element since it's a dupe
                l += 1 # slide window forward since it is now invalid
            dupe.add(s[r]) # add rightmost element to the set since we know it's valid
            res = max(res, r - l + 1) # take best size of the window / longest substring without dupe chars
        return res

        # time complexity: O(n)
        # iterate through each letter in the string s

        # space complexity: O(n)
        # possible that we never have repeating chars