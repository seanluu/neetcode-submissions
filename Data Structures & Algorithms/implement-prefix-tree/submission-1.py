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

    # relevant for this problem since we have a lot of "ay" ending words with "day", "bay", "may",
    # "say", etc

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode() # add children to the prefix tree
            curr = curr.children[i]
        curr.endOfWord = True # blue

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.endOfWord # blue

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True # blue