class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0  # total number of islands found

        rows, cols = len(grid), len(grid[0])

        # up, down, right, left
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # flood-fill from (r, c), sinking every connected "1" to "0"
        def dfs(r, c):
            
            # stop if out of bounds or we hit water/already-visited land
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # mark this cell as visited by sinking it
            grid[r][c] = "0"

            # visit all 4 neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # found unvisited land, a new island
                    dfs(r, c)  # sink the whole island so we don't recount it
                    islands += 1

        return islands