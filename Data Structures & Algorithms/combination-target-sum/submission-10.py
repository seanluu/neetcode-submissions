class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Input:
        # nums = [2,5,6,9]
        # target = 9
        # Output: [[2,2,5],[9]]

        # since we use 2 + 2 + 5 = 9, using 2 twie and 5 once
        # and then 9 = 9, so we use 9 once

        # for case 1, we used 2 twice which is us using it
        # an unlimited number of times

        # Base case: 
        # current combination of nums sum to target
        # stop if the num is greater than the target amount

        # Constraints: 
        # i must stay within bounds of the array and stop if
        # sum if greater than the target

        # Choices: 
        # include nums[i] in our combination sum 
        # or we can exclude it (we can reuse nums[i])

        # Backtracking step:
        # pop the last number added to try a different number

        res = []

        def dfs(i, curr, total): # current index
            if total == target: # save comb if total is exactly the target amount
                res.append(curr.copy())
                return
        
            if i >= len(nums) or total > target:
                # stop exploring if index is out of bounds
                # stop exploring when total sum is greater than target
                return

            # choice #1, where we include nums[i] in our comb sum
            # we can also reuse nums[i] here
            curr.append(nums[i]) # include curr element at index i in our comb sum
            dfs(i, curr, total + nums[i]) # total + nums[i] is adding the curr num to the combination sum
            curr.pop() # backtracking step

            # choice #2, where we exclude nums[i] in our comb sum
            dfs(i + 1, curr, total) # skip curr num and move to next 
            # index without changing the total
        
        dfs(0, [], 0) # start recursion from first element
        # 0 = index
        # [] = curr
        # 0 = total, no indexes implies no sum to go off of

        return res
    


