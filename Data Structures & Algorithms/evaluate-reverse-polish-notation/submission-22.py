class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        # iterate through each operation in the tokens array once
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop() # can't just do any pop, needs to have some structure otherwise we would get negative numbers
                stack.append(b - a) # since we care abt order here
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a)) # convert result to an integer, also float is necessary since "Assume that division between integers always truncates toward zero"
            else: 
                stack.append(int(c)) # c is a number (not an operator)
            # — push it onto the stack, it'll be consumed later when an operator token pops it as an operand

        return stack[0] # after processing every token, this is the final result

        # time complexity: O(n)
        # iterate through each element at least once

        # space complexity: O(n)
        # since we used a stack