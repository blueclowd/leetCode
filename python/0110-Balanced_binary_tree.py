'''
Description:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.is_balanced = True

        if root:
            self.get_height(root)

        return self.is_balanced

    def get_height(self, root):

        if not root.left and not root.right:
            return 1

        left_height = self.get_height(root.left) if root.left else 0
        right_height = self.get_height(root.right) if root.right else 0

        if abs(left_height - right_height) > 1:
            self.is_balanced = False

        return max(left_height, right_height) + 1