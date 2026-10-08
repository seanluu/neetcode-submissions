class Solution:
    def isPalindrome(self, s: str) -> bool:

        # two pointers reading from each end toward the center,
        # until they meet or cross

        # first and last index
        l, r = 0, len(s) - 1

        while l < r:
            # skip non-alphanumeric chars on the left
            # (l < r so the pointers don't cross, e.g. if s is all punctuation)
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip non-alphanumeric chars on the right
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            # compare ignoring case, a mismatch means it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1  # they matched, slide both pointers closer to center
        return True

    # True if c is a letter (a-z, A-Z) or a digit (0-9)
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9') or
                ord('A') <= ord(c) <= ord('Z'))