class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # use a hashmap for fast lookup of target and diff
        
        for i, n in enumerate(nums):
                diff = target - n
                if diff in seen:
                    return [seen[diff], i]
                else:
                    seen[n] = i
        return

        