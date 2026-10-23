class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visit = set()

        q = deque()

        def addCell(r, c):
            # out of bounds checking / if water can't be traversed on, or visited already
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit:
                return 

            visit.add((r, c)) # mark cell as visited
            q.append([r, c]) # add cells to the queue to look at

        # iterate through each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # if it is a treasure chest, we add it to our queue and mark as visited
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        
                

            