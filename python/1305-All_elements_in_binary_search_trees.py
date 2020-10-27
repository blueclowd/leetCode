'''
Description:
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted_nodes1 = []
        self.inorder(root1, sorted_nodes1)

        sorted_nodes2 = []
        self.inorder(root2, sorted_nodes2)

        print(sorted_nodes1, sorted_nodes2)

        sorted_nodes1 += sorted_nodes2
        sorted_nodes1.sort()

        return sorted_nodes1

    def inorder(self, root, sorted_nodes):
        if not root:
            return

        self.inorder(root.left, sorted_nodes)
        sorted_nodes.append(root.val)
        self.inorder(root.right, sorted_nodes)