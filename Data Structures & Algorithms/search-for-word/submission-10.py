class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word): # base case
                return True

            # constraints: out of bounds, char doesn't match, or cell is already in use on this path
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#":
                return False

            board[r][c] = "#" # mark cell as used before exploring neighbors

            # choices: search all 4 directions (up, down, left, right) for word[i+1] next, and  thanks to 'or' short-circuiting, stop trying further directions once one succeeds
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            board[r][c] = word[i] # backtracking step: replace '#' with the real letter

            return res
        
        # iterate through each row once
        for r in range(rows):
            # iterate through each col once
            for c in range(cols):
                if dfs(r, c, 0): # all parameters are at origin
                    return True # word found

        return False # word couldn't be found