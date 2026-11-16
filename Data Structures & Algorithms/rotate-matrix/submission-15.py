class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r # row, col
                topLeft = matrix[top][l + i]
                # overwrite topLeft with botLeft
                matrix[top][l + i] = matrix[bot - i][l] 
                # overwrite botLeft with botRight
                matrix[bot - i][l] = matrix[bot][r - i]
                # overwrite botRight with topRight
                matrix[bot][r - i] = matrix[top + i][r]
                # overwrite topRight with topLeft
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1