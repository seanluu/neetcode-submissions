class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # string s consists of only uppercase English chars and an int k

        # choose up to k chars of the string

        # at most k replacements, return length of the longest substring which contains
        # only one distinct character

        # Input: s = "XYYX", k = 2
        # Output: 4

        # since k = 2, we want to replace 2 chars from the string with the letter X or Y
        # with the opposite character, so replace X with Ys, or we can replace the Ys with X

        # Input: s = "AAABABB", k = 1
        # Output: 5

        # we replace the B here with an A, so now the longest substring with only one distinct
        # character should be 5, since we have "AAAAABB"

        # we probably want to use sliding window here because there's a certain number of
        # chars that we want to replace before we can get the length 

        # only move left pointer of sliding window if we want to shrink the window 
        # when the window becomes invalid (i.e, we violated a constraint that we care about)
        # only move right pointer of sliding window if we want to grow the window and move 
        # forward; it never shrinks

        # we can use a hashmap here since we should map the frequency of chars?

        count = {} # use a hashmap to map char : freq

        maxf = 0 # the character that occurs the most in the entire string

        res = 0 # output should be a 0

        l = 0 # left pointer for sliding window

        for r in range(len(s)): # iterate from beginning of the string to the last index
            count[s[r]] = 1 + count.get(s[r], 0) # rightmost char 
            maxf = max(maxf, count[s[r]]) # replace max frequency with the char that occurs the most (count(s[r]))
            # if applicable ^^^
            while (r - l + 1 - maxf > k): # more replacements needed than we're allowed
                count[s[l]] -= 1 # decrement leftmost char since it isn't relevant to lrcr
                l += 1 # slide window forward since prev window is now invalid
            res = max(r - l + 1, res) # return longest repeating char replacement
            # where r - l + 1 is the size of the sliding window
        return res

        # time complexity: O(n), since we iterate through s once, and each char
        # is added/removed from count at most once

        # space complexity: O(1), since the hashmap can hold at most 26 uppercase
        # letters regardless of input size — bounded by a constant, not n