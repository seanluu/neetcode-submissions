class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # base case: i is the exact length of the word we're looking for (i >= len(word))
        # choices: check up, down, left, right directions to see if using a letter would
        #          contribute to us finding the word we want
        # constraints: out of bounds, wrong character, or already in use on this path
        # backtracking step: restore board[r][c] to its real letter after exploring,
        #                     so other paths can still use this cell

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word): # base case, where i is the exact length of the word we're looking for
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols          # out of bounds
                    or word[i] != board[r][c]                      # wrong character
                    or board[r][c] == "#"):                         # already in use on this path
                return False

            board[r][c] = "#" # mark this cell as in-use before exploring neighbors

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            board[r][c] = word[i] # backtrack: restore the real letter

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False