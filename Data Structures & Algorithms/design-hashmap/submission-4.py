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
        curr = self.map[self.hash(key)] # start at bucket's dummy head
        while curr.next: # look at each real node in the bucket
            if curr.next.key == key: # key already exists, overwrite with a new value
                curr.next.val = value
                return
            curr = curr.next # move onto the next kv pair
        curr.next = ListNode(key, value) # reached the end without finding it, add a new node

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)].next # skip dummy and start at the first real node
        while curr:
            if curr.key == key: # this node holds the key we're looking for (other keys can share the bucket)
                return curr.val
            curr = curr.next
        return -1 # went through the whole bucket, key isn't here

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)] # start at the dummy so we're always one node before the target
        while curr.next: # look at each real node in the bucket
            if curr.next.key == key: # the next node is the one to remove
                curr.next = curr.next.next # skip over it, unlinking it from the chain
                return
            curr = curr.next # key wasn't in the bucket, nothing to remove

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)