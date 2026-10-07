class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # use two pointers since we're scanning from left to right
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]): # if left pointer is alphanumeric, slide closer to center
                l += 1 
            while l < r and not self.alphaNum(s[r]): # if right pointer is alphanumeric, slide closer to center
                r -= 1
            if s[l].lower() != s[r].lower(): # case insensitive filter
                return False
            l, r = l + 1, r - 1 # move towards center regardless
        return True # valid palindrome

    # Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9') or
        ord('A') <= ord(c) <= ord('Z'))

    # time complexity: O(n)
    # since we iterated through each char of the string s once

    # space complexity: O(1)
    # no crazy data structures used here 