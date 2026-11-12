class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        if key not in self.stack: # we add when the key isn't present in the stack, point of the problem
            self.stack.append(key)
        #     return True
        # else: # since this is a set, we shouldn't have dupe key values so we default to return False
        #     return False

    def remove(self, key: int) -> None:
        if key in self.stack: # if the value is in the stack then yes we are able to remove it from the stack
            # pop(i): “take out whatever’s at position i and give it to me”
            # remove(x): “find x and delete it,” and you get nothing back
            self.stack.remove(key) # remove instead of pop since key is a value, not an index
        #     return True
        # else: # value must not be in the stack so it's impossible to remove already, return False
        #     return False

    def contains(self, key: int) -> bool:
        return key in self.stack
        # else:
        #     return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)