class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # return the total number of subarrays whose sum equals to k
        
        # subarray -> contiguous non-empty sequence of elements within an array

        # Input: nums = [2,-1,1,2], k = 2
        # Output: 4

        # since we could do
        # [2] as one array
        # [2 - 1 + 1] = 2 as one array
        # [-1 + 1 + 2] = 2 as one array
        # [2] again as one array

        # prefix sum: the sum of any subarray = prefix_now - prefix_earlier,
        # so we reuse past running totals instead of re-adding every subarray

        res = 0

        currSum = 0

        prefixSum = { 0 : 1 } # if not 0, then we use 1
        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res
            