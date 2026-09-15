class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # find length of the longest substring without dupe chars

        # no dupe chars -> use a hashset since that prevents dupes

        dupe = set()

        # since we want to find the longest we can go without dupes,
        # therefore we should use sliding window

        l = 0

        res = 0

        # iterate through each char in the substring
        for r in range(len(s)):
            while s[r] in dupe: # s[r]'s duplicate is somewhere in [l, r-1] — we don't
                dupe.remove(s[l]) # know exactly where, so we remove from the left one
                l += 1  # at a time until we happen to remove that exact char
                # (could take 1 step if it's at l, or more if it's deeper in)
            dupe.add(s[r]) # add the rightmost element to the set since we know it
            # isn't a repeating character
            res = max(res, r - l + 1) # replace prev longest with new longest
            # we use (r - l + 1) since that is the size of the window
            # (+1) to be inclusive
        return res

        # time complexity: O(n)
        # iterate through each char in the substring once

        # space complexity: O(n)
        # worst case scenario we have no repeating characters
        # so all the characters in the substring get used, so it is O(n)