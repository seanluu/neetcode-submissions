class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # use hashmaps to track frequency for each string

        anagramS, anagramT = {}, {}
        
        for i in range(len(s)):
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0)
            anagramT[t[i]] = 1 + anagramT.get(t[i], 0)

        return anagramS == anagramT