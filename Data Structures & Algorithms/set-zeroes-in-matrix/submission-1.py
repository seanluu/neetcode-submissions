class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # use the first row to mark which cols should become zero
        # use the first col to mark which rows should become zero
        # matrix[0][0] marks col 0, so row 0 gets its own flag (rowZero)

        rows, cols = len(matrix), len(matrix[0])

        rowZero = False  # whether row 0 needs to be zeroed

        # first pass: find zeros and mark their row and col
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # mark col c
                    if r > 0:
                        matrix[r][0] = 0  # mark row r
                    else:
                        rowZero = True  # row 0 can't use matrix[0][0], so use the flag

        # second pass: zero inner cells whose row or col is marked
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # col 0: must happen before zeroing row 0, which would overwrite matrix[0][0]
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # row 0: done last, using its separate flag
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0