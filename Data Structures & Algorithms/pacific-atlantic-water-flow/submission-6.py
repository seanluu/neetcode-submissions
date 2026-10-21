class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        pac = [[False] * cols for i in range(rows)] # top and left sides

        atl = [[False] * cols for i in range(rows)] # bottom and right sides

        def bfs(source, ocean):
            q = deque(source)
            for r, c in source:                      # plant: mark every starting cell
                ocean[r][c] = True

            while q:
                r, c = q.popleft()                   # pop
                for dr, dc in directions:            # peek
                    nr, nc = r + dr, c + dc
                    # pass: out of bounds, already reached, or too low to flow back to (r, c)
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols
                            or ocean[nr][nc]
                            or heights[nr][nc] < heights[r][c]):
                        continue
                    ocean[nr][nc] = True             # paint
                    q.append((nr, nc))               # push

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