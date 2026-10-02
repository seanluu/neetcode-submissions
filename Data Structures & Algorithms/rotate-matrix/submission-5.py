class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1 # l/r mark the current ring's left/right (also top/bottom, since square)

        while l < r: # process one ring at a time, moving inward, until rings meet at the center
            for i in range(r - l): # walk along one edge of the CURRENT ring (not the whole matrix)
                top, bottom = l, r

                # save top-left value before it gets overwritten
                topLeft = matrix[top][l + i]

                # bottom-left -> top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom-right -> bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # top-right -> bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # saved top-left -> top-right (completes the 4-way cycle)
                matrix[top + i][r] = topLeft

            r -= 1 # shrink the ring inward
            l += 1