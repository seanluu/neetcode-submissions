class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        # left is first unvisited col (inclusive)
        # right is one past the last unvisited col (exclusive)
        l, r = 0, len(matrix[0])

        # top is first unvisited row (inclusive)
        # bottom is one past the last unvisited row (exclusive)
        top, bot = 0, len(matrix)


        while l < r and top < bot:
            # traverse from left to right, get every i in top row 
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1 # top row is now fully visited, so we move boundary down
        
             # get every i in the right col
            for i in range(top, bot):
                res.append(matrix[i][r - 1])
            r -= 1 # right col is now fully visited, so we move boundary left
        
            # after shrinking top and right, rectangle might collapse
            # when we have a single row or single col case, so 
            # if no valid rectangle exists, then we stop to avoid duplicates
            if not (l < r and top < bot):
                break

            # get every i in the bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bot - 1][i])
            bot -= 1 # bot row is now fully visited, so we move boundary up
        
            # get every i in the left col
            # traverse bottom to top
            for i in range(bot - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1 # left col is now fully visited, so we move boundary right
        
        return res