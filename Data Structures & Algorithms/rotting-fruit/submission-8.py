class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # use bfs here, since we also need to go layer by layer
        # if a fresh fruit is horizontally or vertically adj to a
        # rotten fruit, then the fresh fruit also becomes rotten

        rows, cols = len(grid), len(grid[0])

        time = 0

        fresh = 0

        q = deque()

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

            