'''
Description:
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        self.output = []

        self.dfs(root, [])

        return ["->".join([str(node) for node in path]) for path in self.output]

    def dfs(self, root, path):

        path.append(root.val)

        if not root.left and not root.right:
            self.output.append(path)

        if root.left:
            self.dfs(root.left, path.copy())

        if root.right:
            self.dfs(root.right, path.copy())
