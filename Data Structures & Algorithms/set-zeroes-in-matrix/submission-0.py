class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Use the first row to mark which columns should become zero
        # Use the first column to mark which rows should become zero

        rows, cols = len(matrix), len(matrix[0])

        rowZero = False
        
        # traverse every cell
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # mark col by setting like this
                    if r > 0:
                        matrix[r][0] = 0 # mark row by setting matrix[r][0] = 0
                    else:
                        rowZero = True # first row needs to be zeroed so we mark as True
        
        # second pass, apply markers to the inner matrix
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # handle first col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0 # zero out the entire first col

        # handle first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0 # zero out the entire first row