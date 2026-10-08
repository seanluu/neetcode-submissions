class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create an empty list if the group anagram doesn't exist already

        # iterate through each individual string once
        for s in strs:
            groupS = "".join(sorted(s)) # anagrams have the same letters, so sorting gives them the same key
            # e.g. "eat", "tea", "ate" all become "aet"
            res[groupS].append(s) # add each string to their respective group anagram
        return list(res.values()) # return final list of all group anagrams
