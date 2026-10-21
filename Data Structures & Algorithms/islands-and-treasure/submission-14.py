class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])

        visit = set()

        q = deque()

        def addCell(r, c):
            # skip if out of bounds, a wall, or already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit:
                return

            # mark as visited
            visit.add((r, c))

            # add to the queue for the next layer
            q.append([r, c])

        # layer 0: put every treasure in the queue before BFS starts
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])   # add to the queue
                    visit.add((r, c))  # mark as visited

        dist = 0

        # multi-source BFS, one layer at a time
        while q:
            # process every cell in the current layer
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # distance to the nearest treasure
                # queue up, down, left, right neighbors
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            # after we process every cell in the current layer,
            # dist goes up by 1 and the while loop runs again on the next layer
            dist += 1