class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 # output

        currSum = 0 # keep track of the current subarray sum

        prefixSum = {0 : 1}

        for num in nums:
            currSum += num # add curr number to our current sum
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return res