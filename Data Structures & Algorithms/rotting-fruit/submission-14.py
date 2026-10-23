class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # use bfs here since we want to search layer by layer
        # and mark fresh fruit as rotten if it happens to be next to rotten fruit

        rows, cols = len(grid), len(grid[0])

        fresh = 0 # keep track of fresh fruit we have
        
        time = 0 # we need to keep track of time, since we want to return the 
        # min number of mins that must elapse until there are zero fresh fruits remaining

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        q = deque() 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        area = 0

        # while queue is non empty and we still have fresh fruit
        while q and fresh > 0:
            for i in range(len(q)):
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
                


            