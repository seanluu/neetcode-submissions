class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create a new group anagram if it hasn't been seen before
        
        for s in strs: # iterate through each individual string
            sortedS = ''.join(sorted(s)) # join words together and sort them in alphabetical order
            # so cat -> act, cab -> abc, etc...
            res[sortedS].append(s) # add those words to their respective group anagrams
        return list(res.values()) # return the final list of all group anagrams in list format

        # time complexity: O(n * k log k)
        # n = number of strings
        # k = maximum length of a string
        # each string is sorted, which takes O(k log k)

        # space complexity: O(n * k)
        # the dictionary stores every string and uses each sorted string
        # (length k) as a key