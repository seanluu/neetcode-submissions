class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # multi-source BFS: start from every treasure at the same time
        # BFS spreads in layers (distance 0, 1, 2, ...), so the first time
        # a cell is reached, it's by its closest treasure

        rows, cols = len(grid), len(grid[0])

        visit = set()
        q = deque()

        # add (r, c) to the queue if it's a valid cell we haven't reached yet
        def addCell(r, c):
            # out of bounds (min(r, c) < 0 checks both at once),
            # already visited, or water (-1), so skip it
            if (min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))   # mark visited when adding
            q.append([r, c])

        # start the queue with every treasure (distance 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0  # distance of the current layer

        while q:
            # everything currently in the queue is one layer, all at distance dist
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # distance to the nearest treasure

                # try all 4 neighbors
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1  # finished this layer, the next one is 1 step farther

        # cells no treasure can reach are never visited, so they keep their original value

        # time: O(rows * cols), each cell is added once
        # space: O(rows * cols) for the queue and visited set