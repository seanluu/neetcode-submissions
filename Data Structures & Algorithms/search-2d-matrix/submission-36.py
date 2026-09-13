class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # consider rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # then consider moving up and down the board
        top, bot = 0, len(matrix) - 1

        # since we want to find a specific target and if it exists, check here
        while top <= bot:
            row = top + ((bot - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False

        l, r = 0, cols - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
            
        return False