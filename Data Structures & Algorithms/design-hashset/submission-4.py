class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        if key not in self.stack: # we add when the key isn't present in the stack, point of the problem
            self.stack.append(key)

    def remove(self, key: int) -> None:
        if key in self.stack: # if the value is in the stack then yes we are able to remove it from the stack
            # pop(i): “take out whatever’s at position i and give it to me”
            # remove(x): “find x and delete it,” and you get nothing back
            self.stack.remove(key) # remove instead of pop since key is a value, not an index

    def contains(self, key: int) -> bool: # explicitly asks for boolean so we can return straight up instead of T/F
        return key in self.stack

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)