class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque() # process oranges level by level (BFS)

        fresh = 0 # count of fresh oranges remaining

        time = 0 # tracks elapsed mins, inrement once per BFS lvl

        rows, cols = len(grid), len(grid[0])

        # iterate through each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # if we have fresh fruit, increment count
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c)) # represents a rotten visit (visited already)
    
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # if we have more than 1 fresh fruit and we have a queue, 
        # we need to check whether it will become rotten or not
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft() # pop the row and col
                for dr, dc in directions: # iterate through each direction (up, down, left, right)
                    row, col = dr + r, dc + c
                    # in bounds AND currently fresh — rot can spread here
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2 # mark as rotten (visited)
                        q.append((row, col)) # spread rot further to next lvl
                        fresh -= 1 # decrement number of fresh fruit we have
            time += 1 # one full min has passed, every orange in this level just rotted
        return time if fresh == 0 else -1 # if any fresh oranges never got reached, it is impossible
        # so we return -1, otherwise the time holds the number of minutes it took
