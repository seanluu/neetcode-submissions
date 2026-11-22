class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # base case: if total == target
        # choices: include candidates[i] in our comb sum or exclude it
        # constraints: total can't be greater than target, i cannot be out of bounds
        # backtracking step: pop the last added element to the curr path
        
        # use sort so dupe values are next to each other and we handle deduplicates since we want to choose an element from candidates at most once within a combination, no dupe combinations
        candidates.sort()

        res = []

        def dfs(i, curr, total):
            # base case: if total == target, we found a valid curr path that sum to our target
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
            # skip every copy of this value (sorted, so copies sit next to each other),
            # otherwise picking a later copy would rebuild a combination we already made

            # very similar logic to 3sum and how we handle duplicates in our triplets (except we use i + 1 instead of i - 1)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res