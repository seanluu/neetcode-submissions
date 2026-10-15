class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        # 1 2 
        # 3 4

        # 3 1
        # 4 2

        # topLeft = matrix[top][l + i]                    # topLeft = matrix[0][0] = 1
        # matrix[top][l + i]    = matrix[bottom - i][l]   # matrix[0][0] = matrix[1][0]  -> 3
        # matrix[bottom - i][l] = matrix[bottom][r - i]   # matrix[1][0] = matrix[1][1]  -> 4
        # matrix[bottom][r - i] = matrix[top + i][r]      # matrix[1][1] = matrix[0][1]  -> 2
        # matrix[top + i][r]    = topLeft                 # matrix[0][1] = 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i] 
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1