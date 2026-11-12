class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            groupS = "".join(sorted(s)) # sort the chars of the strings to be in alphabetical order
            res[groupS].append(s) # add each string to their respective group in groupS (inside the res array)
        return list(res.values()) # return all group anagrams in list format