'''
Description:
Sort a linked list using insertion sort.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        leading_node = ListNode(0, head)
        current_node = head

        while current_node.next:

            if current_node.next.val >= current_node.val:

                current_node = current_node.next

            else:

                current = leading_node
                next_node = current_node.next

                current_node.next = current_node.next.next

                while next_node.val > current.next.val:
                    current = current.next

                next_node.next, current.next = current.next, next_node

        return leading_node.next




