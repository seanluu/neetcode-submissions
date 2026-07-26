class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Base case:
        # unique chosen numbers sum to target

        # Choices:
        # include nums[i] in our combination sum (can also use unlimited number of times)
        # exclude nums[i] in our combination sum

        # Constraints:
        # - if combination of nums chosen > target, then not accepted
        # - i must stay within bounds of the array

        # Backtracking step:
        # pop the last number added to try a different number

        res = []

        # since we know that we care about the combination of nums chosen integer
        # shouldn't be greater than the target number, we need to consider that
        # therefore, we include a total in our DFS

        # since we also care that the index must stay within bounds of the array otherwise
        # it wouldn't work, therefore we include i as a parameter for DFS as well

        # we always care about the current path hence why it is also included in dfs

        # index, current element, total
        def dfs(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return


            # choice #1: include nums[i] in comb sum (unlimited or regular)
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop() # backtracking step

            # choice #2
            # by doing i + 1, we skip choice #1 by excluding nums[i] in comb sum
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
    
        return res