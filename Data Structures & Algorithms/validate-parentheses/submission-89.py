class Solution:
    def isValid(self, s: str) -> bool:

        stack = []  # openers waiting to be closed

        closeToOpen = { '}' : '{', ')' : '(', ']' : '[' }  # closer -> its opener

        for c in s:
            # closing bracket
            if c in closeToOpen:
                # top must be its matching opener, so pop the pair
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # wrong opener on top, or nothing to close
                else:
                    return False
            # opening bracket, wait for its closer
            else:
                stack.append(c)

        return not stack  # valid only if every opener got closed