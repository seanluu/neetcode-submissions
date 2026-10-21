class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visited = set()

        # we can use dfs here, since we want to find how deep an island can go
        # an island can be 1 or 31, just depends on if there is a group
        # of 1s connected horizontally or vertically

        def bfs(r, c):
            q = deque()

            grid[r][c] = 0

            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

            # so basically, we only needed to know that an island existed last time, 
            # but this time we have to actually know how big each island is, so 
            # therefore we need to return the size from DFS so it can travel back up to the outer loop.

        area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area