class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # base case: openN == n and closedN == n — used up both budgets, string complete
        # choices: add '(' if opens remain (openN < n); add ')' if it keeps prefix valid (openN > closedN)
        # constraints: openN < n caps total opens at n; openN > closedN stops closes from ever outnumbering opens
        # backtracking step: pop the last added element so other choices can be explored

        stack = [] # stack is necessary here since we want to pop whenever we have
        # a open and closed bracket to pair together, very similar to Valid Parenthesis
        res = []

        # store either of opening or closed bracket
        def dfs(openN, closedN):
            if openN == n == closedN: # base case: exactly n opens AND n closes placed — string complete
                res.append("".join(stack)) # add finished string to res
                return
            
            # choice #1: add opening bracket at each step
            # if we haven’t used all n opening brackets yet, we can choose to add another '('
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

            # choice #2: add closing bracket — only if there's an unmatched '(' to close
            # (openN > closedN), not a budget check — this is what keeps the prefix valid
            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0) # start at origin for both opening and closing brackets
        return res # return final list of well-formed parenthesis strings