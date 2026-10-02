class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds, or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # mark this cell as visited by sinking it
            grid[r][c] = "0" 

            # visit all 4 directions of the island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # iterate through each cell once
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # nvisited land, if it is a new island
                # then we should sink it so we don't double count it
                    dfs(r, c)
                    islands += 1 # increment the count of islands we have

        return islands
