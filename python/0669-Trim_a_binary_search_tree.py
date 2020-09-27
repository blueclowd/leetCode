'''
Description:
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        self.low = low
        self.high = high

        return self.get_valid_tree(root)

    def get_valid_tree(self, root):

        if not root:
            return root

        if root.val > self.high:
            return self.get_valid_tree(root.left)

        if root.val < self.low:
            return self.get_valid_tree(root.right)

        root.left = self.get_valid_tree(root.left)
        root.right = self.get_valid_tree(root.right)

        return root