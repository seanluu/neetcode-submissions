class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = "" # empty string

        for i in range(len(strs[0])):
            for s in strs:
                # index, val
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res