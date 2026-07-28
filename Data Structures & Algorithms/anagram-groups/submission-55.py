class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # use a hashmap here 
        res = defaultdict(list) # return a empty list by default if the group anagram doesn't exist yet

        for s in strs: # iterate through each string in strs
            anagramS = ''.join(sorted(s)) # for each anagram string, join everything together by getting rid of spaces
            # while also sorting them in alphabetical order 
            # so "cab" becomes "abc"
            res[anagramS].append(s) # add each individual string to their respective group anagram
        return list(res.values()) # return the final list of all unique group anagrams

        # time complexity: O(n * k log k)
        # n = number of strings, k = max string length
        # we sort each string (k log k), once per string (n total)

        # space complexity: O(n * k)
        # we store every string (and its sorted key) across all groups