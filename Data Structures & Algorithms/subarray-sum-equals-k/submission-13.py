class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0

        currSum = 0

        prefixSum = {0 : 1} # return 0 by default if not do 1

        for num in nums:
            currSum += num # add current number to the current sum we have
            diff = currSum - k # calculate how much we can cut off from the start
            res += prefixSum.get(diff, 0)  # each earlier prefix equal to diff can be cut off to leave a subarray summing to k
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0) # record this prefix sum so later indices can cut it off

        return res