class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001 # one slot per possible key (0 to 10^6), -1 means empty

    def put(self, key: int, value: int) -> None:
        self.map[key] = value # key is the index, store value there (overwrites if it exists)

    def get(self, key: int) -> int:
        return self.map[key] # value if we put one, otherwise still -1

    def remove(self, key: int) -> None:
        self.map[key] = -1 # mark the slot empty again

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)