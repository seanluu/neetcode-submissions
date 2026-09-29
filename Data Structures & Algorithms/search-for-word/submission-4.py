class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # base case: i == len(word) — every character matched via a valid path so far
        # choices: which of the 4 neighboring cells to move into next (up/down/left/right)
        # constraints: r,c must stay in bounds; board[r][c] must match word[i];
        #              can't reuse a cell already in use on this path (marked '#')
        # backtracking step: restore board[r][c] to its real letter after exploring,
        #                     so other paths can still use this cell

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word): # base case: matched every character already
                return True

            # constraints, all checked at once:
            # out of bounds, wrong character, or already in use on this path
            if (r < 0 or c < 0 or r >= rows or c >= cols
                    or word[i] != board[r][c] or board[r][c] == "#"):
                return False

                # word[i] != board[r][c] checks "does the letter at this cell match the letter I'm currently looking for"

            board[r][c] = "#" # mark this cell as in-use for this path

            # choices: try all 4 directions, looking for word[i+1] next.
            # 'or' short-circuits — stop exploring as soon as one path succeeds
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            board[r][c] = word[i] # backtrack: restore the real letter for other paths
            return res

        # word could start matching from any cell, so try every one as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False