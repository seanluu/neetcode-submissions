class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [] # we want to return a final list of all subsets eventually
        subset = [] # curr subset being built

        def backtrack(i): # i is the curr index in nums we're making a decision for

            # base case: we considered all elements, so save snapshot of curr subset
            if i >= len(nums): # if index is geq to length of the list
                res.append(subset.copy()) # save the current subset
                # if we didn't make a copy, we would end up with a res list
                # full of empty or incorrect subsets
                return

            # decision 1: include nums[i]
            subset.append(nums[i]) # we decide to include the curr element at index i in our subset
            backtrack(i + 1) # move to the next element to make the next decision
            subset.pop() # backtrack

            # decision 2: skip nums[i]
            backtrack(i + 1)

        # start recursion from the first element
        backtrack(0)

        # return list of all subsets
        return res

        # time complexity: O(n * (2^n))
        # since we iterate through every num -> O(n)
        # there are 2^n subsets, so creating a copy of subset takes O(n) worst case

        # space complexity: O(n)
        # worst case scenario, we store every unique subset in the res array
