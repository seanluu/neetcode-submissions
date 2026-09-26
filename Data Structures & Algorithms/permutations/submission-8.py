class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]] # base case: one permutation of nothing — seed to build outward from

        # process one number from nums at a time, growing perms with each pass
        for n in nums:
            # this pass's permutations get built fresh, then replace perms entirely
            newPerms = []
            for p in perms: # every permutation built from numbers seen so far
                for i in range(len(p) + 1): # every valid slot to insert n into
                    p_copy = p.copy() # O(len(p)) — this + insert is where the
                                       # extra "n" factor in O(n*n!) comes from
                    p_copy.insert(i, n)
                    newPerms.append(p_copy)
            perms = newPerms # swap in this round's permutations for the next pass

        return perms

        # time: O(n * n!) — same reasoning as the recursive version:
        # n! total permutations, each needing O(n) to copy + insert

        # space: better than the recursive version (only one generation alive
        # at a time, no nested call stack each holding its own perms), but
        # still not O(n) — perms itself holds up to n! full lists at the end