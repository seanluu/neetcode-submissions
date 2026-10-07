class Solution:
    def isValid(self, s: str) -> bool:

        # stack holds opening brackets waiting to be closed
        # the most recent opener must close first, which is why we use a stack
        stack = []

        # maps each closing bracket to its matching opener
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }

        # iterate through each char in the string s once
        for c in s:
            # c is a closing bracket
            if c in closeToOpen:
                # it closes the most recent opener, so pop the pair
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # wrong opener on top, or no opener at all
                    return False
            # c is an opening bracket, save it until its closer shows up
            else:
                stack.append(c)

        # valid only if every opener got closed
        return not stack

        # time: O(n), each char is pushed and popped at most once
        # space: O(n), the stack can hold every char in the worst case