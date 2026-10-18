class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set) # track digits in each row, hashset is nec
        rows = defaultdict(set) # track digits in each col, hashset is nec
        squares = defaultdict(set) # track digits in each subbox, hashset is nec

        # needs to be a 9x9 sudoku board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if char == ".", we continue (but why)
                    continue

                # check out of bounds for rows, cols, and squares
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # otherwise if in bounds, we can add the rows, cols, squares we want
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
