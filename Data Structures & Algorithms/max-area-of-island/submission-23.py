class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # because we're working with a 2d grid duhhhh
        rows, cols = len(grid), len(grid[0])

        # up, down, left, right
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # hashset to make sure we don't revisit the same island twice
        visited = set()

        # rows, cols
        def dfs(r, c):
            # out of bounds, water, or if coords are already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c)) # add set of coords to visited so we don't repeat

            # check up, down, left, right directions
            return 1 + (dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

        area = 0 

        # iterate through each cell once
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))

        return area