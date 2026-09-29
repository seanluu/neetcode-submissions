class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # base case: return true if the word is present in the grid
        # choices: include letter in the word
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to the curr path
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#"):
                return False
            
            board[r][c] = "#"

            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
    
        return False

            