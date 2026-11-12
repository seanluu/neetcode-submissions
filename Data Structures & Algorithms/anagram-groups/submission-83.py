class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # sorted string -> list of its anagrams; missing keys start as []

        for s in strs:
            groupS = "".join(sorted(s)) # sort the chars alphabetically; anagrams end up with the same key
            res[groupS].append(s) # add s to the group under its key
        return list(res.values()) # return just the groups, as a list of lists

        # tc: O(n * k log k), sorting each of n strings of length up to k
        # sc: O(n * k), storing every string plus its key