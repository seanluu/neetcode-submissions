class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # 0 -> empty cell
        # 1 -> fresh fruit
        # 2 -> rotten fruit

        # every min, if a fresh fruit is horizontally or vertically adj to
        # a rotten fruit, the fresh fruit also becomes rotten

        # return the minimum # of mins that must elapse until there are zero
        # fresh fruits remaining, otherwise if this state is impossible return -1

        rows, cols = len(grid), len(grid[0])

        q = collections.deque()

        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c)) # run bfs since it is a rotten fruit

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1       