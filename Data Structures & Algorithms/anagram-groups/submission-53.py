class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        # use defaultdict because we want to create a new list
        # whenever we haven't seen a list for the certain
        # group anagram we're on

        for s in strs:
            anagramS = ''.join(sorted(s))
            res[anagramS].append(s)
        return list(res.values())