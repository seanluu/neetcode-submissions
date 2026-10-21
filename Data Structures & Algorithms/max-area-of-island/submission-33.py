class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visited = set()

        # we can use dfs here, since we want to find how deep an island can go
        # an island can be 1 or 31, just depends on if there is a group
        # of 1s connected horizontally or vertically

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0 

            visited.add((r, c))

            # so basically, we only needed to know that an island existed last time, 
            # but this time we have to actually know how big each island is, so 
            # therefore we need to return the size from DFS so it can travel back up to the outer loop.
            return 1 + (dfs(r + 1, c) +
            dfs(r - 1, c) + 
            dfs(r, c + 1) +
            dfs(r, c - 1))

        area = 0

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))

        return area