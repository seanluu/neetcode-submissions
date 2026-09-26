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

            # choice #2: exclude candidates[i] — but if there are duplicates of candidates[i]
            # right after it, skip past ALL of them too before recursing. Otherwise,
            # "exclude candidates[i], then separately consider candidates[i+1]" would
            # re-explore the same decision on an identical value, producing duplicate combos
            
            # i +1 < len(candidates) checks the bounds
            # second part checks if the next one is a duplicate of the previous candidate
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 # skip past all of the duplicates by incrementing += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0) # set all parameters to origin

        return res