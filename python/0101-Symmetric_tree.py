# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        queue = [root.left, root.right]

        while queue:

            node_1 = queue.pop(0)
            node_2 = queue.pop(0)

            if not node_1 and not node_2:
                continue

            if not node_1 or not node_2:
                return False

            if node_1.val == node_2.val:

                queue.append(node_1.left)
                queue.append(node_2.right)

                queue.append(node_1.right)
                queue.append(node_2.left)

            else:

                return False

        return True

# Recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, node_1, node_2):

        if not node_1 and not node_2:
            return True

        if not node_1 or not node_2:
            return False

        return node_1.val == node_2.val and self.is_mirror(node_1.left, node_2.right) and self.is_mirror(node_1.right,
                                                                                                         node_2.left)