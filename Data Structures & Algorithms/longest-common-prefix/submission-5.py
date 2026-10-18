class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # return the longest common prefix of all the strings

        res = "" # return an empty string if there's no longest common prefix

        # first string at index 0, arbitrary, since it's possible
        # that this string is not the shortest string in the input
        # so we stop the for loop earlier
        for i in range(len(strs[0])):
            # iterate through every string
            for s in strs:
                # need to check that i is in bounds
                # (i == len(s))
                # check that every string at index i is the same
                # compare to the first character of the first string
                # (s[i] != strs[0][i])
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res