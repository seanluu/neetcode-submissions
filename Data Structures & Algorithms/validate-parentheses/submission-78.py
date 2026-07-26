class Solution:
    def isValid(self, s: str) -> bool:

        # s only consists of 6 bracket chars: (), {}, []
        # two types of stack problems:

        # 1 -> we pop if we have a matching pair for this problem, which we use here
        # 2 -> we pop only if we have a certain constraint fulfilled
        
        stack = [] # holds open brackets we haven't matched yet

        closeToOpen = { ')' : '(', ']' : '[', '}' : '{'}

        for c in s: # iterate through each char in the string s
            if c in closeToOpen: # if char is a closing bracket
                if stack and stack[-1] == closeToOpen[c]: # if top of stack is the matching open element
                    stack.pop() # we have a matching pair, so we remove it from the stack
                else:
                    return False # otherwise, we have a mismatch or no open bracket to match against
            else:
                stack.append(c) # c is an open bracket, push to be considered for future iterations
        return True if not stack else False # return True only if every open bracket got matched

        # time complexity: O(n)
        # iterate through each char in the string s exactly once

        # space complexity: O(n)
        # worst case (e.g. all open brackets), every char gets pushed onto the stack