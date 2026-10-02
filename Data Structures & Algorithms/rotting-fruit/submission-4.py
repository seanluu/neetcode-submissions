class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # 0 represents an empty cell
        # 1 represents a fresh fruit
        # 2 represents a rotten fruit 

        # this is a breadth-first-search problem, since all rotten oranges (2)
        # start spreading rot at the same time as their neighboring fresh oranges (1)

        # every bfs lvl represents 1 min, so if a fresh ornage is reached, then it
        # becomes rotten in the next minute 

        q = collections.deque() # queue to process oranges level by level (BFS, not DFS)

        fresh = 0 # count of fresh oranges remaining — need this to hit 0 by the end

        time = 0 # tracks elapsed minutes, incremented once per BFS level

        rows, cols = len(grid), len(grid[0])

        # scan the whole grid once: count fresh oranges, and seed the queue
        # with every rotten orange's starting position (all rot spreads at once)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # keep going as long as there's fresh fruit left AND still active rot to spread
        while fresh > 0 and q:
            length = len(q) # snapshot queue size — this is exactly "one level" of BFS,
                              # i.e. every orange that rotted during the previous minute
            for i in range(length): # process only this level's oranges, not ones added during it
                r, c = q.popleft()
                for dr, dc in directions: # check all 4 neighbors
                    row, col = r + dr, c + dc
                    # in bounds AND currently fresh — rot can spread here
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2 # mark as rotten (visited)
                        q.append((row, col)) # it'll spread rot further next level
                        fresh -= 1 # one less fresh orange remaining
            time += 1 # one full minute has passed — every orange in this level just rotted

        # if any fresh oranges never got reached, it's impossible -> -1
        # otherwise, time holds the number of minutes it took
        return time if fresh == 0 else -1