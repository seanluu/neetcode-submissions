class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # palindrome is a string that reads the same forward and backward
        # so basicallyyyyyy we care about reading from left to right so
        # it makes sense to use a two pointers approach here

        # case-insensitive and ignores all non-alphanumeric chars
        # Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9') or
        ord('A') <= ord(c) <= ord('Z'))