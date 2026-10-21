class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        fresh = 0

        time = 0

        q = deque() # use bfs since we want to go layer by layer for which is rotting

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # while we have a non-empty queue filled with rotten fruit, and we have more than 1 fresh fruit
        # that means that it's possible that fresh fruit becomes rotten if it is horizontally or vertically
        # adjacent to a rotten fruit
        while q and fresh > 0:
            length = len(q)
            # iterate through the number of rotten fruit we have...
            for i in range(length): 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


            