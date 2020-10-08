'''
Description:
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        self.sum = sum
        self.n_paths = 0
        self.dfs(root)

        return self.n_paths

    def dfs(self, root):

        if not root:
            return []

        left_sums = self.dfs(root.left)
        right_sums = self.dfs(root.right)

        sums = [root.val]

        if left_sums:
            sums += [left_sum + root.val for left_sum in left_sums]

        if right_sums:
            sums += [right_sum + root.val for right_sum in right_sums]

        for value in sums:
            if value == self.sum:
                self.n_paths += 1

        return sums