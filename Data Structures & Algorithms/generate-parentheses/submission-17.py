class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # base case: if we complete a parenthesis, add it to the results array
        # choices: only add ( if we have openings left, only add ) if it keeps the sequence valid
        # constraints: add ( or ) at eac step
        # backtracking step: pop the last added element to the pair so other choices can be explored
        
        stack = [] # stack is necessary here since we want to pop whenever we have
        # a open and closed bracket to pair together, very similar to Valid Parenthesis
        res = []

        # store either of opening or closed bracket
        def dfs(openN, closedN):
            if openN == n == closedN: # base case: if same num of opening and closing brackets, add to stack
                res.append("".join(stack))
                return
            
            # choice #1: add opening bracket at each step
            # if we haven’t used all n opening brackets yet, we can choose to add another '('
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

            # choice #2: add closing bracket at each step
            # if we haven’t used all n closing brackets yet, we can choose to add another ')'
            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0) # start at origin for both opening and closing brackets
        return res # return final list of well-formed parenthesis strings