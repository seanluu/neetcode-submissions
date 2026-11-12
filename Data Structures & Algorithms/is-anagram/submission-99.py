class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        anagramS, anagramT = {}, {}

        for i in range(len(s)):
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0) # add 1 when we see s[i], 0 by def if s[i] hasn't been seen before?
            anagramT[t[i]] = 1 + anagramT.get(t[i], 0) # add 1 when we see t[i], 0 by def if t[i] hasn't been seen before?

        return anagramS == anagramT # compare char freq for each string1 and string2