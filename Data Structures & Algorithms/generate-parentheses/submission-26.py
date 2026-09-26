class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = [] # we use a stack here because we pop the top whenever we have a matching pair

        res = [] # since we want to return an array

        def dfs(openN, closedN):
            if openN == n == closedN: # exactly n opens AND n closes placed — string complete
                res.append("".join(stack)) 
                return

            if openN < n: # supply check — n pairs total, so cap opens at n
                stack.append('(')
                dfs(openN + 1, closedN)
                stack.pop()

            if openN > closedN: # validity check — only close if there's an
                                  # unmatched '(' waiting (prevents invalid prefixes)
                stack.append(')')
                dfs(openN, closedN + 1)
                stack.pop()

        dfs(0, 0) # start at origin

        return res # return final list of generated parenthesis