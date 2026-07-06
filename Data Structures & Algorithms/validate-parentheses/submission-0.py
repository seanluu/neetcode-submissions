class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # since we need to pop whenever we have matching parenthesis

        closeToOpen = { ']' : '[', '}' : '{', ')' : '('}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False