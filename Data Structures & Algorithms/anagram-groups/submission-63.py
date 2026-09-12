class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagram is a string that contains the exact same chars as another string

        # order of chars can be different though

        # everytime we see a new type of anagram, we want to create an empty list to fill it
        # with said different combinations of that anagram

        res = defaultdict(list) # helps with problem above

        # iterate through each individual string possible
        for s in strs:
            anagramS = ''.join(sorted(s)) # sort every string alphabetically to better group anagrams
            res[anagramS].append(s) # add each anagram to their respective group anagram
        return list(res.values()) # list all strings in each group anagram

        # time complexity: O(n k log k)
        # iterate through each string once at least (n) + sorted (k log k)
        
        # space complexity: O(n * k)
        # n = number of strings, k = max length of a string
        # we store every character of every string in res (grouped by key),
        # plus each sorted key itself is up to length k
        # so total space scales with n * k