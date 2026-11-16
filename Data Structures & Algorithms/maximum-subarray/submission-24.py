class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # default is only num in array
        maxSum, currSum = nums[0], 0

        # iterate through each num
        for num in nums:
            # greedy rule: if curr sum is negative, reset it
            if currSum < 0: 
                currSum = 0 # set curr sum to 0
            currSum += num # otherwise, add the curr num to the sum after we've reset
            maxSum = max(maxSum, currSum) # take best option between the two
        return maxSum

        # tc: O(n)
        # iterate through each num once

        # sc: O(1)
        # no crazy data structures used