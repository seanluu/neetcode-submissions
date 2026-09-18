class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort() # handle dedup so we can skip and avoid dupe combinations

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(candidates):
                return

            # choices: try every candidate from i onward, we don't pick one, so loop goes to j + 1
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                
                curr.append(candidates[j])
                dfs(j + 1, curr, total + candidates[j])
                curr.pop()
        
        dfs(0, [], 0)

        return res