class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        dupe = set() # no dupe chars allowed in window -> use a hashset

        l = 0 

        for r in range(len(s)): # iterate through each letter in the string s
            while s[r] in dupe: # keep shrinking from the left until s[r] is no longer a duplicate
                dupe.remove(s[l]) # evict the leftmost character to shrink the window
                l += 1
            dupe.add(s[r]) # window is valid now — add s[r]
            res = max(res, r - l + 1) # track the longest valid window seen so far
        return res

        # time complexity: O(n) — r and l each move forward at most n times total
        # across the whole run (l never resets), so total work is O(n), not O(n^2)

        # space complexity: O(n) — dupe can hold up to n characters if s has no repeats