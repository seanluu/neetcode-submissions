class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # base case: if num of open == total pairs == num of closed, join stack and add to res
        # choices: either add more open brackets or closed brackets to get pairs
        # constraints: openN < n caps total opens at n (supply limit from "n pairs");
        #              openN > closedN ensures closes never outnumber opens (keeps prefix valid)
        # backtracking step: pop the last added element to the curr path
        
        stack = []
        res = []

        def dfs(openN, closedN):
            if openN == n == closedN: # base case
                res.append("".join(stack))
                return

            # supply check: n pairs total — if fewer opens used than n, add another
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

            # validity check: if there's an unmatched '(' still open, it's safe to close it now
            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0) # start at origin for open brackets and closed brackets

        return res # return final list of valid parenthesis