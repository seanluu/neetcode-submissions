class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # base case: whenever total is equal to the target, we stop adding stuff to the path
        # choices: include candidates[i] in our current combination sum path or we exclude it 
            # each element from candidates may be chosen at MOST ONCE within a combination
            # therefore, we're limited to how many times we can use nums[i] for a single path
        # constraints: if total is ever greater than the target or if i is out of bounds 
        # backtracking step: pop the last added element to the path

        candidates.sort() # arrange early so we can get rid of permutations earlier

        res = []

        def dfs(i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())
                return

            # constraints: 
            if total > target or i >= len(candidates):
                return

            # choice of excluding candidates[i] in our curr comb is handled by for-loop
            # bc if we don't pick it, the next iteration (j + 1) will consider the next candidate
            for j in range(i, len(candidates)):
                # skip dupes at the same recursion level
                if j > i and candidates[j] == candidates[j - 1]: 
                    continue
                # early stop since array is already sorted
                if total + candidates[j] > target:
                    break
                # choice: include candidates[j] in our curr comb sum
                curr.append(candidates[j])
                dfs(j + 1, curr, total + candidates[j])
                curr.pop()
            
        dfs(0, [], 0) # start all params at origin

        return res # return final list of valid combination sums

             