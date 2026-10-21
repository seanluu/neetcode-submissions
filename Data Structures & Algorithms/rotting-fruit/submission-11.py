class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        fresh = 0

        time = 0

        q = deque()

        # itertae through each cell in our grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 # add a fresh fruit
                if grid[r][c] == 2:
                    q.append((r, c)) # add rotten fruit to queue
                
        while q and fresh > 0:
            length = len(q)
            # iterate through every rotten fruit in our queue
            for i in range(length):
                r, c = q.popleft()
                # iterate in each direction
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # check out of bounds or if the fruit isn't fresh
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2 # fruit isn't fresh
                    q.append((nr, nc)) # add to our queue
                    fresh -= 1 # decrement the number of fresh fruit we have since it is rotten
            time += 1 # increment minutes that have passed bc every fresh fruit that becomes rotten 
            
        # return final time if we have zero fresh fruits remaining, otherwise state is impossible so we return -1
        return time if fresh == 0 else -1