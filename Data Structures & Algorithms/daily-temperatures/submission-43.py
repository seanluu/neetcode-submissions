class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # use a monotonic stack here

        # monotonic stack is a stack that is strictly increasing or
        # strictly decreasing order at all times

        # in this case, it is strictly increasing since we want to find the next
        # day with a higher temperature

        res = [0] * len(temperatures)
        # fill array with all 0s by default

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # while stack is non-empty and
            # the current temp is warmer than the temp on top of the stack
            # (stack holds temps in decreasing order, bottom to top)
            # t (current temperature) > stack[-1][0] (temperature at top of stack, aka latest temperature added)
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

        # time complexity: O(n)
        # each index is pushed once and popped at most once, so total
        # work across the whole run is O(n), not O(n) per iteration

        # space complexity: O(n)
        # worst case is a strictly decreasing sequence (e.g. [4,3,2,1]) —
        # nothing ever gets popped, so every index stays on the stack
