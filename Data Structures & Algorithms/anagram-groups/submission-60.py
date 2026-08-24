class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # create a list automatically if none
        # exists for the group anagram we want already

        for s in strs:
            anagramS = ''.join(sorted(s)) # arrange chars in string to be alphabetical order, so 'cat' -> 'act' which helps us create group anagrams
            res[anagramS].append(s) # add every string that we sorted to their
            # respective group anagram
        return list(res.values()) # list all strings in each group anagram