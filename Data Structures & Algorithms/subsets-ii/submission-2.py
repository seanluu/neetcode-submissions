class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # base case: if i >= len(nums)
        # choices: either include nums[i] in our subset or exclude it
        # constraints: i cannot go out of bounds; when excluding nums[i], must also
            # skip any immediate duplicates of nums[i] to avoid generating the same
            # subset twice (relies on nums being sorted first)
        # backtracking step: pop the last added element to the curr path
        
        nums.sort() # sort in numerical order to handle deduplicates

        res = [] # since output is an array

        def dfs(i, curr):
            if i >= len(nums): # base case
                res.append(curr.copy())
                return

            # choice #1: include nums[i] in our subset
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            # choice #2: exclude nums[i] — but if nums[i] has duplicates right after it,
            # skip past ALL of them too before recursing. Otherwise, "exclude nums[i],
            # then separately include the next identical value" would recreate a subset
            # already reachable by including THIS nums[i] instead
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: # using this loop avoids all duplicates in our subsets
                i += 1
            dfs(i + 1, curr) 
        
        dfs(0, []) # set to origin

        return res

        # time complexity: O(n * 2^n)
        # worst case (no actual duplicates present): same 2^n leaves as plain subsets,
        # each needing O(n) to copy into res. The while-loop skip adds at most O(n)
        # total across the whole run (each index only ever gets fast-forwarded past
        # once), so it doesn't change the dominant term

        # space complexity: O(n) extra (recursion depth + curr), O(2^n) for res itself