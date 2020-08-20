# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.sorted_list = []
        self.inorder(root)
        self.current_ptr = -1

    def inorder(self, root: TreeNode):
        if not root:
            return

        self.inorder(root.left)
        self.sorted_list.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """

        self.current_ptr += 1

        return self.sorted_list[self.current_ptr]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """

        return self.current_ptr < len(self.sorted_list) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()