class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = { ']' : '[', '}' : '{', ')' : '(' }

        # iterate through each char in the string s
        for c in s:
            # if the char happens to be a closed bracket in closeToOpen
            if c in closeToOpen:
                # closer must match the most recent unmatched opener
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # pop since we have a matching pair
                else:
                    return False # otherwise we ran into a mismatch
            else:
                stack.append(c) # add the char to the stack to be considered for later pairs
        return True if not stack else False