class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visit = set()

        q = deque() # use bfs here since we want to go layer by layer to search for treasure

        def addCell(r, c):
            # check out of bounds, or if water can be traversed or not, or if cell has been visited already
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit:
                return

            visit.add((r, c)) # otherwise if it's normal add to visited list
            q.append([r, c]) # and append to the queue

        # iterate through each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # if treasure, add to the queue
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        while q:
            # iterate through each treasure we have
            for i in range(len(q)):
                r, c = q.popleft() # row, col
                grid[r][c] = dist # set current cell to current layer
                addCell(r + 1, c) # search every direction, up, down, left, right
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1 # increment dist to move to a new layer to search treasure in
                


