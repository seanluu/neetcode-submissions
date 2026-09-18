class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case: len(perm) == len(nums), every num placed
        # choices: any unused index, any call — order matters so no "forward only"
        # constraints: pick[i] tracks used, since depth alone can't tell us anymore
        # backtracking step: pop perm AND reset pick[i] = False (two things mutated)
        
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False
            

        