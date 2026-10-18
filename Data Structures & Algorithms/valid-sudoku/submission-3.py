class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)     # digits seen in each column
        rows = defaultdict(set)     # digits seen in each row
        squares = defaultdict(set)  # digits seen in each 3x3 box
        # sets give O(1) lookups to check for duplicates

        # check every cell on the 9x9 board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # empty cell, nothing to check
                    continue

                # (r // 3, c // 3) maps each cell to its 3x3 box,
                # e.g. rows 0-2 / cols 3-5 -> box (0, 1)

                # check for duplicates, NOT an out of bounds check
                # check if the current digit was already seen in this row, col, or square,
                # if so, then invalid
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # no duplicate, so record this digit
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

        # O(81) since we're working with a 9x9 sudoku board
        # tc: O(81) = O(1), fixed board size (O(n^2) for an n x n board)
        # sc: O(81) = O(1)