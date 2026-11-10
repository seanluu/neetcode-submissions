class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # stop if this row is too short to reach column i,
                # or its char at column i doesn't match row 0's
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
