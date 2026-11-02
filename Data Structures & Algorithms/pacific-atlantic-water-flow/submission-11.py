class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(heights), len(heights[0])

        pac = [[False] * cols for i in range(rows)]

        atl = [[False] * cols for i in range(rows)]

        # every cell we see is automatically in ocean, so we just use q = deque(ocean) by default
        def bfs(source, ocean):
            q = deque(source)
        
            for r, c in source:
                ocean[r][c] = True

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if ocean[nr][nc] or heights[nr][nc] < heights[r][c]:
                        continue
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