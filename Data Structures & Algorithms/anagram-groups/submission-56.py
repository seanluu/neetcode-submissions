class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            anagramS = ''.join(sorted(s))
            res[anagramS].append(s)
        return list(res.values())
