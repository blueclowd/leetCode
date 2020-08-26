'''
Description:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        self.table = {}

        self.dfs(root, 0)

        output = []

        for level, values in sorted(self.table.items(), key=lambda pair: pair[0]):
            output.append(max(values))

        return output

    def dfs(self, root, row):

        if not root:
            return
        else:
            if row in self.table:
                self.table[row].append(root.val)
            else:
                self.table[row] = [root.val]

        self.dfs(root.left, row + 1)
        self.dfs(root.right, row + 1)