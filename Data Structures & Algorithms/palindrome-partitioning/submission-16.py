class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # base case: i == len(s), so every character is used and curr is one full partition
        # choices: where the current piece ends (j)
        # constraints: the piece s[i..j] must be a palindrome
        # backtracking step: pop the piece after exploring

        res = [] # output is an array

        def dfs(i, curr):
            # base case: completed our palindrome
            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    curr.append(s[i : j + 1])
                    dfs(j + 1, curr)
                    curr.pop()

        dfs(0, [])
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1 # move inward on each step
        return True
