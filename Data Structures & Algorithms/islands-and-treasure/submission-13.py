class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])

        visit = set()

        q = deque()

        def addCell(r, c):
            # check out of bounds and if water cell can't be traversed or if we visited the cell already
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit:
                return
            
            # sink the cell
            visit.add((r, c))

            # add cell to the queue
            q.append([r, c])

        # iterate through each cell
        for r in range(rows):
            for c in range(cols):
                # if we have a treasure cell
                if grid[r][c] == 0:
                    q.append([r, c]) # add to the queue
                    visit.add((r, c)) # mark as visited 
        
        dist = 0

        # bfs timeeeee
        while q:
            # iterate through each cell we added to the queue
            for i in range(len(q)):
                r, c = q.popleft() # pop row and cols
                grid[r][c] = dist # mark as the current distance
                # search up, down, left, right directions
                addCell(r + 1, c) 
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1 # after we process every cell in the current layer, 
            # dist goes up by 1 and the while loop runs again on the next layer