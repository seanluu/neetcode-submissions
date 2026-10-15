class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # given an m x n matrix, return all elements of the matrix
        # in a spiral order 

        # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # Output: [1,2,3,6,9,8,7,4,5]

        # m = x, n = y

        # go right x pointers, go down y points, go left x times, go up 1, go right 2
        # so the cycle goes right, down, left, up, then repeats this cycle until it's complete

        # when we go from left to right, eventually the subarray shrinks (in the middle), so
        # the left and right pointers move inwards, i.e, if we have [1, 2, 3, 4], eventually it
        # will get to [6, 7], and then the top and bottom boundaries move inwards again
        # then L and R reach the same point (no more rectangle), so we can stop the spiral

        # use four pointers

        # once we get through 1, 2, 3, 4 and reach the right boundary at R 
        # we can move the top boundary down a row
        # once we go down 4 -> 8 -> 12, and reach the bottom boundary, we can update our right
        # boundary and move it inwards, once we finish left x times, move our bottom boundary up a row
        # go up once we reach the top boundary, then we can move our left inward, then stop once we reach
        # the R boundary.

        # once top and bottom reach the same point, we can stop the spiral
        # use four pointers since we go right, down, left, up 

        # (top, left) -------------------- (top, right-1)
        #     |                                  |
        #     |                                  |
        # (bottom-1, left) ------------ (bottom-1, right-1)

        res = [] # list to store spiral traversal

        # left is first unvisited col (inclusive)
        # right is one past the last unvisited col (exclusive)
        left, right = 0, len(matrix[0]) 

        # top is first unvisited row (inclusive)
        # bottom is one past the last unvisited row (exclusive)
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # traverse from left to right, get every i in top row 
            for i in range(left, right): # left to right
                res.append(matrix[top][i]) # in the top row, column is i
            top += 1 # top row is now fully visited, so we move boundary down

            # get every i in the right col
            for i in range(top, bottom): # traverse from top to bottom 
                res.append(matrix[i][right - 1]) # right is out of bounds
            right -= 1 # right col is now fully visited, so we move boundary left

            # after shrinking top and right, rectangle might collapse
            # when we have a single row or single col case, so 
            # if no valid rectangle exists, then we stop to avoid duplicates
            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, - 1): # descending order
            # traverse right to left
                res.append(matrix[bottom - 1][i])
            bottom -= 1 # bot row is now fully visited, so we move boundary up
            
            # get every i in the left col
            # traverse bottom to top
            for i in range(bottom - 1, top - 1, - 1): # descending order
                res.append(matrix[i][left])
            left += 1 # left col is now fully visited, so we move boundary right

        return res # all elements have been visited in spiral order