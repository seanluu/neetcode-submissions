class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # 2d grid, must scan all 4 directions as well so could be a graph problem

        # base case: if i == len(word), so every letter matched and the word is found
        # choices: move to one of 4 neighbors (up, down, left, right)
        # constraints: we cannot go out of bounds on rows or cols, cannot be a "#", and the word must be actually on our board
        # backtracking step: restore board[r][c] after exploring so other paths can use it
        
        rows, cols = len(board), len(board[0])

        # row, col, index
        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            # constraints
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#" or word[i] != board[r][c]:
                return False

            # mark as used so this path can't revisit it
            board[r][c] = "#"

            # choices
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            # backtrack: restore the letter so other paths can use this cell
            board[r][c] = word[i]

            return res

        # try every cell as a starting point for word[0]
        for r in range(rows):
            for c in range(cols):
                # can we spell the whole word starting here? (i = 0, the first letter)
                if dfs(r, c, 0):
                    return True

        return False