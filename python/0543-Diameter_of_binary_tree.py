'''
Description:
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0

        self.get_longest(root)

        return self.max_length

    def get_longest(self, root):
        if not root:
            return 0

        left_depth = self.get_longest(root.left)
        right_depth = self.get_longest(root.right)

        self.max_length = max(self.max_length, left_depth + right_depth)

        return max(left_depth, right_depth) + 1