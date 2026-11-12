class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = "" # empty string

        # iterate through the length of the first string in strs
        for i in range(len(strs[0])):
            for s in strs: # iterate through each string in strings
                if i == len(s) or s[i] != strs[0][i]: # this row is too short or doesn't match row 0 in column i
                    return res 
            res += strs[0][i] # every row matched in column i, so add that char to res
        return res