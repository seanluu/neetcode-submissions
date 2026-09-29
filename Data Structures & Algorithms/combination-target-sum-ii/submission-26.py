class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # base case: if total == target, stop
        # choices: include candidates[i] or exclude candidates[i] from
        # our current combination sum
        # constraints: if i >= len(candidates) or if total > target
        # backtracking step: pop the last added element to the curr path

        candidates.sort() # use sort to get rid of deduplicates
        
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res



