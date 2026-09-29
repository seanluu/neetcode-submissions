class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # base case: if num of open == total of pairs == num of closed, stop and add to the stack
        # choices: either add more open brackets or closed brackets to get pairs
        # constraints: 
        # backtracking step: pop the last added element to the curr path
        
        stack = []

        res = []

        def dfs(openN, closedN):
            if openN == n == closedN: # base case
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0)

        return res