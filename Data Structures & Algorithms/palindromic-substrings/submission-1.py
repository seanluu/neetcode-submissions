class Solution:
    def countSubstrings(self, s: str) -> int:

        # expand around center: try each index as the middle of a palindrome,
        # grow outward while the ends match, and count each palindrome found

        res = 0

        # treat each index as the center of a palindrome
        for i in range(len(s)):
            # odd length (like "aba"): middle is one character
            l, r = i, i
            # stay in bounds and keep going while the ends match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1  # s[l..r] is a palindrome, count it
                l -= 1    # expand outward
                r += 1

            # even length (like "abba"): middle is between two characters
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res  # O(n^2) time, O(1) space