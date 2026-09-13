class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0]) # find rows and columns of the matrix

        top, bot = 0, len(matrix) - 1 # pointers for moving up and down the matrix

        # find the exact row of our target
        while top <= bot: 
            row = top + ((bot - top) // 2) # calculate middle row of the whole matrix
            if target > matrix[row][-1]: # if target > value of last element of the row
                top = row + 1 # move up a row to get closer to the target
            elif target < matrix[row][0]: # if target < value of first element of the row
                bot = row - 1 # move down a row to get closer to the target
            else:
                break # otherwise, we've found the row of our target

        if not top <= bot: # if top and bot pointers have crossed, target row doesn't exist
            return False
        
        l, r = 0, cols - 1 # left and right pointers for searching within the identified row
        # so we want to use cols - 1 instead of len(matrix) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target > matrix[row][mid]: # if target > value of middle element of the row
                l = mid + 1
            elif target < matrix[row][mid]: # if target < value of middle element of the row
                r = mid - 1
            else:
                return True # target is actually found 
        
        return False