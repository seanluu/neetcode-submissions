class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows, cols = len(heights), len(heights[0])

        # we need hashsets for each pacific and atlantic
        # - pacific border cells (top row + left column)
        # - atlantic border cells (bot row + right col) 

        pac = set() 
        atl = set()

        def dfs(r, c, visit, prevHeight):
            # base case + constraint: out of bounds, already visited, OR this cell
            # is LOWER than where we came from — water can't flow uphill, so a
            # cell can only be reached by flowing from a HIGHER (or equal) neighbor
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight or (r, c) in visit:
                return

            # mark cell as reachable from this ocean (visited for this DFS)
            visit.add((r, c))

            # choices: flow outward in all 4 directions from here, carrying this
            # cell's height forward as the new "prevHeight" for comparison
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # seed DFS from every cell along the top row and bottom row —
        # top row touches the Pacific, bottom row touches the Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # seed DFS from every cell along the left column and right column —
        # left column touches the Pacific, right column touches the Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # a cell can reach both oceans only if it was visited during BOTH
        # the pacific-seeded DFS runs AND the atlantic-seeded DFS runs
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res