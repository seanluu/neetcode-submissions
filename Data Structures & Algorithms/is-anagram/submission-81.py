class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        # hashmaps so we can keep track of frequency of each char
        # for each of the two strings, s and t
        anagramS, anagramT = {}, {}

        for i in range(len(s)):
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0)
            anagramT[t[i]] = 1 + anagramT.get(t[i], 0)
        
        return anagramS == anagramT

        # check if both anagrams are the same length as each other