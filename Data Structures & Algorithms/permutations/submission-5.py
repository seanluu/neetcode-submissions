class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # base case: empty input has exactly one permutation — the empty arrangement.
        # this is the seed that every insertion builds outward from.
        if len(nums) == 0:
            return [[]]

        # recursively get all permutations of everything EXCEPT the first number.
        # this is where (n-1)! permutations get generated one level down.
        perms = self.permute(nums[1:])
        res = []

        # for each smaller permutation, insert nums[0] into every possible position
        for p in perms:
            # len(p) + 1 valid insertion slots — includes both ends
            # (e.g. inserting into [2,3] can go before 2, between 2 and 3, or after 3)
            for i in range(len(p) + 1): 
                p_copy = p.copy() # O(len(p)) copy — this is where the extra "n" factor
                                   # in O(n * n!) time comes from: n! permutations,
                                   # each needing an O(n) copy+insert
                p_copy.insert(i, nums[0]) # O(len(p)) insert — shifts elements after position i
                res.append(p_copy)

        return res

        # time: O(n * n!) — n! total permutations produced, each costing O(n)
        # to copy + insert into

        # space: NOT O(n) — unlike the backtracking/used[] version, this keeps
        # entire generations of permutations alive simultaneously at every
        # recursion level (perms holds (n-1)! full lists at once), so this
        # uses meaningfully more than O(n) auxiliary space