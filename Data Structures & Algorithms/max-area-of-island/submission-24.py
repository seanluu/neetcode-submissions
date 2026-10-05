class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0]) # grid dimensions

        visited = set() # cells already counted, so we never count (or recurse on) the same cell twice

        # returns the area of the island that (r, c) belongs to (0 if it's not new land)
        def dfs(r, c):
            # base case: out of bounds, water, or cell already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c)) # mark this cell as visited

            # this cell counts as 1, plus whatever area the 4 neighbors contribute
            return 1 + (dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

        area = 0 

        # try every cell as a starting point, water and visited cells just return 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c)) # keep the largest island seen so far

        return area