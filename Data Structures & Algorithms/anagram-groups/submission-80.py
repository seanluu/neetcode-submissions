class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create an empty list if the group anagram list doesn't exist already

        # iterate through each individual string once
        for s in strs:
            groupS = "".join(sorted(s)) # sort this string's chars; anagrams share the same key
            res[groupS].append(s) # add each string to their respective group anagram
        return list(res.values()) # return in list format

        # tc: O(n * k log k)
        # sorting each of the n strings, each up to length k

        # sc: O(n * k)
        # hashmap stores every string plus its sorted key