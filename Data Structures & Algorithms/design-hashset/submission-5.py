class MyHashSet():

    def __init__(self):
        self.stack = []

    def add(self, key):
        if key not in self.stack:
            self.stack.append(key)
        
    def contains(self, key):
        return key in self.stack

    def remove(self, key):
        if key in self.stack:
            self.stack.remove(key)