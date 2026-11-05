class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 # output

        prefixSum = {0 : 1}

        currSum = 0 # current sum

        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return res

