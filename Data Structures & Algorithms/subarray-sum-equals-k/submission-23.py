class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Input: nums = [2,-1,1,2], k = 2
        # Output: 4

        # 2 by itself is 1 subarray
        # since 2 + (-1) + 1 + 2 = 2 is 1 subarray
        # -1 + 1 + 2 is 1 subarray
        # 2 by itself is 1 subarray
        # therefore, out total is 4 since we have 4 possible subarrays

        # total number of subarrays whose equals to k
        
        res = 0

        prefixSum = {0 : 1}

        currSum = 0

        for num in nums: 
            currSum += num # add current number to the current sum that we have total
            diff = currSum - k # calculate how much prefix sum we can cut off and still get a subarray
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return res