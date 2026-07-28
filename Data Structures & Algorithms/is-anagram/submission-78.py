class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): # edge case where we can auto elim strings that aren't equiv to each other
            return False

        anagramS, anagramT = {}, {} # hashmap for each string to map char : count

        for i in range(len(s)): # iterate through each letter of the string once
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0) # for every time the char occurs in string S, 
            # increment count if the letter hasn't occurred before, the default value should be a 0
            anagramT[t[i]] = 1 + anagramT.get(t[i], 0) # for every time the char occurs in string T

        return anagramS == anagramT # compare the strings against each other

        # time complexity: O(n)
        # iterate through each string once

        # space complexity: O(1)
        # we use a hashmap to quickly attach letter to count, which is constant time O(1)
