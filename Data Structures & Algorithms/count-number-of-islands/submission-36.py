class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0 # output

        rows, cols = len(grid), len(grid[0])

        # cover up, down, left, right, directions
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # run dfs on the rows and columns
        def dfs(r, c):
            
            # out of bounds, or char does not match
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # set every cell to "0" by default 
            grid[r][c] = "0"

            # run dfs on every cell
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # iterate through each row
        for r in range(rows):
            # iterate through each col
            for c in range(cols):
                if grid[r][c] == "1": # if visited, then run dfs
                    dfs(r, c)
                    islands += 1 # increment number of islands we have
            
        return islands # return final count of islands