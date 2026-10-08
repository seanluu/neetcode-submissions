class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # find the length of the longest substring without dupe chars

        res = 0

        l = 0

        dupe = set()

        # iterate through each letter in the string s, end at the rightmost element
        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1 # slide window forward, since we ruled that s[l] was a dupe
            dupe.add(s[r])
            res = max(res, r - l + 1)
        return res