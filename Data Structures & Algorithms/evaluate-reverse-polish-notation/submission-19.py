class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Input: tokens = ["1","2","+","3","*","4","-"]
        # Output: 5
        # Explanation: ((1 + 2) * 3) - 4 = 5

        # we use a stack here because if we see a '+'
        # then that means we apply a certain condition to the
        # rest of the array

        # we'll pop for whenever we see a '-' since we want
        # to remove from the stack

        # append for whenever we see an '+' to add to the stack

        stack = []

        res = 0

        # for every char in tokens:
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a) # order matters here
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
