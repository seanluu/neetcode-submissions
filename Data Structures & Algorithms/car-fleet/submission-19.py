class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Input: target = 10, position = [1,4], speed = [3,2]
        # Output: 1

        # car starting at 1 (speed of 3) will eventually become a fleet
        # with the car starting at 4 (speed of 2), since they both meet at the
        # target 10 at the same time as each other

        # since 1 + 3 + 3 + 3 = 10
        # 4 + 2 + 2 + 2 = 10

        # 10 - 1 = 9 / 3 = 3
        # time = (target - position) / speed

        pair = [[p, s] for p, s in zip(position, speed)]

        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
