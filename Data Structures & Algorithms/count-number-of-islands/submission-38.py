class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0 # integer is our output

        rows, cols = len(grid), len(grid[0])

        # all four directions, up, down, left, right
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # constraints: stop if out of bounds, or this cell is water/already-visited land
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0" # mark this cell as visited by sinking it

            # visit all 4 directions of the island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # iterate through each cell once
        for r in range(rows):
            for c in range(cols):
                # if we come across land, make sure we run dfs to make sure we don't double count any visited islands already
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1 # increment the count of islands that we have
        
        return islands # return final number of islands we have in our grid