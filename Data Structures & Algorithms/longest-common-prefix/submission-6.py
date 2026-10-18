class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # check if i is out of bounds, if it isn't then make sure
                # s[i] (char at index i of s) matches
                # strs[0][i] (char at index i of the first string)
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i] # every string matched at i, so add that char to the prefix
        return res
