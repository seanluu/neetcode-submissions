"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(node):
            # if node has been seen before, return the prev mapped version
            if node in oldToNew:
                return oldToNew[node]

            # make a copy of this node (same value, no neighbors yet)
            copy = Node(node.val)
            oldToNew[node] = copy # store copy b4 visiting neighbors 
            # so a neighbor that points back to this node finds it

            # iterate through each neighbor (copy each neighbor) and connect it to our copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # empty graph returns None, otherwise we ret the copy of the starting node (dfs(node))
        return dfs(node) if node else None