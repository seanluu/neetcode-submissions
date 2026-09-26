class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]] # base case

        # compute subproblems

        for n in nums:
            # now add n to every existing permutation is the logic
            newPerms = []
            # iterate through each permutation once
            for p in perms:
                # insert n into each perm
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    newPerms.append(p_copy)
            perms = newPerms
        return perms

