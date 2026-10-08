class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            groupS = "".join(sorted(s))
            res[groupS].append(s)
        return list(res.values())