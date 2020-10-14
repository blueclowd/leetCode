'''
Description:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        return self.dfs(root, key)

    def dfs(self, root, key) -> TreeNode:
        ''' Given the root, return new root without node having value key'''

        if not root:
            return None

        if root.val < key:
            root.right = self.dfs(root.right, key)

        elif root.val > key:
            root.left = self.dfs(root.left, key)

        else:

            # Case 1: leaf node
            if not root.left and not root.right:
                return None

            # Case 2: has both left and right
            if root.right and root.left:
                # Replace the current node with the largest in the left node
                node = root.left

                while node.right:
                    node = node.right

                largest_in_the_left = node.val

                # Delete target node and replace the root
                root.val = largest_in_the_left
                root.left = self.dfs(root.left, largest_in_the_left)

                return root

            # Case 3: has either left or right
            else:
                return root.left if root.left else root.right

        return root



