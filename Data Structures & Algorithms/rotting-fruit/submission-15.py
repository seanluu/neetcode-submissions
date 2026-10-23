class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # since we care about the directions that the fruit goes in...
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(grid), len(grid[0])

        fresh = 0

        time = 0

        q = deque() # use bfs, since we want to go layer by layer
        # checking whether or not fresh fruit is next to rotten fruit

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c)) # add to queue since we want to investigate

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # check out of bounds, and that the cell is not a fresh fruit
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1: 
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time += 1

        # return minimum time
        return time if fresh == 0 else -1

