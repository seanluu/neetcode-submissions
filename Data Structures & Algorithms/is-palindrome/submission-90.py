class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointers, since we want to work towards the middle
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

    # Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9') or
        ord('A') <= ord(c) <= ord('Z'))