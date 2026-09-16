class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # hashmaps to keep track of frequency for each char in the strings s, t
        anagramS, anagramT = {}, {}

        for i in range(len(s)):
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0) # 0 if the char doesn't exist yet
            anagramT[t[i]] = 1 + anagramT.get(t[i], 0)
        
        return anagramS == anagramT # compare the count of each char to each other
        # helps us check if the two strings are anagrams to each other