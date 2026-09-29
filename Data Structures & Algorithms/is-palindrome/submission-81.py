class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointers: a palindrome reads the same forwards and backwards,
        # so compare from both ends inward
        l, r = 0, len(s) - 1

        while l < r: # stop once pointers meet or cross — everything's been compared
            # skip left pointer past non-alphanumeric chars (spaces, punctuation, etc.)
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip right pointer past non-alphanumeric chars
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            # the l < r check inside each inner loop prevents overshooting when
            # the string is entirely non-alphanumeric between the pointers
            # (e.g. s = ",." — without this guard, l or r could walk out of range)

            if s[l].lower() != s[r].lower(): # case-insensitive comparison
                return False
            l, r = l + 1, r - 1 # move both pointers one step inward

        return True 

    def alphaNum(self, c):
        # check if c falls in the ASCII range of lowercase, digit, or uppercase
        # (Python's c.isalnum() does this too, more concisely)
        return (ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9') or
        ord('A') <= ord(c) <= ord('Z'))