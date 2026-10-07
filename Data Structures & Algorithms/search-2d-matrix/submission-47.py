class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        # search range over the rows, from the first row to the last row
        top, bot = 0, rows - 1

        # binary search for the row that could contain target
        while top <= bot:
            row = top + ((bot - top) // 2)
            # target is greater than the last element of the row (largest)
            # so the whole row is too small, and we want to look at lower rows
            if target > matrix[row][-1]:
                top = row + 1
            # target is less than the first element of the row (smallest)
            # so the whole row is too big, and we want to look at higher rows
            elif target < matrix[row][0]:
                bot = row - 1
            # target is within this row's range, so this is the row
            else:
                break

        # pointers crossed, so no row's range contains target
        if not top <= bot:
            return False

        # binary search inside that row for the exact element
        l, r = 0, cols - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            # target is greater than the current element, so it's to the right
            if target > matrix[row][mid]:
                l = mid + 1 # throw away the left half since target element isn't there
            # target is smaller than the current element, so it's to the left
            elif target < matrix[row][mid]:
                r = mid - 1 # throw away the right half since target element isn't there
            # found it
            else:
                return True

        return False  # not in the row

        # time: O(log m + log n), one binary search over rows, one over columns
        # space: O(1)