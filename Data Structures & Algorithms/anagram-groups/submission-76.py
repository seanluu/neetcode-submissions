class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create an empty list if the group anagram doesn't exist already

        # iterate through each string
        for s in strs:
            groupS = "".join(sorted(s)) # sort every string in alphabetical order
            res[groupS].append(s) # add each string to their respective group anagram
        return list(res.values()) # return all group anagrams in list format

        # tc: O(n * k log k), n = number of strings, k = max string length
        # sc: O(n * k) for the hashmap keys and grouped strings