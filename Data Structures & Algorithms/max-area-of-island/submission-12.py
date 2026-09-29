class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set() # use a set to keep track of already visited cells

        def dfs(r, c): # visit all connected land cells (up, down left, right)
            # stop if out of bounds, water (0), or if we visited already
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c)) # mark cell as visited
            return (1 + dfs(r + 1, c) + # return 1 + area from all 4 neighbors total
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))
             
        area = 0 # base case since our output is an integer after all

        # for every cell in grid, if it is land (1) and unvisited, run dfs
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c)) # update max area after each dfs call
        
        return area # return max area found