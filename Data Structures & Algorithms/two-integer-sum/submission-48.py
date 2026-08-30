class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # use a hashmap for fast lookup of target and diff
        
        for i, n in enumerate(nums):
                diff = target - n # calc diff aka second num we add to get the target
                if diff in seen:
                    return [seen[diff], i] # return index of prev seen number and the current index
                else:
                    seen[n] = i # otherwise, store the curr num and its index to be used later
        return

