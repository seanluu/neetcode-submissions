class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotonic stack: holds days still waiting for a warmer day,
        # with temps decreasing from bottom to top
        # (anything warmer than the top gets popped right away)

        stack = []  # pairs of [temp, index]

        # 0 by default, since the problem wants 0 if there's no warmer day later
        res = [0] * len(temperatures)

        # iterate through each index and temperature once
        for i, t in enumerate(temperatures):
            # today is warmer than the day on top of the stack,
            # so today is that day's next warmer day
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd  # days waited = today's index - that day's index

            # today now waits for its own warmer day
            # (temp is for comparing, index is for counting days)
            stack.append([t, i])

        return res  # days still in the stack never found a warmer day, so they stay 0

        # time: O(n), each day is pushed and popped at most once
        # space: O(n), the stack can hold every day (e.g. temps always decreasing)