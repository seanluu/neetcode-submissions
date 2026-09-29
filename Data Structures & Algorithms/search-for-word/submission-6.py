class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):

            if i >= len(word): # base case: matched every character already
                return True

            # constraints, all checked at once:
            # out of bounds, wrong character, or already in use on this path
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#"):
                return False

            # mark this cell as in-use, before exploring neighbors
            board[r][c] = "#"

            # choices: try all 4 directions, looking for word[i+1] next.
            # 'or' short-circuits — stop exploring as soon as one path succeeds
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            # backtrack: restore the real letter once all 4 directions have been explored,
            # so other paths can still use this cell
            board[r][c] = word[i]

            return res

        # word could start matching from any cell, so try every one as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False