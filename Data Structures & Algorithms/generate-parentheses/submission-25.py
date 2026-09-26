class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []

        res = []

        def dfs(openN, closedN):
            if openN == n == closedN:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                dfs(openN + 1, closedN)
                stack.pop()

            if openN > closedN:
                stack.append(')')
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0)

        return res