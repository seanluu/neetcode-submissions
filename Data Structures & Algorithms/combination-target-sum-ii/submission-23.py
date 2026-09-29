class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # base case: if total is same as target, stop
        # choices: include candidates[i] in our comb sum, exclude otherwise
        # constraints: if total > target or i cannot go out of bounds
        # backtracking step: pop the last added element to the curr path
        
        candidates.sort() # use sort to get rid of deduplicates

        res = []

        def dfs(i, curr, total):
            if total == target: # base case
                res.append(curr.copy())
                return

            if total > target or i >= len(candidates): # constraints
                return

            # choice #1: include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop() # backtracking step

            # choice #2: exclude candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 
            dfs(i + 1, curr, total)

        dfs(0, [], 0) # start at origin for all parameters

        return res

            