
# this is a new class
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key : node

        # left = LRU, right = MRU
        # LRU = least recently used
        # MRU = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0) # dummy nodes
        # initially connected to each other
        self.left.next, self.right.prev = self.right, self.left

    # this is new (for get func)
    # remove node from list
    # pointer manipulation
    def remove(self, node):
        # if we have [] [] [] where they all connect to each other doubly LL
        # redirect prev to next.next
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # this is new as well (for get func)
    # insert node at right side
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: # if key exists
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # tells us the node since each key is mapped to a node
        return -1

        # every time we get a value, we want to update the most recently used

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # node already exists in our list with that same key val
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        # doubly ll so insert
        self.insert(self.cache[key])

        # does length of cache now exceed capacity?
        if len(self.cache) > self.cap:
            # remove from the LL and delete the LRU from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        
