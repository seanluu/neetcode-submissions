class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word): # base case
                return True

            # constraints
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == "#"):
                return False 

            board[r][c] = "#" # set as "#" before we run the dfs on the board since we haven't visited yet

            # search left, right, up, down, directions for letters that correspond with our target word
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            board[r][c] = word[i] # backtracking step: replace the matching letter

            return res

        # iterate through each row in rows
        for r in range(rows):
            # iterate through each col in cols
            for c in range(cols):
                if dfs(r, c, 0): # if we run dfs and our index hits 0, means we found the word
                    return True # therefore we can return True
        
        return False # otherwise, we did not find the words so we return False