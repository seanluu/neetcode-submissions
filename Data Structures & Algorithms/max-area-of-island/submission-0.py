class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0 # this problem uses the numbers directly, not in quotes like number of islands
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        # we probably want to use islands = max(islands, ...)
        # to replace the old max area with the new max area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    islands = max(islands, area)

        return islands