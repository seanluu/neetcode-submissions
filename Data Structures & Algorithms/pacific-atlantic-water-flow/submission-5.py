class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):
                            q.append((nr, nc))
        
        pacific, atlantic = [], []

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        for c in range(cols): 
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res