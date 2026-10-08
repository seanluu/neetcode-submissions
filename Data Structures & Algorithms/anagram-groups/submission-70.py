class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # creates an empty list if group anagram doesn't exist already

        for s in strs:
            groupA = "".join(sorted(s))
            res[groupA].append(s)
        return list(res.values())