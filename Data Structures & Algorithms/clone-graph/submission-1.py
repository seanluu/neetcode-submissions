"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {} # hashmap (old node -> its copy)
        # necessary since the graph may contain cycles, so we can't copy recursively
        # without remembering what we've already copied

        def dfs(node):
            # if we already made a copy of this node, return that same copy
            # (this also stops us from looping forever when the graph has a cycle)
            if node in oldToNew:
                return oldToNew[node]

            # make a copy of this node (same value, no neighbors yet)
            # this is how we make the deep copy...
            copy = Node(node.val)
            # store the copy BEFORE visiting neighbors, so a neighbor that points back to this node finds it
            # instead of making another copy
            oldToNew[node] = copy

            # copy each neighbor (dfs returns the neighbor's copy) and connect it to our copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # empty graph returns None, otherwise return the copy of the starting node
        return dfs(node) if node else None