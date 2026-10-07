class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # define the rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # search range over the rows, from the first row to the last row
        top, bot = 0, rows - 1

        # binary search to find the exact row of our target element
        while top <= bot:
            row = top + ((bot - top) // 2)
            # target is bigger than this row's last (largest) value,
            # so the whole row is too small, look at lower rows
            if target > matrix[row][-1]:
                top = row + 1
            # target is smaller than this row's first (smallest) value,
            # so the whole row is too big, look at higher rows
            elif target < matrix[row][0]:
                bot = row - 1
            # target is within this row's range, so this is the row
            else:
                break

        # pointers crossed, so no row's range contains target
        if not top <= bot:
            return False

        l, r = 0, cols - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            # now that we're in the specific row of the element we want,
            # now we can use binary search specifically to find the element
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
            
        return False

