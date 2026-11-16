class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r
                # if we change from the top row to the bottom row, 
                # the fixed row changes from top to bot, and the moving 
                # column flips direction from l + i to r - i.
                topLeft = matrix[top][l + i] # top row, i steps right of the left edge
                # overwrite the top-left spot with the bottom-left value
                matrix[top][l + i] = matrix[bot - i][l]
                # overwrite the bottom-left spot with the bottom-right value
                matrix[bot - i][l] = matrix[bot][r - i]
                # overwrite the bottom-right spot with the top-right value
                matrix[bot][r - i] = matrix[top + i][r]
                # overwrite the top-right spot with the saved top-left value
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1