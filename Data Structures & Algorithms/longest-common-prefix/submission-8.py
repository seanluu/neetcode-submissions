class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # check if index is out of bounds
                # or if the character at index i in string s != the character at index i in the first string of strs
                # stop if s has no index i, or the char at i in s != the char at i in strs[0]
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res