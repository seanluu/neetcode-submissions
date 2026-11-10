class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        # binary search over rows to find the one whose range could hold target
        top, bot = 0, rows - 1

        while top <= bot:
            row = top + ((bot - top) // 2) # middle row
            if target > matrix[row][-1]: # target past this row's max, search rows below
                top = row + 1
            elif target < matrix[row][0]: # target before this row's min, search rows above
                bot = row - 1
            else: # target falls within this row's range, this is the row
                break

        if not top <= bot: # pointers crossed, no row's range contains target
            return False

        # binary search within the row we found
        l, r = 0, cols - 1

        while l <= r:
            mid = l + ((r - l) // 2) # middle col
            if target > matrix[row][mid]: # target is to the right
                l = mid + 1
            elif target < matrix[row][mid]: # target is to the left
                r = mid - 1
            else:
                return True # found it
        return False # not in the row

        # tc: O(log m + log n) = O(log(m * n)), binary search over m rows, then over n cols in one row
        # sc: O(1), just pointers