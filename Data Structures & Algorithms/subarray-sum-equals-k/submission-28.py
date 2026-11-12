class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0

        prefixSum = {0 : 1}

        currSum = 0

        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
            # LHS stores the new count back in the dictionary under the key currSum. 
            # If the key didn’t exist, it gets created. If it did, the old value gets overwritten
            # RHS looks up the key currSum in the dictionary. 
            # if it’s there, you get its count. If not, you get 0.

        return res