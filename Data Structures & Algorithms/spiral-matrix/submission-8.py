class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        # four boundaries of the unvisited rectangle
        l, r = 0, len(matrix[0])  # left = leftmost unvisited col, right = one past the rightmost unvisited col
        top, bot = 0, len(matrix) # top = topmost unvisited row, bottom = one past the bottommost unvisited row

        # keep going while there is still an unvisited rectangle
        while l < r and top < bot:
            # 1. left -> right across the top row (cols l to r - 1)
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1 # top row is done, shrink inward

            # 2. top -> bottom down the right column (rows top to bot - 1)
            for i in range(top, bot):
                res.append(matrix[i][r - 1])
            r -= 1 # right column is done, shrink inward

            # if the remaining rectangle is invalid, break (prevents duplicates)
            if not (l < r and top < bot):
                break

            # 3. right -> left across the bottom row (cols r - 1 down to l)
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bot - 1][i])
            bot -= 1 # bottom row is done, shrink inward

            # 4. bottom -> top up the left column (rows bot - 1 up to top)
            for i in range(bot - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1 # left column is done, shrink inward

        return res