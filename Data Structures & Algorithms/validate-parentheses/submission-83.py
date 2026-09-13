class Solution:
    def isValid(self, s: str) -> bool:

        # use a stack here since we want to pop whenever we have a match

        stack = []

        # map each closing parenthesis to their respective opening parenthesis
        closeToOpen = { ']' : '[', ')' : '(', '}' : '{'}

        # iterate through each char in the string s
        for c in s:
            if c in closeToOpen: # if that char is found in closeToOpen
                if stack and stack[-1] == closeToOpen[c]: # stack isn't empty, and the top of
                # the stack (which is always an opening bracket) matches the opener
                # that corresponds to this closing bracket c
                    stack.pop() # pop from the stack since we have a matching pair
                else:
                    return False # otherwise, we have a mismatch or no open bracket
            else:
                stack.append(c) # c is an open bracket, push so we can consider for future iterations
        return True if not stack else False # ret True only if every open bracket got matched

        # time complexity: O(n)
        # iterate through each char in the string s at least once

        # space complexity: O(n)
        # worst case is that every char gets pushed onto the stack