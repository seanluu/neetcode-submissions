class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        fresh = 0

        time = 0

        q = deque()

        # count fresh oranges and put every rotten one in the queue (minute 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1  # count a fresh orange
                if grid[r][c] == 2:
                    q.append((r, c))  # add rotten orange to the queue

        # keep spreading while there are rotten oranges to process and fresh ones left
        while q and fresh > 0:
            length = len(q)
            # process every orange that rotted last minute
            for i in range(length):
                r, c = q.popleft()
                # check up, down, left, right
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # skip if out of bounds or not a fresh orange
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2  # rot it
                    q.append((nr, nc))  # it spreads next minute
                    fresh -= 1  # one less fresh orange
            time += 1  # one minute passes after the whole layer rots

        # if every orange rotted, return the time, otherwise some were unreachable
        return time if fresh == 0 else -1