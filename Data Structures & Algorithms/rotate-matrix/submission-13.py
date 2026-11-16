class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r
                # we rotate clockwise, so every value moves one spot clockwise:
                #   top-left -> top-right -> bottom-right -> bottom-left -> top-left
                # to avoid overwriting a value before we copy it, we fill each spot
                # with the value that belongs there, starting from top-left and going counterclockwise
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