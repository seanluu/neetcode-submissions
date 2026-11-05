class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0  # number of subarrays that sum to k

        prefixSum = {0: 1}  # prefix sum -> how many times we've seen it; 0 seeded for subarrays starting at index 0

        currSum = 0  # running sum of nums[0..i]

        for num in nums:
            currSum += num
            diff = currSum - k  # an earlier prefix with this sum means the subarray after it sums to k
            res += prefixSum.get(diff, 0)  # each earlier prefix equal to diff ends one valid subarray here
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)  # record this prefix sum for later indices

        return res