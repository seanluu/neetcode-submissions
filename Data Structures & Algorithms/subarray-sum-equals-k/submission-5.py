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

        prefixSum = {0: 1}  # running sum of 0 seen once (empty front),
        # so subarrays starting at index 0 get counted

        for num in nums:
            currSum += num # running total up to here
            diff = currSum - k  # like two sum: the earlier running sum we'd chop off
                                # to leave exactly k (diff + k = currSum)
            res += prefixSum.get(diff, 0)  # add how many times we've seen diff (0 if never);
                                           # each one is a different subarray ending here
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0) # record this sum for future indices
        return res

        # tc: O(n), one pass
        # sc: O(n), hashmap of running sums