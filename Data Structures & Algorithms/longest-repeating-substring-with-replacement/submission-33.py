class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        # use sliding window since we want to find the longest repeating char replacement
        # and there is a max amount that we want to grab before stopping

        l = 0 

        maxf = 0 # need to determine max frequency of a single char before we can proceed

        count = {} # use a hashmap to track the frequency for each character

        # iterate through each char in the string s
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # keep track of frequency for rightmost element
            # if there is a char we haven't seen before, we say the frequency is 0 
            maxf = max(maxf, count[s[r]]) # replace old max freq with new max freq 
            # based on rightmost element of window
            while (r - l + 1 - maxf > k): # while length of window - maxf is greater than the integer k
            # amount of replacements we have to make
                count[s[l]] -= 1 # decrement the leftmost elements that are repeating
                l += 1 # slide window forward to shrink the window
            res = max(r - l + 1, res) # replace res with length of the window
        return res # return longest repeating character replacement

        # time complexity: O(n)
        # iterate through each char in the string s at least once

        # space complexity: O(1)
        # we used a hashmap, so we should have O(1) runtime
        # we are also only considering uppercase English characters
        # therefore it is rlly just O(26) but it reduces down to O(1)

