class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

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

    def addWord(self, word: str) -> None:
        curr = self.root
        # iterate through every char in the word
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # add children to trie
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # try every child for the dot
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word  # reached the end, so is it a real word?

        return dfs(0, self.root)
