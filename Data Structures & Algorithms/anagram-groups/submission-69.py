class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key = sorted version of a string, value = list of strings in that group
        # defaultdict(list) creates an empty list automatically for a new key
        res = defaultdict(list)

        # iterate through each string once
        for s in strs:
            # anagrams have the same letters, so sorting gives them the same key
            # e.g. "eat", "tea", "ate" all become "aet"
            groupS = "".join(sorted(s))
            res[groupS].append(s)  # add the string to its anagram group

        return list(res.values())  # each value is one group of anagrams

        # time complexity: O(n * k log k)
        # we go through n strings, and sorting each one costs k log k

        # space complexity: O(n * k)
        # n = num of strings, k = max len of a string