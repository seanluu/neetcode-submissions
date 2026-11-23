class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # we know that this is backtracking because we want to return all well-formed
        # parenthesis strings that we can generate with n pairs of parentheses
        # (big emphasis on the ALL well-formed)
        
        res = []

        stack = []

        def dfs(openN, closedN):
            # add built string to the result once we have an equal amount of open and closed parentheses
            # string is complete and valid only under this condition
            if openN == n == closedN:
                res.append("".join(stack))
                return

            # add '(' only if we still have openings left
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN) # backtrack after each choice
                stack.pop()

            # add ')' only if it doesnt break validity
            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1) # backtrack after each choice
                stack.pop()

        dfs(0, 0) # start at origin for both openN and closedN

        return res