class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # since we can either go up, down, left, right
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        islands = 0 # running count of islands found — just the answer accumulator, not a base case
        rows, cols = len(grid), len(grid[0]) 

        # run depth first search on the rows and columns
        def dfs(r, c):
            
            # base case (does double duty): out of bounds, OR water/already-visited
            # (sunk land is also marked '0', so this catches both cases)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # constraint: stay in bounds; never revisit sunk/water land
            # mark as visited by sinking the land
            grid[r][c] = "0" 

            # choices: explore all 4 neighbors
            # [1,  0]  -> down
            # [-1, 0]  -> up
            # [0,  1]  -> right
            # [0, -1]  -> left

            # dr = "delta r" = "change in r" (r = row)
            # dc = "delta c" = "change in c" (c = column)
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            # NOTE: no backtracking/undo here, unlike subsets/permute/word search —
            # sinking is permanent since each cell only ever needs exploring once,
            # not revisited across multiple alternate paths

        # iterate through each row and column
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # if we see unvisited land, it's the start of a NEW island
                    dfs(r, c) # sink the entire connected island
                    islands += 1 # count it once

        return islands # return final total of islands