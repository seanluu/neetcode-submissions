class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix) - 1 # l/r mark the current ring's left/right (also top/bottom, since square)

        # Example matrix:   1 2 3
        #                   4 5 6
        #                   7 8 9
        # l = 0, r = 2, so top = 0, bottom = 2

        while l < r: # process one ring at a time, moving inward, until rings meet at the center
            for i in range(r - l): # walk along one edge of the CURRENT ring (not the whole matrix)
                top, bottom = l, r

                # ---------------- i = 0 (the four corners) ----------------
                # ---------------- i = 1 (one step along each edge) ---------

                # save top-left value before it gets overwritten
                topLeft = matrix[top][l + i]
                # i=0: matrix[0][0] = 1
                # i=1: matrix[0][1] = 2

                # bottom-left -> top-left
                matrix[top][l + i] = matrix[bottom - i][l]
                # i=0: matrix[0][0] = matrix[2][0] = 7
                # i=1: matrix[0][1] = matrix[1][0] = 4

                # bottom-right -> bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # i=0: matrix[2][0] = matrix[2][2] = 9
                # i=1: matrix[1][0] = matrix[2][1] = 8

                # top-right -> bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]
                # i=0: matrix[2][2] = matrix[0][2] = 3
                # i=1: matrix[2][1] = matrix[1][2] = 6

                # saved top-left -> top-right (completes the 4-way cycle)
                matrix[top + i][r] = topLeft
                # i=0: matrix[0][2] = 1
                # i=1: matrix[1][2] = 2

                # matrix after i=0:   7 2 1      after i=1:   7 4 1
                #                     4 5 6                   8 5 2
                #                     9 8 3                   9 6 3

            r -= 1 # shrink the ring inward
            l += 1
            # now l = 1, r = 1, so l < r is false and the loop ends (5 in the center stays put)