class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sort duplicates so we can avoid reusing them in combinations
        candidates.sort()

        res = []

        def dfs(i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())
                return

            # constraints
            if total > target or i >= len(candidates):
                return

            # choice #1: include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            # choice #2: exclude candidates[i]
            # while there's a next element (i + 1 bounds check) and it's the same value as candidates[i], it's a duplicate, so step past it; in the exclude branch we skip every copy so we don't rebuild a combination we already made
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total) # continue with choice #2

        dfs(0, [], 0)

        return res