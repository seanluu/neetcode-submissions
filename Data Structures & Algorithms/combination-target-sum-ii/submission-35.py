class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # base case: if total == target, stop here
        # choices: include candidates[i] in our comb or exclude it
        # constraints: if total is greater than target, or if index has reached the end of the candidates array
        # backtracking step: pop the last added element to the current path
        
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target: # base case
                res.append(curr.copy())
                return

            # constraints
            if total > target or i == len(candidates):
                return
            
            # choice #1: include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop() # backtracking step

            # choice #2: exclude candidates[i], and skip all its duplicates too,
            # otherwise we'd re-explore the same decision on an identical value (duplicate combos)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # bounds check, then duplicate check
                i += 1 # skip past every duplicate
            dfs(i + 1, curr, total)

        dfs(0, [], 0) # set all parameters to origin

        return res