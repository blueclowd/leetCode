'''
Description:
Write a program to find the node at which the intersection of two singly linked lists begins.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        current_A, current_B = headA, headB

        if not current_A or not current_B:
            return None

        n_visited_end = 0

        while current_A != current_B and n_visited_end < 4:

            if current_A.next:
                current_A = current_A.next
            else:
                current_A = headB
                n_visited_end += 1

            if current_B.next:
                current_B = current_B.next
            else:
                current_B = headA
                n_visited_end += 1

        if current_A == current_B:
            return current_A
        else:
            return None


