class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = "" # empty string

        for i in range(len(strs[0])):
            for s in strs:
                # strs[0] is the first string in the list, e.g. "flower"
                # strs[0][i] is the character at position i in that string, e.g. "flower"[2] == "o"
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res