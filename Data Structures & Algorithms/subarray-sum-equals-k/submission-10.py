class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0

        currSum = 0
        
        # hashmap, base case of zero and a single prefix sum that sums to 0
        prefixSum = {0: 1}  # running sum : how many times seen

        # input: [1, -1, 1, 1, 1, 1], k = 3 -> output: 4
        # at each step, look up diff = currSum - k in prefixSum
        # e.g. currSum = 3 -> diff = 0, seen twice (start, and after [1,-1])
        #      so chopping nothing or chopping [1,-1] both leave a sum of 3
        # chop off a front piece that sums to diff, and what’s left sums to exactly k.

        # iterate through every value in the input array
        for num in nums:
            currSum += num # add num to our running sum
            diff = currSum - k # later we'll we chop off diff to get what sums to exactly k
            # ^^^ if we can remove of a prefix sum of size diff, then we can find a potential result and we could have multiple prefixSums that sum up to diff, so we take that and add to the result
            res += prefixSum.get(diff, 0) # add how many earlier front pieces summed to diff, also possible this diff does not exist in prefixSum so in that case we return a default value of 0 
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0) # increment the number of prefixSums that have the particular currSum value
        return res