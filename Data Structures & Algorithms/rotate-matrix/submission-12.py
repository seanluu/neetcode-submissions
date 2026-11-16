class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r
                topLeft = matrix[top][l + i]
                # bottom-left -> top-left
                matrix[top][l + i] = matrix[bot - i][l]
                # top-left -> top-right
                matrix[bot - i][l] = matrix[bot][r - i]
                # top-right -> bottom-right
                matrix[bot][r - i] = matrix[top + i][r]
                # bottom-left -> top-left
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1