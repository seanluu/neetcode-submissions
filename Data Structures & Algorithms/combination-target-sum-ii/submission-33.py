class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # base case: if index is greater than or equal to the number of candidates total (i >= len(nums))
        # choices: include candidates[i] or exclude it from our combination sum
        # constraints: total is bigger than the target, or i goes out of bounds
        # backtracking step: pop the last added element from the curr path

        candidates.sort()

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