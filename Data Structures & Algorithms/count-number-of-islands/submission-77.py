class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(dr + r, dc + c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

        # tc: O(m * n), each cell is visited by the loop once and flipped to "0" by dfs at most once
        # sc: O(m * n), recursion stack can go m*n deep in the worst case (grid is all land)