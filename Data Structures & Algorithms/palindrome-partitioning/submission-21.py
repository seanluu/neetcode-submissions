class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        # base case: i == len(s), so every character is used and curr is one full partition
        # choices: where the current piece ends (j)
        # constraints: the piece s[i..j] must be a palindrome
        # backtracking step: pop the piece after exploring
        
        res = []

        def dfs(i, curr):
            # used every character, so save a copy of this partition
            if i >= len(s):
                res.append(curr.copy())
                return

            # i = start of piece, j = end of piece
            for j in range(i, len(s)):
                if self.isPali(s, i, j):           # only use palindrome pieces
                    curr.append(s[i : j + 1])      # choose: s[i..j] (+1 since slices skip the end)
                    dfs(j + 1, curr)               # explore: next piece starts after j
                    curr.pop()                     # undo

        dfs(0, [])

        return res
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True