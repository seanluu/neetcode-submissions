class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # use a hashset since that elims dupes

        dupe = set()
        
        for num in nums:
            if num in dupe:
                return True
            else:
                dupe.add(num)
        return False