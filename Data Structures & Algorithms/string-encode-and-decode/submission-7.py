class Solution:

    def encode(self, strs: List[str]) -> str:
        # format each string as "length#string", e.g. ["hi","abc"] -> "2#hi3#abc"
        # the length tells decode exactly how many chars to read, so strings
        # can contain "#" or digits without breaking anything
        res = []  # collect pieces, join once at the end (faster than +=)

        for s in strs:
            res.append(str(len(s)))  # length of the string
            res.append("#")          # delimiter marks where the length ends
            res.append(s)            # the string itself
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # start of the current "length#string" chunk

        while i < len(s):
            # find the "#" that ends the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # digits between i and "#"

            i = j + 1             # string starts right after "#"
            j = i + length        # and ends length chars later
            res.append(s[i:j])

            i = j                 # move to the next chunk
        return res

        # tc: O(n) for both, n = total chars across all strings
        # sc: O(n) for the encoded string / output list