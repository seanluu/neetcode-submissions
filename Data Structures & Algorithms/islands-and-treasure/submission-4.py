class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # instead of running BFS from every empty room, we run BFS once starting from all
        # treasure (0 cells) at the same time

        # since BFS spreads out in "waves" of distance 0, 1, 2, ...
        # if we start the queue with all treasures, the first time the wave reaches an empty cell
        # it must be the closest treasure (since BFS guarantees the first visit is the shortest dist)
        # in an unweighted grid), so each cell gets filled with its minimum distance to any treasure

        rows, cols = len(grid), len(grid[0])

        visit = set()

        q = deque()

        def addCell(r, c):
            # either out of bounds, visited already, or is a water cell that cannot be traversed
            if (min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == -1):
                return
            # otherwise, we can traverse or it is in bounds
            visit.add((r, c))
            q.append([r, c])
        
        # iterate through each cell once
        for r in range(rows):
            for c in range(cols):
                # if it is a treasure chest, add to the queue to be searched
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        # while our q isn't empty
        while q:
            # process every node currently in the queue (one BFS lvl = distance dist)
            for i in range(len(q)):
                r, c = q.popleft() # for every cell we pop
                # set grid[r][c] = dist (distance to the nearest trasure)
                grid[r][c] = dist
                # try all 4 neighbors, and if they're in bounds,
                # we mark it as visited and push to the queue
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1 # after we finish the lvl, we increment the dist