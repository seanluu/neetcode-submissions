class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # length of the longest substring without dupes -> hashset

        dupe = set()

        res = 0

        # since we need to find the longest string without dupes, that means
        # we use a sliding window since there's a max amt before we reach a duplicate char

        l, r = 0, len(s) - 1 # first and last index for sliding window

        res = 0 # return an integer

        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l += 1
            dupe.add(s[r])
            res = max(res, r - l + 1)
        return res