class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # up, down, right, left
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(heights), len(heights[0])

        # same shape as heights: [False] * cols is one row, range(rows) is how many rows
        # pac[r][c] / atl[r][c] = True means water at (r, c) can reach that ocean
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        # source = edge cells touching the ocean, ocean = grid to mark (pac or atl)
        # walk UPHILL from the ocean: if a neighbor is >= current, water could flow
        # down from the neighbor to here, so the neighbor can reach this ocean too
        def bfs(source, ocean):
            q = deque(source)
            for r, c in source:
                ocean[r][c] = True                 # edge cells touch the ocean directly

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue                   # off the grid, skip
                    if ocean[nr][nc] or heights[nr][nc] < heights[r][c]:
                        continue                   # already visited or downhill, skip
                    ocean[nr][nc] = True           # mark when queued so it's only added once
                    q.append((nr, nc))

        pacific = []
        atlantic = []

        # top row touches the Pacific, bottom row touches the Atlantic
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        # left column touches the Pacific, right column touches the Atlantic
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        # spread inland from each ocean separately
        bfs(pacific, pac)
        bfs(atlantic, atl)

        # answer = cells that can reach both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res