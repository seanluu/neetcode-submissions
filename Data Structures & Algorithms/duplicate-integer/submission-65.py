class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupe = set() # avoid duplicates by using a hashset

        for num in nums:
            if num in dupe:
                return True
            else:
                dupe.add(num) # add num to set for further consideration in future
        return False