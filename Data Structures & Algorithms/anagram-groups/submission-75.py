class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create an empty list by default if group anagram doesn't exist
        # already

        for s in strs:
            groupS = "".join(sorted(s))
            res[groupS].append(s)
        return list(res.values())