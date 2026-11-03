# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root): # return the height here
            nonlocal res # global variable

            if not root: # base case where root == null so we return 0
                return 0

            left = dfs(root.left) # run dfs on left subtree
            right = dfs(root.right) # run dfs on right subtree

            res = max(res, left + right) # take best diameter so far compared to other diameters
            return 1 + max(left, right) # +1 for the curr node we're at 
            # either max of the left or the right subtree

        dfs(root) # call recursive function at origin

        return res # return best diameter of binary tree