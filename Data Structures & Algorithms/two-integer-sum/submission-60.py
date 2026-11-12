class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i] # return the index of diff, and current index
            else:
                seen[n] = i # save n so a later num can pair with it