#include "functionInterface.h"
#include <stdlib.h>

/**
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    int v1 = 0;
    int v2 = 0;

    int sum = 0;
    int carry = 0;

    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* current = head;

    while (l1 || l2 || carry)
    {
        v1 = (l1 == NULL)? 0 : l1->val;
        v2 = (l2 == NULL)? 0 : l2->val;

        // Calculate sum and carry
        sum = v1 + v2 + carry;
        carry = sum / 10;
        sum = (sum >= 10) ? sum - 10 : sum;

        // Prepare new node
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = sum;
        newNode->next = NULL;

        // Update current node
        current->next = newNode;
        current = current->next;

        // Foward if not NULL
        l1 = (l1 == NULL)? l1 : l1->next;
        l2 = (l2 == NULL)? l2 : l2->next;
    }

    return head->next;

}
