class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            group = "".join(sorted(s))
            res[group].append(s)
        return list(res.values())