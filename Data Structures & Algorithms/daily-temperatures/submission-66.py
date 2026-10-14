class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # (temp, index)

        res = len(temperatures) * [0]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:  # today is warmer than the most recent waiting day's temp
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res