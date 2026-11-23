class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    # trie (prefix tree): each level is the next letter, and words that start the same
    # share that path until they differ; word marks where a full word stops

    # example...

    # if we have "bad", "bat", "bag"

    # root
    # -> b
    #     -> a
    #         -> d (end)
    #         -> t (end)
    #         -> g (end)
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root # start at the root
        # iterate through each char in the word
        for c in word:
            i = ord(c) - ord("a") # letter -> index ('a' -> 0, 'b' -> 1, ...)
            if curr.children[i] == None: # no child for this letter yet
                curr.children[i] = TrieNode()  # create a node for this letter
            curr = curr.children[i] # move down to that letter's node
        curr.endOfWord = True # mark the end of a full word

    def search(self, word: str) -> bool:
        curr = self.root # start at the root
        # iterate through each char in the word
        for c in word: 
            i = ord(c) - ord("a") # letter -> index ('a' -> 0, 'b' -> 1, ...)
            # if there are currently no children
            if curr.children[i] == None: # letter missing, so the word isn't in the trie
                return False
            curr = curr.children[i] # move down to that letter's node
        return curr.endOfWord # path exists, but only True if a word ends here

    def startsWith(self, prefix: str) -> bool:
        curr = self.root # start at the root
        # iterate through each char in the prefix
        for c in prefix:
            i = ord(c) - ord("a") # letter -> index ('a' -> 0, 'b' -> 1, ...)
            if curr.children[i] == None: # letter missing, so no word starts with this prefix
                return False
            curr = curr.children[i] # move down to that letter's node
        return True # path exists, so some word starts with this prefix