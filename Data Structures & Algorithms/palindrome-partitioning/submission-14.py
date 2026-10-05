class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # base case: i >= len(s) — every character has been assigned to some piece
        # choices: for each starting point i, try every possible substring
        #          s[i:j+1] as "the next piece" (j sweeps from i to end of s)
        # constraints: only take a cut if s[i:j+1] is actually a palindrome —
        #              unlike subsets, this problem has a REAL constraint to check
        # backtracking step: pop the last piece before trying a different cut length

        res = []
        curr = []

        def dfs(i):
            if i >= len(s): # base case: used up every character, partition complete
                res.append(curr.copy())
                return

            for j in range(i, len(s)): # choices: try every possible end-point for this piece
                if self.isPali(s, i, j): # constraint: only proceed if s[i:j+1] is a palindrome
                    curr.append(s[i:j+1]) # choice: commit to this piece
                    dfs(j + 1) # move past this whole piece, not just one character
                    curr.pop() # backtrack: undo before trying a different cut

        dfs(0)
        return res

    # handle palindrome check with two pointers in a separate function
    def isPali(self, s, l, r):
        # two pointers: walk inward from both ends, checking mirrored characters match
        while l < r:
            if s[l] != s[r]: # mismatch found — not a palindrome
                return False
            l, r = l + 1, r - 1 # move both pointers one step inward
        return True # pointers met/crossed without a mismatch — it's a palindrome