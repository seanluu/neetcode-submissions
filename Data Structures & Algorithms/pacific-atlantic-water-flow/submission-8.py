class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(heights), len(heights[0])

        # one row, number of rows
        pac = [ [False] * cols for r in range(rows) ]
        atl = [ [False] * cols for r in range(rows) ]

        # start, ocean
        def bfs(source, ocean):
            q = deque(source)

            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                            continue                                  # off the grid, skip
                        if ocean[nr][nc] or heights[nr][nc] < heights[r][c]:
                            continue                                  # visited or downhill, skip
                        ocean[nr][nc] = True
                        q.append((nr, nc))

        pacific = []
        atlantic = []

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res
