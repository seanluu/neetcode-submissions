class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        # four corners, 1 cant go any higher or go left
        # 2 cant go higher or right
        # 4 can't go right or lower
        # 3 cant go lower or left
        
        # directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # rows, cols
        m, n = len(matrix), len(matrix[0])

        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return

            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
        
            dfs(col, row - 1, r, c, dc, -dr)
        
        dfs(m, n, 0, -1, 0, 1)
        return res
    