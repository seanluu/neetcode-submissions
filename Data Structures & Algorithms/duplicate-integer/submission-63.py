class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupe = set()

        for num in nums:
            if num in dupe:
                return True
            else:
                dupe.add(num)
        return False