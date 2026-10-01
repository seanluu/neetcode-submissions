class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Kadane's algorithm:
        # if the running sum becomes negative, keeping it will only reduce the sum
        # of any future subarray
        
        # first element (to handle all negative arrays)
        # 0 to track the running subarray sum
        maxSum, currSum = nums[0], 0

        for num in nums:
            # greedy rule: if current sum is negative, we reset the amount to 0
            # because everytime we saw a negative, it wouldn't make sense to continue with that subarray
            # and it's smarter to just skip it and start fresh with a new subarray
            if currSum < 0:
                currSum = 0
            currSum += num # we add the curr number to the currSum
            maxSum = max(maxSum, currSum) # update maxSum with the max between maxSub 
        return maxSum