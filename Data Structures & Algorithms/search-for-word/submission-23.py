class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # base case:
            if i == len(word): # all letters match so we found a valid word, so we ret True
                return True
            # constraints: rows/cols are out of bounds, the cell was already used (#) or it doesn't match word[i]
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#" or word[i] != board[r][c]:
                return False

            # mark as visited
            board[r][c] = "#"

            # choices: search all 4 directions
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            # backtracking step: restore the letter so other paths can use this cell
            board[r][c] = word[i] 

            return res

        # try every cell as a starting point for word[0]
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): # if we can spell whole word starting from here, return True
                    return True

        return False