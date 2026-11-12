class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    # can use a hash table with separate chaining to 
    # reduce memory usage to be just as effective as a hashmap

    # create an array of buckets (smaller than the key range) 
    # and use a hash function (key modulo bucket count) to determine
    # which bucket a key belongs to. each bucket is a LL that stores k-v pairs
    # this handles collisions by chaining multiple entries in the same bucket

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    # this is new
    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)